#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script takes a Python list of stories
# and turns it into an "index.html" page.

import codecs
import parsearticles
import pystache
from os import path
from dateutil.parser import parse

# An individual "article" or "story" is a dictionary with
# doc_id
# headline
# date
# wordcount
# body


class IndexOutput(object):
    def __init__(self, article_index):
        self.article_index = article_index

    # def headline(self):
    #     for story in self.article_list:
    #         yield story["headline"]

    # def date(self):
    #     for story in self.article_list:
    #         yield parse(self.story["date"]).strftime("%A, %d %B %Y")

    def stories(self):
        x = ""
        for story in self.article_index:
            dateURL = parse(story["date"]).strftime("%d-%B-%Y") + ".html"
            x += '<li><a href="' + dateURL + '">' + story["headline"] + " " + parse(story["date"]).strftime("%A, %d %B %Y") + "</a></li>"
        return x

# def next
# def previous
#      using the headline/date from the "index"


def htmlize_article_index(article_index):
    '''use pystache to turn the list into HTML to output,
    take HTML string and write it to a file '''
    output = IndexOutput(article_index)
    renderer = pystache.Renderer()
    with codecs.open("index.html", encoding='utf-8', mode='w') as f:
        f.write(renderer.render(output))

if __name__ == "__main__":
    article_index = parsearticles.parse_file(parsearticles.ARCHIVEFILE, [])[1]
    htmlize_article_index(article_index)

