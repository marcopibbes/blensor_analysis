import dataset_loader
import pointcloud


scans= input("Insert qty of scans: ")
scans=int(scans)
sensors= input("Insert qty of sensors: ")
sensors=(int)(sensors)
noisy= input("Noisy scan? (1/0): ")
filtered= input ("Filtered scan? (1/0): ")

pcds=[]
for i in range (0,scans):
    pointclouds= dataset_loader.loadscan(sensors,i,int(noisy))
    pcds.append(pointcloud.generateGraphics(pointclouds,int(filtered)))

pointcloud.visualizeGraphics(pcds)
#22pointcloud.clusterData(pcds)

'''
Multitarget tracking (es. sort)
Intersection over union

'''
