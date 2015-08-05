#functions.py

#functions used for NOAA_events_Automation

import os
import datetime
from sys import argv
from math import asin,floor, pi, sin
from numpy import array, shape, zeros, pi, sqrt, sin, cos, tan, arctan



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
def minutes_elapsed(start_time,end_time):
	"""
	start_time and end time are in [yyyy,mm,dd,hh,nn,ss] format
	"""
	#CHECKING THAT START TIME IS BEFORE END TIME AND SWITCHING IF NECESSARY
	neg_time = 1  #will multiply time by this factor and will change to -1 if start_time > end_time
	if start_time[0] > end_time[0]:
		neg_time = -1
		placeholder = start_time
		start_time = end_time
		end_time = placeholder

	elif start_time[0] == end_time[0] and start_time[1] > end_time[1]:
		neg_time = -1
		placeholder = start_time
		start_time = end_time
		end_time = placeholder

	elif start_time[0] == end_time[0] and start_time[1] == end_time[1] and start_time[2] > end_time[2]:
		neg_time = -1
		placeholder = start_time
		start_time = end_time
		end_time = placeholder

	elif start_time[0] == end_time[0] and start_time[1] == end_time[1] and start_time[2] == end_time[2] and start_time[3] > end_time[3]:
		neg_time = -1
		placeholder = start_time
		start_time = end_time
		end_time = placeholder 

	elif start_time[0] == end_time[0] and start_time[1] == end_time[1] and start_time[2] == end_time[2] and start_time[3] == end_time[3] and start_time[4] > end_time[4]:
		neg_time = -1
		placeholder = start_time
		start_time = end_time
		end_time = placeholder

	elif start_time[0] == end_time[0] and start_time[1] == end_time[1] and start_time[2] == end_time[2] and start_time[3] == end_time[3] and start_time[4] == end_time[4] and start_time[5] > end_time[5]:
		neg_time = -1
		placeholder = start_time
		start_time = end_time
		end_time = placeholder







	ys = int(start_time[0])	#start year
	ye = int(end_time[0])	#end year
	ms = int(start_time[1])	#start month
	me = int(end_time[1])	#end month
	ds = int(start_time[2])	#start day
	de = int(end_time[2])	#end day
	hs = int(start_time[3])	#start hour
	he = int(end_time[3])	#end hour
	ns = int(start_time[4])	#start minute
	ne = int(end_time[4])	#end minute
	ss = int(start_time[5])	#start second
	se = int(end_time[5])	#end second

	





	dd_per_mm = [31,28,31,30,31,30,31,31,30,31,30,31]
	dd_per_mm_ly = [31,29,31,30,31,30,31,31,30,31,30,31]
	
	#ADDING TIME UNTIL END DATE IS REACHED

	#MATCHING THE SECONDS
	s_counter = 0
	while ss != se: #matching the seconds
		ss += 1
		s_counter += 1
		if ss == 60:
			ss = 0
			ns += 1
			if ns == 60:
				ns = 0
				hs += 1 
				if hs == 24:
					hs = 0
					ds += 1
					if ys % 4 == 0:
						if ds == dd_per_mm_ly[int(ms-1)] + 1:
							ds = 1
							ms += 1
							if ms == 13:
								ms = 1
								ys += 1
					else:
						if ds == dd_per_mm[int(ms-1)] + 1:
							ds = 1
							ms += 1
							if ms == 13:
								ms = 1
								ys += 1
		

	#MATCHING THE MINUTES
	n_counter = 0
	while ns != ne:
		ns += 1
		n_counter += 1
		if ns == 60:
			ns = 0
			hs += 1 
			if hs == 24:
				hs = 0
				ds += 1
				if ys % 4 == 0:
					if ds == dd_per_mm_ly[int(ms-1)] + 1:
						ds = 1
						ms += 1
						if ms == 13:
							ms = 1
							ys += 1
				else:
					if ds == dd_per_mm[int(ms-1)] + 1:
						ds = 1
						ms += 1
						if ms == 13:
							ms = 1
							ys += 1

	#MATCHING THE HOURS
	h_counter = 0
	while hs != he:
		hs += 1
		h_counter += 1
		if hs == 24:
			hs = 0
			ds += 1
			if ys % 4 == 0:
				if ds == dd_per_mm_ly[int(ms-1)] + 1:
					ds = 1
					ms += 1
					if ms == 13:
						ms = 1
						ys += 1
			else:
				if ds == dd_per_mm[int(ms-1)] + 1:
					ds = 1
					ms += 1
					if ms == 13:
						ms = 1
						ys += 1

	#MATCHING THE DAYS, MONTHS, AND YEARS (CAN'T ADD MORE THAN DAYS DUE TO LEAP YEARS)
	d_counter = 0 
	while not (ds == de and ms == me and ys == ye):  
		ds += 1
		d_counter += 1
		if ys % 4 == 0:
			if ds == dd_per_mm_ly[int(ms-1)] + 1:
				ds = 1
				ms += 1
				if ms == 13:
					ms = 1
					ys += 1
		else:
			if ds == dd_per_mm[int(ms-1)] + 1:
				ds = 1
				ms += 1
				if ms == 13:
					ms = 1
					ys += 1


	#ADDING THE COUNTED TIMES TOGETHER
	total_time = float(s_counter)/60 + float(n_counter) + float(h_counter) * 60 + float(d_counter) * 1440

	return total_time * neg_time
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
def J_date(date):
	"""
	Calculates the julian date from the given gregorian date
	"""
	jd_ref = [2000,1,1,12,00,00]
	jd_2000 = 2451545.0
	minutes = minutes_elapsed(jd_ref,date) 
	JD = float(minutes/1440.0) + jd_2000
	return JD
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
def helio(dates_list,planets):

	"""
	GIVES THE RADIUS, LONGITUDE, AND LATITUDE OF THE PLANETS LISTED ON THE DATES LISTED.
	IMPORTS necessary :
		from sys import argv
		from numpy import array, shape, zeros, pi, sqrt, sin, cos, tan, arctan
		from math import asin  
		from MSE_Angle import minutes_elapsed, J_date

	INPUTS:
		1st input --> dates_list  --> [ [date_1] , [date_2] , ... ]
		2nd input -->   planets   --> [ planet1_# , planet2_# , ... ]
	"""
	JD = []
	for date in dates_list:
		JD.append(J_date(date))

	# DEFINING ORBITAL PERAMETERS AND FIXED VALUES 
	
	#ORBITAL PERAMETERS:
	#					  (1)semi-major axis in AU, 
	#					  (2)eccentricity, 
	# 					  (3)inclination (degrees), 
	#					  (4)longitude of the ascending node (degrees), 
	#					  (5)longitude of perihelion (degrees), 
	#					  (6)mean longitude (degrees) )
	PD = array(
		[[ 0.38709893, 0.20563069, 7.00487,  48.33167,  77.45645, 252.25084 ], 	# Mercury
	    [ 0.72333199, 0.00677323, 3.39471,  76.68069, 131.53298, 181.97973 ],  # Venus	
	    [ 1.00000011, 0.01671022, 0.00005, -11.26064, 102.94719, 100.46435], 	# Earth	
	    [ 1.52366231, 0.09341233, 1.85061,  49.57854, 336.04084, 355.45332], 	# Mars
	    [ 5.20336301, 0.04839266, 1.30530, 100.55615,  14.75385,  34.40438],  	# Jupiter		
	    [ 9.53707032, 0.05415060, 2.48446, 113.71504,  92.43194,  49.94432], 	# Saturn			   
	    [19.19126393, 0.04716771, 0.76986,  74.22988, 170.96424, 313.23218],  	# Uranus	
	    [30.06896348, 0.00858587, 1.76917, 131.72169,  44.97135, 304.88003], 	# Neptune	 
	    [39.48168677, 0.24880766,17.14175, 110.30347, 224.06676, 238.92881]])	# Pluto	
	
	
	#DPD gives the time rate of change of the above quantities ("/century)
	DPD = array( 
		[[0.00000066, 0.00002527, -23.51, -446.30, 573.57, 538101628.29 ],
	 	[ 0.00000092, -0.00004938, -2.86, -996.89, -108.80, 210664136.06],
	 	[-0.00000005, -0.00003804, -46.94, -18228.25, 1198.28, 129597740.63],
	 	[-0.00007221, 0.00011902, -25.47, -1020.19, 1560.78, 68905103.78 ],
	 	[0.00060737, -0.00012880, -4.15, 1217.17, 839.93, 10925078.35 ],
	 	[-0.00301530, -0.00036762, 6.11, -1591.05, -1948.89, 4401052.95],
	 	[0.00152025, -0.00019150, -2.09, -1681.40, 1312.56, 1542547.79 ],
	 	[-0.00125196, 0.0000251, -3.64, -151.25, -844.43, 786449.21 ],
	 	[-0.00076912, 0.00006465, 11.07, -37.33, -132.25, 522747.90]])
	
	JD0 = 2451545.0    #Julian Date for Epoch 2000.0
	radeg = 180.0/pi   #RADIANS TO DEGREES CONVERSION
	circnst = 2.0 * pi


	#CALCULATING THE NUMBER OF DAYS SINCE THE EPOCH
	t = [( i - JD0 ) / 36525.0 for i in JD]  #TIME SINCE J2000 EPOCH IN CENTURIES
	ip = [i - 1 for i in planets]
	
	#Converting arc seconds in DPD to degrees
	for i in ip:
		for j in range(2,6):
			DPD[i][j] = DPD[i][j]/3600.0 
	
	ntime = len(t)
	nplanet = len(planets)
	
	
	hrad = zeros((nplanet,ntime))
	hlon = zeros((nplanet,ntime))
	hlat = zeros((nplanet,ntime))
		

	#LOOPING OVER ALL OF THE DATES
	
	for i in range(ntime):
	
		PD1 = array( [[PD[j][k] + DPD[j][k]*t[i] for k in range(6)] for j in ip] )  #ADJUSTING ORBITAL PERAMETERS BASED ON DATE 
		
		a = array( [ (PD1[j][0]) for j in range(nplanet) ]) 							#semi-major axis
		eccen = array([ (PD1[j][1])for j in range(nplanet)])			#eccentricity	
		inc = array([ (PD1[j][2])/radeg for j in range(nplanet)])			#inclination in radians
		omega = array([ (PD1[j][3])/radeg for j in range(nplanet)])			#longitude of the ascending node
		ph = array([ (PD1[j][4])/radeg for j in range(nplanet)])				#longitude of the perihelion
		L = array([ (PD1[j][5])/radeg for j in range(nplanet)])				#mean longitude
		n = array([0.9856076686/a[j]/sqrt(a[j])/radeg for j in range(nplanet)])	#mean motion, in radians/day
	
		m = L - ph
		m = m % circnst
	
		for j in range(nplanet):
			if m[j] < 0:
				m[j] += 2.0*pi   
	
		e1 = m + (m + eccen*sin(m) - m) / (1.0 - eccen*cos(m))
		e = e1 + (m + eccen*sin(e1) - e1) / (1.0 - eccen*cos(e1))
		maxdif = max(abs(e - e1))
		niter = 0
		while (maxdif > 1e-5) and (niter < 10):
			e1 = e
			e = e1 + (m + eccen*sin(e1) - e1) / (1.0 - eccen*cos(e1))
			maxdif = max(abs(e - e1))
			niter += 1
	
		nu = 2.0*arctan( sqrt((1.0 + eccen) / (1.0 - eccen)) * tan(e/2.0) )  #true anomaly
	
		for j in range(nplanet):
			hrad[j][i] = a[j]*(1.0 - eccen[j]*cos(e[j]))
			hlon[j][i] = (nu[j] + ph[j])*radeg
			hlat[j][i] =  asin( sin(hlon[j][i] - omega[j]) * sin(inc[j]) )*radeg
	
	for i in range(hlon.shape[0]):
		for j in range(hlon.shape[1]):
			if hlon[i][j] < 0:
				hlon[i][j] += 360

	return hrad,hlon,hlat
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
def MSE_angle(date):
	"""
	CALCULATES THE MARS SUN EARTH ANGLE FOR A GIVEN DATE
	"""
	hrad, hlon, hlat = helio([date],[3,4])

	angle = hlon[1] - hlon[0]
	if abs(angle) > 180:
		angle = 360 - abs(angle)

	return abs(angle[0])
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
#NOAA_events_reader
def NOAA_events_reader(file_path):
	"""
	for a given file path returns the important information from the file in the following format:
		[ [1st_flare_evnet] , [2nd_flare_event] , ... ] where 
		[1st_flare_evnet] is [begin_time , peak_time , end_time , location , peak_val(W/m^2)]


		note: file path must have '/' even if it is in the current working directory

		IMPORTS:

	"""
	#defining the data to output
	data = []

	#reading info from the file path
	path_list = file_path.split('/')
	yyyymmdd = path_list[-1][0:8]


	#defining first data line in file based on file date (formatt changes different before 19980509)
	start_line = 13
	if float(yyyymmdd) < 19980509.0:
		start_line = 7

	event_file = open(file_path,'r')
	lines = event_file.readlines()

	#removing the blank lines
	del_count = 0
	for i in range(start_line,len(lines)):
		if lines[i - del_count] == '\n':
			del lines[i - del_count]
			del_count += 1
	#remove new line '\n' from data lines
	for i in range(start_line,len(lines)):
		lines[i] = lines[i].strip()
	#remove non data lines
	for i in range(0,start_line):
		del lines[0]


	#finding the range of indicies for the lines in "lines(LIST)" that have the same event number
	event_indicies = [(0,0)]
	for i in range(len(lines)):
		if lines[i].split()[0] == lines[event_indicies[-1][0]].split()[0]:
			event_indicies.append((event_indicies[-1][0],i))
			del event_indicies[-2]
		else:
			event_indicies.append((i,i))


	#FOR EACH EVENT		
	for indicies in event_indicies:
		#FOR EACH LINE IN EACH EVENT
		FL_XR_XF = [[],[],[]]

		for i in range(indicies[0],indicies[1]+1):
			

			#CHECK IF 'FLA' 'XRA' OR 'XFL' ARE POSTED IN EACH EVENT

			if 'FLA' in lines[i]:
				FL_XR_XF[0].append(lines[i])

			elif 'XRA' in lines[i]:	
				FL_XR_XF[1].append(lines[i])

			elif 'XFL' in lines[i]:	
				FL_XR_XF[2].append(lines[i])


		#for each element in FL_XR_XF


		new_event = []
		b_time = 'na'
		m_time = 'na'
		e_time = 'na'
		loc = 'na'
		peak_val = 'na'



	
		#OBTAINING b_time, m_time, and e_time FROM FL_XR_XF.
		if len(FL_XR_XF[0]) != 0:
			#Formatting the info from the line
			info = FL_XR_XF[0][0].split(' ')
			del_count = 0
			for i in range(len(info)):
				if info[i - del_count] == '' or info[i - del_count] == ' ' or info[i - del_count] == '+':
					del info[i - del_count]
					del_count += 1

			#defining the time variables
			b_time , m_time , e_time =  str(info[1]) , str(info[2]) , str(info[3])     


		elif len(FL_XR_XF[1]) != 0:
			#Formatting the info from the line
			info = FL_XR_XF[1][0].split(' ')
			del_count = 0
			for i in range(len(info)):
				if info[i - del_count] == '' or info[i - del_count] == ' ' or info[i - del_count] == '+':
					del info[i - del_count]
					del_count += 1
			#defining the time variables
			b_time , m_time , e_time =  str(info[1]) , str(info[2]) , str(info[3])


		elif len(FL_XR_XF[2]) != 0:
			#Formatting the info from the line
			info = FL_XR_XF[2][0].split(' ')
			del_count = 0
			for i in range(len(info)):
				if info[i - del_count] == '' or info[i - del_count] == ' ' or info[i - del_count] == '+':
					del info[i - del_count]
					del_count += 1
			#defining the time variables
			b_time , m_time , e_time =  str(info[1]) , str(info[2]) , str(info[3])



		#OBTAINING THE LOCATION FROM FL_XR_XF
		if len(FL_XR_XF[0]) != 0:
			#Formatting the info from the line
			info = FL_XR_XF[0][0].split(' ')
			del_count = 0
			for i in range(len(info)):
				if info[i - del_count] == '' or info[i - del_count] == ' ' or info[i - del_count] == '+':
					del info[i - del_count]
					del_count += 1

			#extracting the location
			loc = str(info[7])
		else:
			loc = 'N.A.'


		#OBTAINING THE PEAK VALUE FROM FL_XR_XF
		if len(FL_XR_XF[1]) != 0:
			#Formatting the info from the line
			info = FL_XR_XF[1][0].split(' ')
			del_count = 0
			for i in range(len(info)):
				if info[i - del_count] == '' or info[i - del_count] == ' ' or info[i - del_count] == '+':
					del info[i - del_count]
					del_count += 1

			for string in info:
				if 'E-0' in string or 'E0' in string:
					peak_val = str(float(string) * 1e-3)




				
		new_event.append(b_time)		
		new_event.append(m_time)
		new_event.append(e_time)
		new_event.append(loc)
		new_event.append(peak_val)	

		if not all(i == 'na' or i == 'N.A.' for i in new_event[0:5]):
			data.append(new_event)

	
	event_file.close()

	return data

#---------------------------------------------------------------------------------------------------















