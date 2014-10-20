#!/usr/bin/python

import re
from bs4 import BeautifulSoup, UnicodeDammit
from os import path
from dateutil.parser import parse

def parse_file():
    file_path = path.relpath("../../Documents/factiva/62-articles.htm")
    with open(file_path) as f:
        newsfile = f.read()
    cols = UnicodeDammit.detwingle(newsfile)
    soup = BeautifulSoup(cols)
    articles = soup.find_all("div", attrs={"class": "article"})
    article_list = []
    for article in articles:
        article_list.append(parse_article(article))
    return article_list # JSON time!

def parse_article(element):
    article_data = {}
    article_data["doc_id"] = element.find("p", text=re.compile("Document")).contents[0].strip("Document ")
    article_data["headline"] = element.find("div", id="hd").contents[0].contents[0]
    date = element.find("div", text=re.compile("The Oakland Tribune")).previous_element
    article_data["date"] = parse(date)
    wordcountstring = element.find("div", text=re.compile("The Oakland Tribune")).previous_sibling.previous_sibling.contents[0]
    article_data["wordcount"] = int(wordcountstring.strip(" words"))
    article_text = ""
    rights_tag = element.find("div", text=re.compile("All rights reserved"))
    for paragraph in rights_tag.next_element.next_element.next_siblings:
        article_text = article_text + repr(paragraph)
    # text of article is after "all rights reserved" and before the Document ID
    article_text = article_text.rpartition("<p>Document OKLD")[0]
    article_data["body"] = article_text
    return article_data

if __name__ == "__main__":
    parse_file()
