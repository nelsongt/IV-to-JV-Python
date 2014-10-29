import os
import csv


def csv_extract_col(csvinput, colname, key):
    """ extract a named column from a csv stream into a dictionary
          colname:  name of columm to extract
          key:  name of another columm to use as keys in returned dict
    """
    col = {}
    for row in csv.DictReader(csvinput):
        col[row[key]] = row[colname]
    return col


print "Enter the location of the files: "; directory = raw_input()

path = r"%s" % directory

for file in os.listdir(path):
    current_file = os.path.join(path, file)

    f = open(current_file, "r")
    data = [item for item in csv.reader(f)]
    f.close()
     
    new_column = ["Col 1", "Line 1", "Line 2"]
     
    new_data = []
     
    for i, item in enumerate(data):
	try:
	    item.append(new_column[i])
	except IndexError, e:
	    item.append("placeholder")
	new_data.append(item)
     
    f = open('csv2B.csv', 'w')
    csv.writer(f).writerows(new_data)
    f.close()

