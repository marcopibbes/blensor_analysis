import numpy as np

def loadscan(scan, noisy):
        
        path=str(scan)
        data11= np.loadtxt("./BLENSOR/sensor_"+path+"_0.csv", delimiter=",",skiprows=1)
        data21= np.loadtxt("./BLENSOR/sensor_"+path+"_1.csv", delimiter=",",skiprows=1)
        data31= np.loadtxt("./BLENSOR/sensor_"+path+"_2.csv", delimiter=",",skiprows=1)

        if(noisy==1):
                data1=[]
                data1.append(data11[:,8])
                data1.append(data11[:,9])
                data1.append(data11[:,10])

                data2=[] 
                data2.append(data21[:,8])
                data2.append(data21[:,9])
                data2.append(data21[:,10])

                data3=[]
                data3.append(data31[:,8])
                data3.append(data31[:,9])
                data3.append(data31[:,10])

        else:
                data1=[]
                data1.append(data11[:,5])
                data1.append(data11[:,6])
                data1.append(data11[:,7])

                data2=[] 
                data2.append(data21[:,5])
                data2.append(data21[:,6])
                data2.append(data21[:,7])

                data3=[]
                data3.append(data31[:,5])
                data3.append(data31[:,6])
                data3.append(data31[:,7])

        points1 = np.vstack(data1).T
        points2 = np.vstack(data2).T
        points3= np.vstack(data3).T
        
        return points1, points2, points3
