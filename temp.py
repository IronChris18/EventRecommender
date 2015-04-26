"""
	Run this python script within child_pages to avoid
	creating 619 new files in the parent directory
"""

import os, subprocess

""" open each child page and get html info"""

temp = "http://illinois.edu/calendar/detail/1447?eventId=32007637&calMin=201504&cal=20150425&skinId=10312"

page = "intint.txt"

subprocess.call(["phantomjs","../getHtml.js",temp,page]) #no html data


#os.system("wget "+temp)	#get html data
