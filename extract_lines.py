#!/usr/bin/env python 

import csv
import os


sensornumber = "10"
sensorfile = 'Data_150621/2015-06-20_SensorData.csv'
resultfile = '2015-06-20_SensorData_filtered.csv'


script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
#abs_file_path = os.path.join(script_dir, rel_path)

#print(os.path.join(script_dir, sensorfile))
#print(os.path.join(script_dir, resultfile))



#outfile = open(os.path.join(script_dir, resultfile),'w+')
with open(os.path.join(script_dir, resultfile),'w+') as csvoutfile:
  linewriter = csv.writer(csvoutfile, delimiter=";")
  with open(os.path.join(script_dir, sensorfile), 'rb') as csvfile:
    linereader = csv.reader(csvfile, delimiter=';')
    for row in linereader:
      if row[0] == sensornumber:
	linewriter.writerow(row)
      
#outfile.close
