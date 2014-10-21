#!/usr/bin/python

# This script takes a list of HTML files of my old newspaper columns
# and scrapes them using Beautiful Soup. The result is a dictionary
# containing the stories as structured data: unique doc_id, headline,
# date, body, and wordcount.
# TODO: improve BS usage for performance, also pull out pull quotes
# and "write to her at" end lines.

import re
from bs4 import BeautifulSoup, UnicodeDammit
from os import path

file_list = [
"../../Documents/factiva/Factiva-98-articles.htm",
"../../Documents/factiva/62-articles.htm",
"../../Documents/factiva/Factiva-99-articles.htm",
"../../Documents/factiva/Factiva-30.htm"]
article_list = []

def parse_file(filename):
    file_path = path.relpath(filename)
    with open(file_path) as f:
        newsfile = f.read()
    cols = UnicodeDammit.detwingle(newsfile)
    soup = BeautifulSoup(cols)
    articles = soup.find_all("div", attrs={"class": "article"})
    for article in articles:
        doc_id = article.find("p", text=re.compile("Document")).contents[0].strip("Document ")
        if is_unique(doc_id):
            article_list.append(parse_article(article))

def parse_article(element):
    article_data = {}
    article_data["doc_id"] = element.find("p", text=re.compile("Document")).contents[0].strip("Document ")
    article_data["headline"] = element.find("div", id="hd").contents[0].contents[0]
    # instead of contents[0] try .text or .string
    if element.find("div", text=re.compile("The Oakland Tribune")):
        # consider setting that element.find to a variable -- if not None, look at its .previous_element
        article_data["date"] = element.find("div", text=re.compile("The Oakland Tribune")).previous_element
        wordcountstring = element.find("div", text=re.compile("The Oakland Tribune")).previous_sibling.previous_sibling.contents[0]
        article_data["wordcount"] = int(wordcountstring.strip(" words"))
    article_text = ""
    if element.find("div", text=re.compile("All rights reserved")):
        rights_tag = element.find("div", text=re.compile("All rights reserved"))
        # assign it to rights_tag earlier. can use    if rights_tag
        for paragraph in rights_tag.next_element.next_element.next_siblings:
            # maybe try find_next or find_next_siblings if it is all the <p> tag
            article_text = article_text + repr(paragraph)
            # text of article is after "all rights reserved" and before the Document ID
        article_text = article_text.rpartition("<p>Document OKLD")[0]
        article_data["body"] = article_text
    else:
        print(article_data["headline"]+" has no rightstag")
    return article_data

def is_unique(uniqueid):
    '''Checks whether I've already grabbed this article; the archive HTML files overlap.'''
    for item in article_list:
        if item["doc_id"] == uniqueid:
            return False
    return True

if __name__ == "__main__":
    for archivefile in file_list:
        parse_file(archivefile)
    print(len(article_list))
    return article_list

