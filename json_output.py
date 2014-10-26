#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script takes a Python dictionary of newspaper stories
# and turns it into a JSON file for consumption by Lunr.js.

import json
import parsearticles
from dateutil.parser import parse

# An individual "article" or "story" is a dictionary with
# headline
# date
# body

def date_convert(story):
    ''' Convert a datetime object to a wieldier string.'''
    dateslug = parse(story["date"]).strftime("%d-%B-%Y")
    story["date"] = dateslug
    return story

def write_json(storylist):
    '''write the dict to a JSON file'''
    with open("data.json", "w") as f:
        json.dump(storylist, f, ensure_ascii=False)

if __name__ == "__main__":
    article_list = parsearticles.parse_files(parsearticles.ARCHIVEFILES, [])[0]
    for story in article_list:
        story = date_convert(story)
    write_json(article_list)
