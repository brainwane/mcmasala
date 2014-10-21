#!/usr/bin/python

# This script takes a Python dictionary of newspaper stories
# and turns them into HTML files.

import re
import json
import io
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
    return a giant string '''
    pagestart = "<html><head><title>"
    title_to_body = "</title></head><body>"
    hed = "<div class='hed'>" + story["headline"]+"</div>"
    byline = ("<p class='byline'>by Sumana Harihareswara, " +
              parse(story["date"]).isoformat() + "</p>")
    story_body = "<div class='story'>" + clean_html(story["body"]) + "</div>"
    footer = ("<div class='footer'" +
              "A <a href='http://harihareswara.net'>Sumana Harihareswara</a> website"
              + "</div>")
    pageend = "</body></html>"
    output = (pagestart + story["headline"] + title_to_body + hed +
              byline + story_body + footer + pageend)

def clean_html(body):
    ''' clean up unnecessary characters in the story body
    return a big string of HTML and a slug string'''
    return body

def write_page(story_html, slug):
    ''' takes HTML string and writes it to a file '''
    pass

if __name__ == "__main__":
    pass
