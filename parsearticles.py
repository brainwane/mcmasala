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

ARCHIVEFILES = ["../../Documents/mcm-archive/all-articles.htm", 
"/home/sumanah/Documents/mcm-archive/leftovers/2005-05-26.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2005-07-28.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2005-08-04.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2005-08-18.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2005-10-09.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2005-11-06.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2005-11-20.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2006-09-10.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2007-05-20.html", 
"/home/sumanah/Documents/mcm-archive/leftovers/2007-06-10.html"]



def parse_archival_article(element):
    ''' I concatenated together a big HTML file of a bunch of my columns.
    This function uses Beautiful Soup to parse it for headline/body/date.'''
    article_data = {}
    article_data["headline"] = element.find("div", id = "hd").text.strip("\n").rstrip()
    trib = element.find("div", text=re.compile("The Oakland Tribune"))
    if trib:
        article_data["date"] = trib.previous_element
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


def parse_leftover_article(soup):
    '''I also grabbed some additional articles from another site.
    They don't have the DocIDs or wordcounts.'''
    article_data = {}
    postdate = soup.find("div", attrs={"class":"articleDate"})
    article_data["date"] = repr(postdate)
    article_data["headline"] = soup.find("meta", attrs={"property": "twitter:title"})["content"]
    body = soup.find("div", id = "articleViewerGroup").previous_element.contents
    prose = ""
    for para in body[3:]:
        prose += repr(para)
    article_data["body"] = prose
    return article_data


def parse_files(filenames, article_list):
    '''Returns a date-sorted list of dictionaries, and a date-sorted list
    of dates-and-headlines dicts.'''
    print("running")
    for filename in filenames:
        file_path = path.relpath(filename)
        print(file_path)
        with open(file_path) as f:
            newsfile = f.read()
        if ".html" in file_path:
            soup = BeautifulSoup(newsfile, "html5lib")
        else:
            cols = UnicodeDammit.detwingle(newsfile)
            soup = BeautifulSoup(cols, "html5lib")
        archival_articles = soup.find_all("div", attrs={"class": "article"})
        for article in archival_articles:
            headline = article.find("div", id = "hd").text.strip("\n").rstrip()
            if is_unique(headline, article_list):
                article_list.append(parse_archival_article(article))
        if archival_articles == []:
            headline = soup.find("meta", attrs={"property": "twitter:title"})["content"]
            if is_unique(headline, article_list):
                article_list.append(parse_leftover_article(soup))
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
    parse_files(ARCHIVEFILES, [])
