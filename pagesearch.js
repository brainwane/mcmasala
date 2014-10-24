/* Borrowed a lot from https://github.com/jdomingu/Lunr.HTML.Scrape.Search/blob/master/search.js */
/* Much thanks to Nicholas Cassleman for guidance */

idx = lunr.Index.load(the_index);

function lunrsearch() {
    var query = document.getElementById('search-query').value;
    var result = idx.search(query);
    if (result.length !== 0) {
	var formatted_result = "<strong>Results</strong>";
	for (var i = 0; i < result.length; i++) {
	    var pubdate = result[i]['ref'];
	    formatted_result += "<br>" + pubdate;
	}
	document.getElementById('searchResults').innerHTML = formatted_result;
    }
	else {
	    document.getElementById('searchResults').innerHTML = "<p>No results</p>";
	}
    }
$(document).ready(function() {
  $(window).keydown(function(event){
    if(event.keyCode == 13 && document.getElementById('search-query') == document.activeElement) {
      event.preventDefault();
      lunrsearch();
      return false;}
  });
});

/* event.preventDefault() is to prevent page refresh when the user hits Enter */
