import numpy as np
import matplotlib.pyplot as plt
import os
import csv

def numberof_datapoints(dirName):
    n = 0
    i = 0
    pattern = '$DATA:'

    for root, directory, files in os.walk(dirName):
         for file in files:
             if '.txt' in file:
                 files.append(os.path.join(root, file))
     

    for file in files:
        with open(dirName + "\\" + file) as myfile:
            reader = csv.reader(myfile, delimiter = '\n')
            for myline in myfile:   
                if i == 11:
                    n = int(myline[2]+myline[3]+myline[4]+myline[5])
                    break
                else:
                    i +=1

    return n+1

def readin_values():
    dirName = r'C:\Users\Flo\Desktop\LabCourse\Muon Lifetime\data Flo and Konny'
    
    n = numberof_datapoints(dirName)
    i = 0
    j = 0
    data_temp = []
    data = np.empty(n, int)

    for root, directory, files in os.walk(dirName):
         for file in files:
             if '.txt' in file:
                 files.append(os.path.join(root, file))
     

    for file in files:
        with open(dirName + "\\" + file) as f:
            reader = csv.reader(f, delimiter = '\n')
            for row in reader:
                if i > 11 and i < 2060:
                    data_temp.append(row[0])
                #else:
                #    j += 1
                i += 1
            #print("Number of lines read in :", i-j)

    f.close()

    data[:] = data_temp

    for l in range(len(data)):
        #print("Counts at", l, "keV :", data[l])
        if data[l] != 0:
            print("Counts at", l, "keV", ":", data[l])
    return data

def main():
    readin_values()

if __name__ == '__main__':
    main()