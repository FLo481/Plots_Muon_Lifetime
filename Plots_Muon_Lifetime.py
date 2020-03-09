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

    myfile.close()

    return n+1

def numberof_nonzero_bins(dirName):

    temp = []
    count = 0
    i = 0
    n = numberof_datapoints(dirName)

    for root, directory, files in os.walk(dirName):
         for file in files:
             if '.txt' in file:
                 files.append(os.path.join(root, file))
     

    for file in files:
        with open(dirName + "\\" + file) as f:
            reader = csv.reader(f, delimiter = '\n')
            for row in reader:
                if i > 11 and i < 2060:
                    temp.append(int(row[0]))
                i += 1
    
    for l in range(n):
        if not temp[l] == 0:
            count += 1

    f.close()

    return count

def readin_values(dirName):

    n = numberof_datapoints(dirName)
    m = numberof_nonzero_bins(dirName)
    i = 0
    j = 0
    data_temp = []
    data_temp_2 = []
    energy_temp = []

    for root, directory, files in os.walk(dirName):
         for file in files:
             if '.txt' in file:
                 files.append(os.path.join(root, file))
     

    for file in files:
        with open(dirName + "\\" + file) as f:
            reader = csv.reader(f, delimiter = '\n')
            for row in reader:
                if i > 11 and i < 2060:
                    data_temp.append(int(row[0]))
                #else:
                #    j += 1
                i += 1
            #print("Number of lines read in :", i-j)
    
    for l in range(n):
        if not data_temp[l] == 0:
            data_temp_2.append(data_temp[l])
            energy_temp.append(l)
            #print(l, "keV", data_temp[l])

    f.close()

    counts = np.empty(m, int)
    energy = np.empty(m, int)

    counts[:] = data_temp_2
    energy[:] = energy_temp

    del data_temp
    del data_temp_2
    del energy_temp

    #for l in range(nonzero_bincount):
    #    print("Counts at", energy[l], "keV", ":", counts[l])
    
    return energy, counts

def eval_calibration_file():

    dirName = r'C:\Users\Flo\Desktop\LabCourse\Muon Lifetime\calibration'
    n = numberof_nonzero_bins(dirName)
    energy, counts = readin_values(dirName)

    for l in range(n):
        if l > 0:
            print(energy[l]-energy[l-1])

    return 0

def eval_real_data():

    dirName = r'C:\Users\Flo\Desktop\LabCourse\Muon Lifetime\data Flo and Konny'
    energy, counts = readin_values(dirName)


    plt.errorbar(energy, counts, fmt='x', label="Detected Muon Decays", markersize=5)
    plt.grid()
    plt.xlabel("Energy [keV]", fontsize=16)
    plt.ylabel("Counts", fontsize=16)
    plt.legend()

    plt.show()
    plt.clf() 



def main():
    #readin_values()
    #eval_calibration_file()
    eval_real_data()

if __name__ == '__main__':
    main()



#plt.errorbar(energy, counts, fmt='x', label="Calibration counts", markersize=11)
#plt.grid()
#plt.xlabel("Energy [keV]", fontsize=16)
#plt.ylabel("Counts", fontsize=16)
#plt.legend()

#plt.show()
#plt.clf()  