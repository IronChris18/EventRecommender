
var page = require('webpage').create();
var url = 'http://www.illinois.edu/calendar/IllinoisCalendarList';

// for debug (to see if page returns status code 200)
page.onResourceReceived = function(response) {
    if (response.url === url) {
        console.log('Resorce: "' + response.url + '" status: '  + response.status);

        if (response.status === 200) {
            console.log(response.url);
            for (var i = 0; i < response.headers.length; i++) {
                console.log(response.headers[i].name + ': ' + response.headers[i].value);
            }
        }
    }
};

page.onLoadFinished = function(status){
    console.log('Status: ' + status);

    console.log('Starting evaluate...');
    var links = page.evaluate(function() {
        var nodes = [],
            matches = document.querySelectorAll("a.listing-thumb");

            for(var i = 0; i < matches.length; ++i) {
                nodes.push(matches[i].href);
            }

            return nodes;
    });
    console.log('Done evaluate... count: ' + links.length);

    if (links && links.length > 0) {
        for(var i = 0; i < links.length; ++i) {
            console.log('(' + i + ') ' + links[i]);
        }
    } else {
        console.log("No match found!");
    }

    phantom.exit(0);
};

page.open(url);
