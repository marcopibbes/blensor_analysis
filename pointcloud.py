
import open3d as o3d

def generateGraphics(points1,points2,points3,filtered):

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
  
  if(filtered==1):
    filtered_pcd = combined_pcd.select_by_index([i for i in range(len(combined_pcd.points)) if combined_pcd.points[i][2] > -1.2])
    return filtered_pcd
  
  else:
    return combined_pcd
  

def visualizeGraphics(pcds):
  for pcd in pcds:
    o3d.visualization.draw_geometries([pcd])
    
  