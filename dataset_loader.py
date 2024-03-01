import numpy as np

def loadscan(sensors,scan, noisy):
        
        points=[]
        path=str(scan)
        for i in range (0,sensors):
                data11= np.loadtxt("./BLENSOR/sensor_"+path+"_"+str(i)+".csv", delimiter=",",skiprows=1)

                if(noisy==1):
                        data1=[]
                        data1.append(data11[:,8])
                        data1.append(data11[:,9])
                        data1.append(data11[:,10])

                else:
                        data1=[]
                        data1.append(data11[:,5])
                        data1.append(data11[:,6])
                        data1.append(data11[:,7])

                points1 = np.vstack(data1).T
                points.append(points1)


        return points
