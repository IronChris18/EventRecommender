#!/user/bin/python

import sys
import os
import re
import string
from os import listdir
from os.path import isfile, join

path = "/home/carberr2/cs410/EventRecommender/event_pages"
path_out = "/home/carberr2/cs410/EventRecommender/cleaned_files/"
data_list = [];
date_flag = 0;
time_flag = 0;
location_flag = 0;
found_buffer = 0;
found_bio = 0;

first_line = 0;
get_next_line_bio = 0;
check_no_more = 0;
counter = 0;
title_line = "";
bio_line = "";

def check_list( list_check ):
	global time_flag
	global date_flag
	global location_flag
	global found_buffer
	for item in list_check:
		if "Time" in item:
			time_flag = 1
		if "Date" in item:
			date_flag = 1
		if "Location" in item:
			location_flag = 1
	if (time_flag + date_flag + location_flag == 3):
		date_flag = 0
		time_flag = 0
		location_flag = 0
		found_buffer = 1;
		return found_buffer;
	date_flag = 0;
	time_flag = 0;
	location_flag = 0
	found_buffer = 0;
	return found_buffer;

def write_list( correct_list ):
	file_name = path_out+"list" + str(counter) + ".txt"
	with open(file_name, "a") as my_doc:
		my_doc.write(title_line)
		for line in correct_list:
			line.rstrip()
			my_doc.write(line)
		#my_doc.write(bio_line)
		my_doc.close()		
		return;

def write_bio_line( correct_line ):
	file_name = path_out+"list" + str(counter) + ".txt"
	with open(file_name, "a") as my_doc:
		my_doc.write(correct_line)
		my_doc.close()
		return;

for dir_entry in os.listdir(path):
	dir_entry_path = os.path.join(path, dir_entry)
	counter = counter + 1
	if os.path.exists(dir_entry_path):
		with open(dir_entry_path, 'r') as my_file:
			print dir_entry_path
			#counter += counter + 1
			for line in my_file:
				if first_line == 0:
					title_line = line
					first_line = 1
					print title_line
				if get_next_line_bio == 1:
					bio_line = "BIO " + line
					get_next_line_bio = 0
					found_bio = 1
				if "Originating Calendar" in line:
					get_next_line_bio = 1
				if not line.split():
					if check_no_more == 0:
						found_buffer = check_list(data_list)
						if found_buffer == 1:
							write_list(data_list)
							check_no_more = 1
						else:
							#print data_list
							data_list[:] = []
				#if found_buffer == 1:
				#	#print data_list
				#	found_buffer = 0
				#	first_line = 0
				#	data_list[:] = []
				#	break
				if found_buffer == 0:
					data_list.append(line)
			if found_buffer == 1:
				if found_bio == 1:
					write_bio_line(bio_line)
			data_list[:] = []
			check_no_more = 0
			found_buffer = 0
			found_bio = 0
			first_line = 0
	data_list[:] = []

					
						
				


