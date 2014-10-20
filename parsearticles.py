#!/usr/bin/python

import re
from bs4 import BeautifulSoup

def parse_file():
    with open("../../Documents/62-articles.htm") as f:
        cols = f.read()
    soup = BeautifulSoup(cols)
    articles = soup.find_all("div", attrs={"class": "article"})
    article_list = []
    for article in articles:
        article_list.append(parse_article(article))
    return article_dict # JSON time!

def parse_article(element):
    article_data = {}
    docid_string = element.find("p", text=re.compile("Document"))
    # do a regex to find the actual OKLD.... string; add to dictionary
    article_data["headline"] = element.find("div", id="hd").contents[0].contents[0]
    # text of article is after "all rights reserved" and before the Document ID
    return article_data

if __name__ == "__main__":
    parse_file()
