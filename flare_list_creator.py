#flare_list_creator2.py

#---------------------------------------------------------------------------------------------------
#IMPORTS
import os
import datetime


#IMPORTS NEEDED FOR MSE_ANGLE FUNCTION
from sys import argv
from numpy import array, shape, zeros, pi, sqrt, sin, cos, tan, arctan
from math import asin  
from functions import minutes_elapsed, J_date, helio, MSE_angle, NOAA_events_reader
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#MAKING A STRING LENGTHENER
def add_spaces(string,total_length):
	"""
	ADDS SPACES TO THE END OF A STRING TO MAKE IT THE GIVEN LENGTH
	"""
	while len(string) < total_length:
		string += ' '

	return string

#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#CREATING a list of NOAA_event files to check

#defining global variables
event_file_paths = []


#FINDING THE EVENT YEAR DIRECTORIES and files
dirs = os.listdir('./NOAA_events/')
for dname in dirs:

	if '_events' in dname and 'collector' not in dname:
		event_file_paths.append([dname , [] ])

		files = os.listdir('./NOAA_events/%s/' % dname)

		for fname in files:
			if 'events.txt' in fname:
				event_file_paths[-1][1].append(fname)

#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#CRETING THE FILE AND WRITING THE INITIAL LINES

yyyymmdd = '%s/%s/%s' % ( str(datetime.datetime.now())[0:4] , str(datetime.datetime.now())[5:7] , str(datetime.datetime.now())[8:10] )


flare_list = open('./FLARE_LIST.txt', 'w')
flare_list.truncate()

headers = '#START_DATE(YYYYMMDD)  ' + 'START_TIME(HHMM)  ' + 'MAX_TIME(HHMM)  ' + 'END_TIME(HHMM)  ' + 'LOCATION  ' + 'MSE_ANGLE(DEG)  ' + 'PEAK_VAL(W/m^2)' + '\n'
spacer = '------------------------------------------------------------------------------------------------------------------------------------------------------\n'


#WRITING FILE FORMAT/INFO
flare_list.write('#FLARE_LIST.txt\n')
flare_list.write('#LAST WRITTEN(flare_list_creator.py): %s \n' % yyyymmdd )
flare_list.write('#LAST_UPDATED(flare_list_updater.py): %s \n# \n# \n' % yyyymmdd )
flare_list.write(headers)
flare_list.write(spacer)



#OBTAINING THE INFORMATION FROM EACH FILE IN event_file_list AND WRITING THE NEW INFO TO THE FLARE_LIST

for year_paths in event_file_paths:

	#PRINT THE DIRECTORY THAT IS CURRENTLY BEING EXAMINED
	print "CURRENT DIRECTORY:  %s" % year_paths[0]

	#PRINT THE DATE THAT IS CURRENTLY BEING ANALYZED
	for filename in year_paths[1]:
		print "       CHECKING DATE:  %s/%s/%s" % (filename[0:4] , filename[4:6] , filename[6:8])

		#IF THE MSE ANGLE IS LESS THAN 30 DEG
		#if MSE_angle([int(filename[0:4]),int(filename[4:6]),int(filename[6:8]),12,00,00]) < 30:

		data = NOAA_events_reader("./NOAA_events/%s/%s" % (year_paths[0] , filename) )
		for event in data:
			if event[4] != 'na' and event[4] != 'N.A.':
				if float(event[4]) > 1e-9: 
					date = add_spaces(str("%s/%s/%s" % (filename[0:4] , filename[4:6] , filename[6:8])) , 23)
					st = add_spaces(str(event[0]),18)
					pt = add_spaces(str(event[1]),16)
					et = add_spaces(str(event[2]),16)
					loc = add_spaces(str(event[3]),10)
					angle = add_spaces(str(MSE_angle([int(filename[0:4]),int(filename[4:6]),int(filename[6:8]),12,00,00])),16)
					pv = add_spaces(str(event[4]),15)
					flare_list.write( date + st + pt + et + loc + angle + pv + '\n' + '\n' )
			else:
				date = add_spaces(str("%s/%s/%s" % (filename[0:4] , filename[4:6] , filename[6:8])) , 23)
				st = add_spaces(str(event[0]),18)
				pt = add_spaces(str(event[1]),16)
				et = add_spaces(str(event[2]),16)
				loc = add_spaces(str(event[3]),10)
				angle = add_spaces(str(MSE_angle([int(filename[0:4]),int(filename[4:6]),int(filename[6:8]),12,00,00])),16)
				pv = add_spaces(str(event[4]),15)
				flare_list.write( date + st + pt + et + loc + angle + pv + '\n' + '\n' )



flare_list.close()
#---------------------------------------------------------------------------------------------------



