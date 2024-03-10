import numpy as np
import open3d as o3d
import random
import copy

def track(bounding_boxes):

    for bbox in bounding_boxes:
        bbox.color=[round(random.random(),1),round(random.random(),1),round(random.random(),1)]

    matched_bounding_boxes=[]

    for i in range (0, len(bounding_boxes)): 

        corners1 = bounding_boxes[i].get_box_points()
        
      
        for bbox in bounding_boxes:
            
            corners2 = bbox.get_box_points()

            print("Corner1: " , np.asarray(corners1)[:,0])
            print("Corner2: " , np.asarray(corners2)[:,0])

            # Calculate overlap along each axis (assuming boxes don't intersect completely)
            xmin_overlap = max(np.min(np.asarray(corners1)[:,0]), np.min(np.asarray(corners2)[:,0]))
            xmax_overlap = min(np.max(np.asarray(corners1)[:,0]), np.max(np.asarray(corners2)[:,0]))
            ymin_overlap = max(np.min(np.asarray(corners1)[:,1]), np.min(np.asarray(corners2)[:,1]))
            ymax_overlap = min(np.max(np.asarray(corners1)[:,1]), np.max(np.asarray(corners2)[:,1]))
            
            print("xmin ", xmin_overlap)
            print("xmax ", xmax_overlap)
            print("ymin ",ymin_overlap)
            print("ymax ",ymax_overlap)
            
            if(bbox not in matched_bounding_boxes):

                if (xmin_overlap >= xmax_overlap) or (ymin_overlap >= ymax_overlap) and (bbox!=bounding_boxes[i]):
                 bbox.color=[round(random.random(),1),round(random.random(),1),round(random.random(),1)]

                else:
                    bbox.color=bounding_boxes[i].color
                    matched_bounding_boxes.append(bbox)
                
        
    o3d.visualization.draw([*bounding_boxes],show_skybox=False)
            
        


