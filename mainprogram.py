import dataset_loader
import pointcloud

scans= input("Insert qty of scans: ")
scans=int(scans)
noisy= input("Noisy scan? (1/0): ")
filtered= input ("Filtered scan? (1/0): ")

pcds=[]
for i in range (0,scans):
    points1,points2,points3 = dataset_loader.loadscan(i,int(noisy))
    pcds.append(pointcloud.generateGraphics(points1,points2,points3,int(filtered)))

pointcloud.visualizeGraphics(pcds)





