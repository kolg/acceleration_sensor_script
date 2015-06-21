#!/usr/bin/env python 

#calculate the RMS-Value of the acceleration (gravity filtered) 
#RMS: https://en.wikipedia.org/wiki/Root_mean_square
#from the *.csv-file produced by the Sensor Recording App by Michael Braun 

#License: this script can be used, modified and distributed for anthing which 
#is related to Openstreetmap and any non-commercial projects. (jlcod)

import csv
import os
from datetime import datetime, date, time, timedelta

sensornumber = "10" #in this case, Sensor 10 delivers the acceleration values without gravity
sensorfile = 'Data_150621/2015-06-20_SensorData.csv'
resultfile = '2015-06-20_SensorData_rms.csv'

integrationtime_sec = 10 # Integration time for the RMS calculation

# get the absoulte paths for the given relative file paths
script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/

#initialize the buffers
starttimestr='0'
rmsbuf=0.0
rmscnt=0


with open(os.path.join(script_dir, resultfile),'w+') as csvoutfile: #open result file for writing
  linewriter = csv.writer(csvoutfile, delimiter=";")
  with open(os.path.join(script_dir, sensorfile), 'rb') as csvfile: #open input file for reading
    linereader = csv.reader(csvfile, delimiter=';')
    for row in linereader:
      if row[0] == sensornumber:	#if there is a value of sensor 10
	if starttimestr == '0':		#(this is only executed once to determine the initial start time)
	  starttimestr = row[1]
	  starttime=datetime.strptime(starttimestr, "%H:%M:%S.%f")
	if datetime.strptime(row[1], "%H:%M:%S.%f") >= starttime + timedelta(seconds=integrationtime_sec):
	  #if the given integration time is over
	  if rmsbuf !=0:
	    #...and values had been recorded in this time, 
	    # write a new line to the output file with the time and the calculated RMS-value
	    # (square root of the sum of squared values normalized by the number of values)
	    linewriter.writerow( [(starttime + timedelta(seconds=integrationtime_sec)).strftime("%H:%M:%S.%f"), str((rmsbuf/rmscnt)**0.5)])
	  else: 
	    #give a NaN if there had been no values in the integration period
	    linewriter.writerow( [(starttime + timedelta(seconds=integrationtime_sec)).strftime("%H:%M:%S.%f"), 'NaN'])
	  #now start over again and empty the calculation buffers
	  rmsbuf=0
	  rmscnt=0
	  #and calculate the new starttime for the integration period
	  starttime = starttime + timedelta(seconds=integrationtime_sec)
	  
	#for every sensor value, put the sqared value of the acceleration into the sum
	rmsbuf += float(row[6])*float(row[6])
	#and increment the counter to to remember how many values are taken
	rmscnt +=1
	
