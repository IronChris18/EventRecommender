import os, subprocess

path = "/home/carberr2/cs410/EventRecommender/child_pages/"

i = 1
for fname in os.listdir(path):
	f = path+fname
	if not os.path.isfile(f):
		print "not real file: " +fname
		#os.remove(fname)
		continue
	print "sup dawg"
	file = open(f, "r")
	url = "hello"
	print file
	j = 0
	for line in file.readlines():
		if(j == 0):
			garbage = line # file.readline()
			j = j+1
			continue
		url = line #file.readline()
		print "inside file: "+url
		url = str(url[:-1])
		page = "event_"+str(i)+".txt"
		subprocess.call(["phantomjs","../getHtml.js",url,page])
		print str(i)
		i = i + 1
	file.close()
