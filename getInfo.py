import os, subprocess

#get parent names
os.system('phantomjs getLinkNames.js names.txt')
#get parent links
os.system('phantomjs getParent.js links.txt')

#read output file to get links
##open each link and retrieve html page
file = open('links.txt', "r")

#for(i=0; i<620; i++):
for i in range(0, 620):
	if(i == 0):
		garbage = file.readline()
		continue
	
	url = file.readline()
	page = 'page_'+str(i)+'.txt'
	subprocess.call(["phantomjs","getHtml.js",url,page])
	print 'Page: '+str(i)+'\n'

file.close()
