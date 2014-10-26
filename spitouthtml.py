#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script takes a Python dictionary of newspaper stories
# and turns them into HTML files, including an index.html page.

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
    def __init__(self, story, article_index):
        self.story = story
        self.article_index = article_index

    def headline(self):
        return self.story["headline"]

    def pubdate(self):
        return parse(self.story["date"]).strftime("%A, %d %B %Y")

    def verbiage(self):
        return self.story["body"]

# def next
# def previous
#      using the headline/date from the "index"


class IndexOutput(object):
    def __init__(self, article_index):
        self.article_index = article_index

    def stories(self):
        # This would be better as a Pystache partial or
        # iteration if I could figure that out.
        toc = ""
        for storydesc in self.article_index:
            dateURL = parse(storydesc["date"]).strftime("%d-%B-%Y") + ".html"
            toc += '<li><a href="' + dateURL + '">' + storydesc["headline"] + "</a>, " + parse(storydesc["date"]).strftime("%A, %d %B %Y") + "</li>"
        return toc

def htmlize_story(story, article_index):
    '''use pystache to turn each storydict into HTML to output,
    take HTML string and write it to a file'''
    storyoutput = HtmlOutput(story, article_index)
    dateslug = parse(story["date"]).strftime("%d-%B-%Y") + ".html"
    renderer = pystache.Renderer()
    with codecs.open(dateslug, encoding='utf-8', mode='w') as f:
        f.write(renderer.render(storyoutput))

def htmlize_article_index(article_index):
    '''use pystache to turn the list into HTML to output,
    take HTML string and write it to a file '''
    indexoutput = IndexOutput(article_index)
    renderer = pystache.Renderer()
    with codecs.open("index.html", encoding='utf-8', mode='w') as f:
        f.write(renderer.render(indexoutput))


if __name__ == "__main__":
    (article_list, article_index) = parsearticles.parse_files(parsearticles.ARCHIVEFILES, [])
    htmlize_article_index(article_index)
    for article in article_list:
        htmlize_story(article, article_index)

