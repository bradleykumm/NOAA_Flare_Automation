#NOAA_events_collector.py

#---------------------------------------------------------------------------------------------------
#IMPORTS
import datetime
import os
from ftplib import FTP
import urllib
import pickle

#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#DEFINING NEEDED FUNCTIONS
def day_adder(date):
	"""
	ADDS A DAY TO THE GIVEN [YYYY,MM,DD] DATE AND RETURNS THE NEW DATE IN THE SAME FORMAT
	"""
	#extracting year month and day from inpute date
	year = date[0]
	month = date[1]
	day = date[2]

	#days per month
	days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
	if year % 4 == 0:
		days_per_month[1] += 1

	#finding the next date
	day += 1

	if day == (days_per_month[month - 1] + 1):
		day = 1
		month += 1

		if month == 13:
			year += 1
			month = 1

	return([year,month,day])


def day_before(date):
	"""
	FOR A DATE [YYYY,MM,DD] RETURNS THE DATE OF THE PREVIOUS DAY
	"""
	#extracting year month and day from inpute date
	year = date[0]
	month = date[1]
	day = date[2]

	#days per month
	days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
	if year % 4 == 0:
		days_per_month[1] += 1

	#finding the previous day's date
	day += -1
	if day == 0:
		day = days_per_month[month - 2]
		month += -1
		if month == 0:
			month = 12
			year += -1
	return([year,month,day])

def yyyymmdd(date):
	"""
	CONVERTS [YYYY,MM,DD] DATE TO YYYYMMDD STRING
	"""
	year = str(date[0])

	month = str(date[1])
	if len(month) == 1:
		month = '0' + month

	day = str(date[2])
	if len(day) == 1:
		day = '0' + day


	yyyymmdd = year + month + day
	return yyyymmdd

#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#EXTRACTING TODAYS DATE AND CREATING THE NECESSARY DIRECTORIES
date = datetime.datetime.now()

year = str(date)[0:4]
month = str(date)[5:7]
day = str(date)[8:10]
today = [ int(year) , int(month) , int(day) ]
yesterday = day_before(today)

this_year_dir =  "./%s_events" % year
last_year_dir =  "./%d_events" % (int(year) - 1)


if not os.path.exists(this_year_dir):
	os.makedirs(this_year_dir)
if not os.path.exists(last_year_dir):
	os.makedirs(last_year_dir)
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#RETRIEVING THE FILES (FTP)

#for the last 30 days download any missing events files
day = today
downloaded_files = []
for i in range(30):

	day = day_before(day)
	year = str(day[0])
	filename = yyyymmdd(day) + "events.txt"
	file_comp_path = "./%s_events/%s" % (year,filename)
	prev_dir_path = "./NOAA_events/%s_events/%s" % (year,filename)

	if not os.path.exists(file_comp_path):
		#save file_comp_path to downloaded files so it can be pickled here and unpickled by another startup program
		downloaded_files.append(prev_dir_path)

		#loging in to the server
		ftp = FTP('ftp.swpc.noaa.gov','anonymous','***************')
		ftp.cwd('/pub/indices/events/')

		#retrieving the file
		localfile = open(filename,'wb')
		ftp.retrbinary('RETR ' + filename,localfile.write)
		ftp.quit()
		localfile.close()
		current_path = "./%s" % filename
		os.rename(current_path , file_comp_path)
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#pickling the downloaded file paths(used by flare_list_updater.py)
#pickle_file = open("../NOAA_downloaded.pkl","w")
#pickle_file.close()
pickling_file = open("../NOAA_downloaded.pkl","wb")
pickling_file.truncate()
pickle.dump(downloaded_files,pickling_file)
pickling_file.close()

#---------------------------------------------------------------------------------------------------











