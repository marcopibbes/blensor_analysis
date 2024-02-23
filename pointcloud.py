import pandas as pd
import numpy as np
import BLENSOR
import open3d as o3d

# Leggi i dati dai file CSV
data11= np.loadtxt("./BLENSOR/sensor_0_0.csv", delimiter=",",skiprows=1)
data21= np.loadtxt("./BLENSOR/sensor_0_1.csv", delimiter=",",skiprows=1)
data31= np.loadtxt("./BLENSOR/sensor_0_2.csv", delimiter=",",skiprows=1)

x_points1=data11[:,8]
y_points1=data11[:,9]
z_points1=data11[:,10]

x_points2=data21[:,8]
y_points2=data21[:,9]
z_points2=data21[:,10]

x_points3=data31[:,8]
y_points3=data31[:,9]
z_points3=data31[:,10]

# Load x, y, z data1 from CSV files
data1=[]
data1.append(x_points1)
data1.append(y_points1)
data1.append(z_points1)

data2=[]
data2.append(x_points2)
data2.append(y_points2)
data2.append(z_points2)

data3=[]
data3.append(x_points3)
data3.append(y_points3)
data3.append(z_points3)



points1 = np.vstack(data1).T
points2 = np.vstack(data2).T
points3= np.vstack(data3).T


# Create Open3D point cloud object
pcd1 = o3d.geometry.PointCloud()
pcd1.points = o3d.utility.Vector3dVector(points1)

pcd2 = o3d.geometry.PointCloud()
pcd2.points = o3d.utility.Vector3dVector(points2)

pcd3 = o3d.geometry.PointCloud()
pcd3.points = o3d.utility.Vector3dVector(points3)

combined_pcd = o3d.geometry.PointCloud()

for point in pcd1.points:
  combined_pcd.points.append(point)

for point in pcd2.points:
  if point not in combined_pcd.points:  
    combined_pcd.points.append(point)

for point in pcd3.points:
  if point not in combined_pcd.points:
    combined_pcd.points.append(point)


# Visualize the combined point cloud
filtered_pcd = combined_pcd.select_by_index([i for i in range(len(combined_pcd.points)) if combined_pcd.points[i][2] > -1.2])
o3d.visualization.draw_geometries([filtered_pcd])