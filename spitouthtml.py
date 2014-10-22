#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script takes a Python dictionary of newspaper stories
# and turns them into HTML files.

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


class HtmlOutput(object):
    def headline(self, story):
        return story["headline"]

    def pubdate(self, story):
        return parse(story["date"]).strftime("%A, %d %B %Y")

    def dateslug(self, story):
        return parse(story["date"]).strftime("%d-%B-%Y") + ".html"

    def verbiage(self, story):
        return story["body"]



def htmlize_story(story):
    '''use pystache to turn the dict into HTML to output,
    take HTML string and write it to a file '''
    output = HtmlOutput()
    dateslug = parse(story["date"]).strftime("%d-%B-%Y") + ".html"
    renderer = pystache.Renderer()
    with codecs.open(dateslug, encoding='utf-8', mode='w') as f:
        f.write(renderer.render(output, story))

if __name__ == "__main__":
    article_lists = parsearticles.parse_all_articles(parsearticles.global_file_list)
    for article_list in article_lists:
        for article in article_list:
            htmlize_story(article)
