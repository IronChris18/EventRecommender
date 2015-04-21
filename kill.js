
var page = require('webpage').create();
var url  = 'http://illinois.edu/calendar/IllinoisCalendarList';

page.open(url, function() {
    //Get parent link
    var parent = page.evaluate(function() {
        var test = document.querySelectorAll('li a');
        return Array.prototype.map.call(test, function(elem) {
            return elem.href;       
        });
    });
    for(var i=0; i < parent.length; i++){
        //Print parent link 
        console.log("Parent link: " + parent[i]);

        //Then open child link          
        page.open(parent[i],function(){         
            //console.log(document.title);          
            var child = page.evaluate(function() {
                var test = document.querySelectorAll('div.productRow');
                return Array.prototype.map.call(test, function(elem) {
                    return elem.innerHTML;      
                });
            }); 
            console.log(child.length);
            phantom.exit();
        });

    }

});
