
var page = require('webpage').create();
var system = require('system');
var fs = require('fs');

var url  = 'http://illinois.edu/calendar/IllinoisCalendarList';
var outfile = system.args[1];

page.open(url, function() {
    //Get parent link
 	var output = url +'\n';
    var parent = page.evaluate(function() {
        var test = document.querySelectorAll('li a');
        return Array.prototype.map.call(test, function(elem) {
            return elem.href;       
        });
    });
	for(var i = 0; i < parent.length; i++) {

		output += parent[i]+'\n';
	}
	fs.write(outfile, output);
	phantom.exit();
});




/*    for(var i=0; i < parent.length; i++){
        //Print parent link 
        console.log("Parent link: " + parent[i]);

        console.log(i);
        //Then open child link          
        page.open(parent[i],function(){         
            //console.log(document.title);
            //console.log(i);
            child = page.evaluate(function() {
                var test = document.querySelectorAll('week-list');
                return Array.prototype.map.call(test, function(elem) {
                    return elem.innerHTML;      
                });
            }); 
            console.log("child stuff: "+child[0]);
            phantom.exit();
        });

    }
	//phantom.exit();
*/

