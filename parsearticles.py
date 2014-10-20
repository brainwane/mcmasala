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
        # append it to the list
        pass
    return article_dict # JSON time!

def parse_article(element):
    article_data = {}
    docid_string = element.find_all("p", text=re.compile("Document"))
    # do a regex to find the actual OKLD.... string; add to dictionary
    headline_string = element.find_all("div", id="hd")
    # use BS to find the string in the child "b" tag here; add to dictionary
    # text of article is after "all rights reserved" and before the Document ID


if __name__ == "__main__":
    parse_file()
