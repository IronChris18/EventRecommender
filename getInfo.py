import os, subprocess

#get parent names
print "hi\n"
#subprocess.call(["phantomjs","getParent.js","links.txt"])
os.system('phantomjs getLinkNames.js names.txt')
#get parent links
os.system('phantomjs getParent.js links.txt')
print "hello\n"
#read output file to get links
##open each link and retrieve html page
file = open('links.txt', "r")
print "how are you\n"
#for(i=0; i<620; i++):
for i in range(0, 5):
	if(i == 0):
		garbage = file.readline()
		continue
	
	url = file.readline()
	print url+'\n'
	page = 'page_'+str(i)+'.txt'
	print page+'\n'
	os.system('phantomjs getHtml.js'+' '+url+' '+page)
	print 'Page: '+str(i)+'\n'

file.close()
