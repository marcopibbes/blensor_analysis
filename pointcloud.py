import numpy as np
import matplotlib as plt
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
    filtered_downsampled_pcd=filtered_pcd.voxel_down_sample(voxel_size=0.25)
    return filtered_downsampled_pcd
  
  else:
    combined_downsampled_pcd=combined_pcd.voxel_down_sample(voxel_size=0.25)
    return combined_downsampled_pcd
  

def clusterData(pcds):
  for pcd in pcds:

    labels = np.array(pcd.cluster_dbscan(eps=2, min_points=5, print_progress=True))

    clusters = []
    for label in np.unique(labels):
        cluster_mask = (labels == label)
        clusters.append(pcd.select_by_index(np.where(cluster_mask)[0]))

    bounding_boxes = []
    for cluster in clusters:
        aabb = cluster.get_axis_aligned_bounding_box()
        aabb.color = [1,0,0]
        bounding_boxes.append(aabb)

    colors = plt.cm.tab10(labels / (labels.max() if labels.max() > 0 else 1))
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

    o3d.visualization.draw([pcd, *bounding_boxes],show_skybox=False)


def visualizeGraphics(pcds):
  for pcd in pcds:
    o3d.visualization.draw([pcd],show_skybox=False)
    
  