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
    energy_temp = []
    counts = np.empty(n, int)
    energy = np.empty(n, int)

    for l in range(n):
        energy_temp.append(l)

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

    counts[:] = data_temp
    energy[:] = energy_temp

    #for l in range(n):
    #    print("Counts at", l, "keV :", data[l])
    #    if counts[l] != 0:
    #        print("Counts at", l, "keV", ":", data[l])

    return energy, counts

def plot_calibration_file():
    dirName = r'C:\Users\Flo\Desktop\LabCourse\Muon Lifetime\data Flo and Konny'
    
    n = numberof_datapoints(dirName)

    counts = np.empty(n, int)
    energy = np.empty(n, int)

    energy, counts = readin_values()

    #for l in range(n):
    #    print(energy[l], "keV", counts[l])

    plt.errorbar(energy, counts, fmt='x', label="Calibration counts", markersize=11)
    plt.grid()
    plt.xlabel("Energy [keV]", fontsize=16)
    plt.ylabel("Counts", fontsize=16)
    plt.legend()

    plt.show()
    plt.clf()  


    return 0


def main():
    #readin_values()
    plot_calibration_file()

if __name__ == '__main__':
    main()