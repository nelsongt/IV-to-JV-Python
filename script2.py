import os
import csv
import math

print "Enter the (relative) location of the files: "; directory = raw_input()

print "Enter the radius of the diode (um): "; radius_um = raw_input()
radius_cm = float(radius_um) * 0.0001
area = radius_cm * radius_cm * math.pi

path = r"%s" % directory

pathout = os.path.join(path, "jv")
if not os.path.exists(pathout):
  os.makedirs(pathout)

for file in os.listdir(path):
    current_file = os.path.join(path, file)
    print "Current file: %s" % file
    
    f = open(current_file, "r")
    data = [item for item in list(csv.reader(f))]
    f.close()
    
    
    new_data = [["Voltage (V)","Current Density (A/cm^2)"]]
     
    for i, item in enumerate(data):
	if data[i][0] == "MetaData":
	  if data[i][1] == " TestRecord.TestTarget":
	    device = data[i][2].replace(" ","")
	  elif data[i][1] == " TestRecord.Remarks":
	    diode = data[i][2]
	elif data[i][0] == "Dimension1":
	  dimension = int(data[i][1].replace(" ",""))
	  print "Data set found! Number of data points: %d" % dimension
	  for x in xrange(i+3,i+3+dimension):
	      new_data.append([data[x][1].replace(" ",""), float(data[x][2].replace(" ","")) / area])
	  break
	
    output_file = os.path.join(pathout, "%s%s.csv" %(device, diode))
    f = open(output_file, 'w')
    csv.writer(f).writerows(new_data)
    f.close()

    print "File completed"