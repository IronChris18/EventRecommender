"""
	Run this python script within child_pages to avoid
	creating 619 new files in the parent directory
"""

import os, subprocess

#get parent names
os.system('phantomjs ../getParent.js ../names.txt')
#get parent links
os.system('phantomjs ../getParent.js ../links.txt')
#replace spaces with underscores in calendar names
os.system('sed -i s/\ /\_/g ../names.txt')
os.system('sed -i s/\,//g ../names.txt')

#read output file to get links and link names
file = open('../links.txt', "r")
name = open('../names.txt', "r")

""" open each child page and get html info"""
for j in range(0, 5):
	garbage = name.readline()	# name child pages something useful
for i in range(0, 620):
	if(i == 0):
		garbage = file.readline()
		continue
	
	url = file.readline()	#get child_page url
	#page = 'page_'+str(i)+'.txt'	#name child pages numerically
	page = name.readline()	#get calendar page name
	#print url
	temp = str(url[:-1])	#remove newline character on url
	page = str(page[:-1])+".txt"	#same for page names
	subprocess.call(["phantomjs","../getChildren.js",temp,page]) #no html data
	#os.system("wget "+temp)	#get html data

file.close()

