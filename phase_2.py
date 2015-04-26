import os, subprocess

path = "/home/carberr2/cs410/EventRecommender/child_pages"

for fname in os.listdir(path):
	if not os.path.isfile(fname):
		print "not real file: " +fname
		os.remove(fname)
		continue

	file = open(fname, "r")
	url = "hello"
	i = 0
	while url != None:
		if(i == 0):
			garbage = file.readline()
			continue
		i++
		url = file.readline()
		url = str(url[:-1])
		page = "page_"+str(i)+".txt"
		subprocess.call(["phantomjs","../getHtml.js",url,page])

	file.close()
