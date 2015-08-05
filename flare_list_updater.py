#flare_list_updater.py

#---------------------------------------------------------------------------------------------------
#IMPORTS
import os
import pickle
import datetime

from functions import minutes_elapsed, J_date, NOAA_events_reader, helio, MSE_angle

#IMPORTS NEEDED FOR MSE_ANGLE FUNCTION
from sys import argv
from numpy import array, shape, zeros, pi, sqrt, sin, cos, tan, arctan
from math import asin  
#from MSE_Angle import minutes_elapsed, J_date
#from helio_func import MSE_angle
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#unpickling the downloaded files from the NOAA_downloaded.pkl (pickle file created by ./NOAA_evnets/NOAA_events_collector.py)
unpickling_file = open("NOAA_downloaded.pkl","rb")
downloaded_files = pickle.load(unpickling_file)
unpickling_file.close()
os.remove("NOAA_downloaded.pkl")
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
#UPDATING THE FILE

#WRITING THE CURRENT FILE TO THE UPDATED FILE
date = datetime.datetime.now()
yyyymmdd = '%s/%s/%s' % ( str(date)[0:4] , str(date)[5:7] , str(date)[8:10] )
update_line = '#LAST_UPDATED(flare_list_updater.py): %s \n# \n# \n' % yyyymmdd
updated_file = open('FLARE_LIST_UPDATE.txt', 'w')

with open('./FLARE_LIST.txt') as fp:
	lines = fp.readlines()
	for line in lines:
		if 'flare_list_updater.py' in line:
			updated_file.write(update_line)
		else:
			updated_file.write(line)


#WRITING IN THE NEW DATA (CODE FROM: flare_list_creator.py)
	flare_list = open('./FLARE_LIST.txt', 'w')

	for file_path in downloaded_files:
		filename = (file_path.split('/'))[-1]

	
		data = NOAA_events_reader(file_path)
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
					if all(str(date + st + pt + et + loc + angle + pv) not in line for line in lines):
						updated_file.write( date + st + pt + et + loc + angle + pv + '\n' + '\n' )
			else:
				date = add_spaces(str("%s/%s/%s" % (filename[0:4] , filename[4:6] , filename[6:8])) , 23)
				st = add_spaces(str(event[0]),18)
				pt = add_spaces(str(event[1]),16)
				et = add_spaces(str(event[2]),16)
				loc = add_spaces(str(event[3]),10)
				angle = add_spaces(str(MSE_angle([int(filename[0:4]),int(filename[4:6]),int(filename[6:8]),12,00,00])),16)
				pv = add_spaces(str(event[4]),15)
				if all(str(date + st + pt + et + loc + angle + pv) not in line for line in lines):
					updated_file.write( date + st + pt + et + loc + angle + pv + '\n' + '\n' )

	flare_list.close()
updated_file.close()

#REPLACING THE OLD FLARE_LIST.py FILE WITH THE UPDATED FILE
os.remove('./FLARE_LIST.txt')
os.rename('./FLARE_LIST_UPDATE.txt','./FLARE_LIST.txt')

#---------------------------------------------------------------------------------------------------
