**[Site](#site)** |
**[History](#history)** |
**[TODO](#TODO)**

# MC Masala

This repository is for the website containing Sumana Harihareswara's MC Masala newspaper columns -- a static text site with a simple search engine.

## Site

The site isn't quite up yet but I'll link to it here. This repository will contain the back-end scripts I wrote for munging the text, the CSS for styling the site, and the code and hooks for the search.

Requires:

1. Python 3
1. Beautiful Soup 4 and Pystache
1. Nodejs
1. Lunr.js and jQuery - I used [this plugin](https://github.com/slashdotdash/jekyll-lunr-js-search/blob/master/build/search.min.js) plus lunr.min.js

Run:

1. `python3 json_output.py` to create the data file for Lunr to search
1. edit the JSON file slightly to turn the list into the value for a dictionary whose value is `"pages"`
1. `nodejs build_index.js` to create Lunr.js's index file
1. `python3 spitouthtml.py` to create the index.html and individual story files

## History

Between April 2005 and August 2007, I [wrote a weekly column called "MC Masala"](http://www.harihareswara.net/sumana/2011/02/23/0) for the "Inside Bay Area" section of several papers in the San Francisco Bay Area, including the Oakland Tribune. My work circulated to about a million people, I'm told. In 2011 I made [an abortive attempt](http://www.harihareswara.net/masala) to get the columns online but wasn't a strong programmer and thus gave up on all the fiddly bits. Now I'm at [Hacker School](http://hackerschool.com/) and figured this would be a fun and useful way to learn Beautiful Soup and learn to finagle a search engine.

## TODO:
* improve de-duplication (checking dates and headlines)
* figure out why only including search.min.js and not lunr.min.js causes registration problems
* use Pystache more thoroughly instead of string concatenation & other hacks