#!/user/bin/python

import sys
import os
import re
import string
from os import listdir
from os.path import isfile, join

path = "/home/carberr2/cs410/EventRecommender/cleaned_files"
path_out = "/home/carberr2/cs410/EventRecommender"
EVENT_STRING = ""
DATE_STRING = ""
LOCATION_STRING = ""
TIME_STRING = ""
BIO_STRING = ""
event_flag = 0;
get_next_line_date = 0;
get_next_line_time = 0;
get_next_line_location = 0;  

json_file = open(path_out + "/jsonfile.txt", 'a')

def check_date( check_line ):
	global get_next_line_date
	check_line = check_line.replace("Date","",1)
	if not check_line.split():
		get_next_line_date = 1;
		return check_line;
	return check_line;

def check_time( check_line ):
	global get_next_line_time
	check_line = check_line.replace("Time","",1)
	if not check_line.split():
		get_next_line_time = 1;
		return check_line;
	return check_line;

def check_location( check_line ):
	global get_next_line_location
	check_line = check_line.replace("Location","",1)
	if not check_line.split():
		get_next_line_location = 1;
		return check_line;
	return check_line;
	
	
for dir_entry in os.listdir(path):
	dir_entry_path = os.path.join(path, dir_entry)
	if os.path.exists(dir_entry_path):
		with open(dir_entry_path, 'r') as my_file:
			for line in my_file:
				if event_flag == 0:
					EVENT_STRING = line
					event_flag = 1
				if get_next_line_date == 1:
					DATE_STRING = line
					get_next_line_date = 0
				if get_next_line_time == 1:
					TIME_STRING = line
					get_next_line_time = 0
				if get_next_line_location == 1:
					LOCATION_STRING = line
					get_next_line_location = 0
				if "Date" in line:
					DATE_STRING = check_date(line)
				if "Time" in line:
					TIME_STRING = check_time(line)
				if "Location" in line:
					LOCATION_STRING = check_location(line)
				if "BIO" in line:
					BIO_STRING = line[4:]
					if not BIO_STRING.split():
						BIO_STRING = "N/A"				
			EVENT_STRING = EVENT_STRING.rstrip()
			DATE_STRING = DATE_STRING.rstrip()
			TIME_STRING = TIME_STRING.rstrip()
			LOCATION_STRING = LOCATION_STRING.rstrip()
			if not BIO_STRING.split():
				BIO_STRING = "N/A"
			else:
				BIO_STRING = BIO_STRING.rstrip()
			event_flag = 0
		json_file.write('{ "create": { "_index": "team_index", "_type": "doc"}}\n')
		json_file.write('{"doc_id": "' + dir_entry + '", "event" : "' + EVENT_STRING + '", "date" : "' + DATE_STRING + '", "time" : "' + TIME_STRING + '", "location" : "' + LOCATION_STRING + '", "bio" : "' + BIO_STRING + '"}\n')
		my_file.close()
		print dir_entry
				
					
				



