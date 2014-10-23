#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script takes a list of HTML files of my old newspaper columns
# and scrapes them using Beautiful Soup. The result is a dictionary
# containing the stories as structured data: unique doc_id, headline,
# date, body, and wordcount.
# TODO: improve BS usage for performance, also pull out pull quotes
# and "write to her at" end lines.

import re
from bs4 import BeautifulSoup, UnicodeDammit
from os import path
from dateutil.parser import parse

ARCHIVEFILE = "../../Documents/factiva/all-articles.htm"


def parse_article(element):
    article_data = {}
    article_data["doc_id"] = element.find("p", text=re.compile("Document")).text.strip("Document ")
    article_data["headline"] = element.find("div", id = "hd").text.strip("\n").rstrip()
    trib = element.find("div", text=re.compile("The Oakland Tribune"))
    if trib:
        article_data["date"] = trib.previous_element
        wordcountstring = trib.previous_sibling.previous_sibling.text
        article_data["wordcount"] = int(wordcountstring.strip(" words"))
    article_text = ""
    rights_tag = element.find("div", text=re.compile("All rights reserved"))
    if rights_tag:
        for paragraph in rights_tag.next_element.next_element.next_siblings:
            article_text = article_text + repr(paragraph)
            # text of article is after "all rights reserved" and before the Document ID
            article_text = article_text.replace("</p>\'\\n\'", "</p>")
        article_text = article_text.rpartition("<p>Document OKLD")[0]
        article_data["body"] = article_text
    else:
        print(article_data["headline"]+" has no rightstag")
    return article_data

def parse_file(filename, article_list):
    '''Returns a date-sorted list of dictionaries, and a date-sorted list
    of dates-and-headlines dicts.'''
    file_path = path.relpath(filename)
    with open(file_path) as f:
        newsfile = f.read()
    cols = UnicodeDammit.detwingle(newsfile)
    soup = BeautifulSoup(cols, "html5lib")
    articles = soup.find_all("div", attrs={"class": "article"})
    for article in articles:
        headline = article.find("div", id = "hd").text.strip("\n").rstrip()
        if is_unique(headline, article_list):
            article_list.append(parse_article(article))
    article_list.sort(key=lambda k: parse(k["date"]))
    index = [{k:v for (k,v) in story.items() if ("date" in k) or ("headline" in k)} for story in article_list]
    return (article_list, index)

def is_unique(headline, article_list):
    '''Checks whether I've already grabbed this article; the archive HTML files overlap.'''
    for item in article_list:
        if item["headline"] == headline:
            return False
    return True

if __name__ == "__main__":
    parse_file(ARCHIVEFILE, [])
