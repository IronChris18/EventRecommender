var page = require('webpage').create();
var system = require('system');
var fs = require('fs');

if(system.args.length !== 2) {
  console.log('Usage: phantomjs text-scraper.js <out>');
  phantom.exit();
}

var url = 'http://illinois.edu/calendar/IllinoisCalendarList';
var outfile = system.args[1];

page.onConsoleMessage = function(msg) {
  console.log(msg);
};

page.open(url, function(status) {
  var output = url + '\n';
  if(status === 'success') {
    setTimeout(function() {
      var text = page.evaluate(function () {
	      return document.title + '\n' + document.body.innerText;	//get link titles in a list
      });
      output += text;
      fs.write(outfile, output);
    }, 1000);
    setTimeout(function () {
      phantom.exit()
    }, 1000);
  } else {
    console.log("Error!")
    phantom.exit()
  }
});
