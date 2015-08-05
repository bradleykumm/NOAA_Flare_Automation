#NOAA_organizer.py 
#CHECKS THAT ALL OF THE NOAA EVENTS FILES ARE IN THE DIRECTORY FOR THAT YEAR

#--------------------------------------------------------------------------------------------------
#IMPORTS
import datetime
import os
#--------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------
#DEFINING THE START DATE AND FINDING TODAYS DATE

start_year = 1996

date = datetime.datetime.now()
current_year = int(str(date)[0:4])

#--------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------
#GOING THROUGH ALL OF THE DIRECTORIES AND MOVIING FILES TO THEIR PROPER DIRECTORY

for year in range(start_year,current_year+1):

	year_dir = "./%d_events/" % year

	for file in os.listdir(year_dir):

		file_year = file[0:4]

		if file_year != str(year) and file != 'README':

			current_path = "%s%s"%(year_dir,file)
			new_path = "./%s_events/%s" % (file_year,file)
			os.rename(current_path,new_path)


#DELETING ANY DUPLICATES

for year in range(start_year,current_year + 1):

	year_dir = "./%d_events/" % year

	
	#COMPARING EACH FILE (FILE1) TO ALL OF THE OTHER FILES IN THE DIRECTORY
	del_count = 0
	file_list = os.listdir(year_dir)
	for i in range(len(file_list)):
		for j in range(len(file_list)):
			if not i == j and file_list[i - del_count] == file_list[j - del_count]:
				repeat_year = file_list[i - del_count][0:4]
				repeat_path = "./%s_events/%s" % (repeat_year,file_list[i - del_count])
				os.remove(repeat_path)
				del_count += 1

#-------------------------------------------------------------------------------------------------

