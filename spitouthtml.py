#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script takes a Python dictionary of newspaper stories
# and turns them into HTML files.

import codecs
import parsearticles
from os import path
from dateutil.parser import parse

# An individual "article" or "story" is a dictionary with
# doc_id
# headline
# date
# wordcount
# body

def htmlize_story(story):
    ''' turn the dict into HTML
    return a giant string plus a datestring for the filename'''
    pagestart = "<html><head><title>"
    title_to_body = "</title><link rel='stylesheet' href='../style.css'></head><body>"
    hed = "<div class='story'><h2 class='hed'>" + story["headline"]+"</h2>"
    byline = ("<p class='byline'>by Sumana Harihareswara, " +
              parse(story["date"]).strftime("%A, %d %B %Y") + "</p>")
    story_body = "<div class='verbiage'>" + story["body"] + "</div></div>"
    footer = ("<div class='footer'>" +
              "A <a href='http://harihareswara.net'>Sumana Harihareswara</a> website"
              + "</div>")
    navbar = """<aside class='sidebar'>
Part of <a href="https://github.com/brainwane/mcmasala">MC Masala</a>
<nav role='navigation'>
<ul>
<li><a href="https://github.com/brainwane/mcmasala">Next</a></li>
<li><a href="https://github.com/brainwane/mcmasala">Previous</a></li>
<li><a href="../">Go up a level</a></li>
<ul>
</nav>
</aside>"""
    pageend = "</body></html>"
    output = (pagestart + story["headline"] + title_to_body + hed +
              byline + story_body + footer + navbar + pageend)
    dateslug = parse(story["date"]).strftime("%d-%B-%Y") + ".html"
    return output, dateslug

def write_page(story_html, slug):
    ''' takes HTML string and writes it to a file '''
    with codecs.open(slug, encoding='utf-8', mode='w') as f:
        f.write(story_html)

if __name__ == "__main__":
    article_lists = parsearticles.parse_all_articles(parsearticles.global_file_list)
    for article_list in article_lists:
        for article in article_list:
            (html, filename) = htmlize_story(article)
            write_page(html, 'stories/{}'.format(filename))
