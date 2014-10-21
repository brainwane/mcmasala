#!/usr/bin/python

# This script takes a Python dictionary of newspaper stories
#  and turns them into HTML files.

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
    pass

def clean_html(body):
    ''' clean up unnecessary characters in the story body
    return a big string of HTML and a slug string'''
    pass

def write_page(story_html, slug):
    ''' takes HTML string and writes it to a file '''
    pass

if __name__ == "__main__":
    pass
