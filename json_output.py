#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script takes a Python dictionary of newspaper stories
# and turns it into a JSON file for consumption by Lunr.js.

import json
import parsearticles
from dateutil.parser import parse

# An individual "article" or "story" is a dictionary with
# * headline
# * date (was potentially a datetime object; converting to string for
#         serialization)
# * body
# * an href tag (we're adding that here as a GUID)

def add_date_url(story):

    '''Add a unique identifier to each story's dict that will be used
    by the search engine: headline as text, href pointing to the URL.
    And convert a datetime object to a wieldier string.'''

    datestring = parse(story["date"]).strftime("%d-%B-%Y")
    story["date"] = datestring
    urldesc = '<a href="' + datestring  + '.html">' + story["headline"] + "</a>"
    story["url"] = urldesc
    return story

def write_json(storylist):

    '''write the dict to a JSON file'''

    with open("data.json", "w") as f:
        json.dump(storylist, f, ensure_ascii=False)

if __name__ == "__main__":
    article_list = parsearticles.parse_files(parsearticles.ARCHIVEFILES, [])[0]
    for story in article_list:
        story = add_date_url(story)
    write_json(article_list)
