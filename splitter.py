#FileSplitter splits large CSV files into smaller pieces of a given row length.
#The first row in the parent file is assumed to be a header, and will be included in each child automatically.
#Written by Collin Bomalick
#github.com/cbomalick

import csv
import os 

#Input file
master = "master.csv"

#Maximum length
max_length = 999

#Counters
file_number = 1
row_count = 0
total_rows = 0
total_files = 0

#Pull current file path
folder = os.path.dirname(os.path.realpath(__file__)) + "/"

#Root name of output files
filename = "part"+str(file_number)
newfile = folder + filename +".csv"

#Open and read the master file
with open(folder + master) as master_file:
    csv_reader = csv.reader(master_file, delimiter=",")

    #Create and open the new file
    f = open(newfile, "a")
    total_files += 1
    
    #Separate the headers from the data
    headers = next(csv_reader)

    #Write the headers into the first file
    f.write(",".join(headers))
    f.write("\n")
    row_count += 1
    
    for row in csv_reader:
        #Write the data into the file
        f.write(",".join(row) + "\n")
        row_count += 1
        total_rows += 1
        
        #When row count hits the maximum, start a new file
        if row_count == max_length:
            #Close the previous file, reset the counter and increment the file name by 1
            f.close()
            row_count = 0
            file_number += 1

            #Set the new file name
            filename = "part"+str(file_number)
            newfile = folder + filename +".csv"

            #Create and open the new file
            f = open(newfile, "a")
            f.write(",".join(headers) + "\n")
            row_count += 1
            total_files += 1
    
    #Print results when finished
    print("Operation complete. " + str(total_rows) + " rows were split into " + str(total_files) + " files.")
