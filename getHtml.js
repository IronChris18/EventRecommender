
var page = require('webpage').create();
var system = require('system');
var fs = require('fs');

var url= system.args[1];
var outfile= system.args[2];

console.log("html file: "+outfile);
page.open(url, function() {
    //Get html page
 	//var output = url +'\n';
 	console.log("html open page");
    var output = page.evaluate(function() {
        /*var test = document.querySelectorAll('li a');
        return Array.prototype.map.call(test, function(elem) {
            return elem.href;       
        });*/
		return document.title;// + '\n' + document.body.innerText;
    });
	console.log("before writing file");
	fs.write(outfile, output);
	console.log("after write file");
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
*/
