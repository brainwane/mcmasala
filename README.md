**[Site](#site)** |
**[History](#history)** 

# MC Masala

This repository is for the website containing Sumana Harihareswara's MC Masala newspaper columns -- a static text site with a simple search engine.

## Site

The site isn't quite up yet but I'll link to it here. This repository will contain the back-end scripts I wrote for munging the text, the CSS for styling the site, and the code and hooks for the search.

## History

Between April 2005 and August 2007, I [wrote a weekly column called "MC Masala"](http://www.harihareswara.net/sumana/2011/02/23/0) for the "Inside Bay Area" section of several papers in the San Francisco Bay Area, including the Oakland Tribune. My work circulated to about a million people, I'm told. In 2011 I made [an abortive attempt](http://www.harihareswara.net/masala) to get the columns online but wasn't a strong programmer and thus gave up on all the fiddly bits. Now I'm at [Hacker School](http://hackerschool.com/) and figured this would be a fun and useful way to learn Beautiful Soup and learn to finagle a search engine.

TODO:
* get Lunr branch in shape, including linking with the text of headlines instead of just dates, and merge
* get Next/Previous and Up A Level links working
* improve de-duplication (checking dates and headlines)
* add photo/logo image