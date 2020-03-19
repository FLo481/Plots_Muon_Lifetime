import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import scipy.optimize

def fit_func1(x, a, b):
    
    return a*x+b

def fit_func2(x, a, b, c):

    return a*np.exp(-b*x)+c

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

    #for l in range(m):
    #    print("Counts at", energy[l], "keV", ":", counts[l])
    
    return energy, counts

def eval_calibration_file():

    dirName = r'C:\Users\Flo\Desktop\LabCourse\Muon Lifetime\calibration'
    m = numberof_nonzero_bins(dirName)
    time_temp = [1,2,3,4,5,5,6,6,7,8]
    energy_err_temp = []
    energy_err = np.empty(m, int)
    time = np.empty(m, int)
    k = 1
    energy, counts = readin_values(dirName)

    #xerr of +/- 1keV
    for l in range(m):
        energy_err_temp.append(1)
    
    time[:] = time_temp
    energy_err[:] = energy_err_temp
    del time_temp
    del energy_err_temp

    #plt.errorbar(energy, time, yerr = None, xerr = energy_err , fmt='x', label="Calibration data", markersize=11)
    params, params_cov = scipy.optimize.curve_fit(fit_func1, energy, time, sigma = None, absolute_sigma = True)
    #plt.plot(energy, fit_func1(energy, params[0], params[1]), label= r"constant fit $y=ax+b$")
    #plt.grid()
    #plt.xlabel("Energy [keV]", fontsize=16)
    #plt.ylabel("Time $[\mu s]$", fontsize=16)
    #plt.legend()

    perr = np.sqrt(np.diag(params_cov))/np.sqrt(len(time))
    val_time = 1/params[0]
    val_time_err =  perr[0]/params[0]

    #print("1 µs =", val_time, "+/-", perr[0]/params[0], "keV")

    #plt.show()
    #plt.clf()

    return val_time, val_time_err

def eval_real_data():

    dirName = r'C:\Users\Flo\Desktop\LabCourse\Muon Lifetime\data Flo and Konny'
    energy, counts = readin_values(dirName)
    val_time, val_time_err = eval_calibration_file()
    m = numberof_nonzero_bins(dirName)
    fit = np.empty(m, float)

    plt.errorbar(energy/val_time, counts, yerr = np.sqrt(counts), xerr = np.sqrt((1/energy)**2+(val_time_err/val_time)**2)*energy/val_time, fmt='x', label="Detected Muon Decays", markersize=5, zorder = -1)
    params, params_cov = scipy.optimize.curve_fit(fit_func2, energy/val_time, counts, sigma = np.sqrt(counts), absolute_sigma = True)
    plt.plot(energy/val_time, fit_func2(energy/val_time, params[0], params[1], params[2]), label= r"Exponential fit $y=ae^{-bt}+c$")
    plt.grid()
    plt.xlabel("Time [$\mu s$]", fontsize=16)
    plt.ylabel("Counts", fontsize=16)
    #plt.legend()

    perr = np.sqrt(np.diag(params_cov))/np.sqrt(len(energy))
    print("Lifetime of Muon =", 1/params[1]*1000, "+/-", perr[1]/params[1]*1000, "ns")

    #calculating Chi^2
    chi_squared_value = 0
    fit[:] = fit_func2(energy/val_time, params[0], params[1], params[2])

    for l in range(m):
        chi_squared_value += (counts[l] - fit[l])**2/(np.sqrt(counts[l]))**2 

    print("red Chi^2 =", chi_squared_value/(m-3))
    print("a =", params[0], "+/-", perr[0])
    print("b =", params[1]*1000, "+/-", perr[1]*1000, "ms")
    print("c =", params[2], "+/-", perr[2])

    plt.show()
    plt.clf()

def main():
    #dirName = r'C:\Users\Flo\Desktop\LabCourse\Muon Lifetime\calibration'
    #readin_values(dirName)
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