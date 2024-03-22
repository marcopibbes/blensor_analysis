import numpy as np
import open3d as o3d
import random
import matplotlib.pyplot as plt
import csv
import data_writer


def plot_trajectories(bounding_boxes):

    x_coords=[]
    y_coords=[]
  
    for bbox in bounding_boxes:
        x_coords.append(np.asarray(bbox.get_center())[0])
        y_coords.append(np.asarray(bbox.get_center())[1])


    plt.plot(x_coords, y_coords, marker='o', linestyle='')  
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Detected Trajectories")
    plt.show()

            
        
def track(bounding_boxes):


    for list in bounding_boxes:
        for bbox in list:
            bbox.color=[round(random.random(),1),round(random.random(),1),round(random.random(),1)]
        

    matched_bounding_boxes=[]
    map={}
    

    for i in range(len(bounding_boxes)-1) : 

        
        
        for j in range (len(bounding_boxes[i])):
            
            
            
            corners1 = bounding_boxes[i][j].get_box_points()

            if(i==0):
             map[bounding_boxes[i][j].color[0]+bounding_boxes[i][j].color[2]+bounding_boxes[i][j].color[1]]=random.randint(0,5000)
             data_writer.write_bbox_csv(i+20,map[bounding_boxes[i][j].color[0]+bounding_boxes[i][j].color[2]+bounding_boxes[i][j].color[1]],np.asarray(corners1)[0,0],np.asarray(corners1)[0,1],np.asarray(corners1)[0,2],np.asarray(corners1)[1,0],np.asarray(corners1)[1,1],np.asarray(corners1)[1,2],np.asarray(corners1)[2,0],np.asarray(corners1)[2,1],np.asarray(corners1)[2,2],np.asarray(corners1)[3,0],np.asarray(corners1)[3,1],np.asarray(corners1)[3,2],np.asarray(corners1)[4,0],np.asarray(corners1)[4,1],np.asarray(corners1)[4,2],np.asarray(corners1)[5,0],np.asarray(corners1)[5,1],np.asarray(corners1)[5,2],np.asarray(corners1)[6,0],np.asarray(corners1)[6,1],np.asarray(corners1)[6,2],np.asarray(corners1)[7,0],np.asarray(corners1)[7,1],np.asarray(corners1)[7,2])

        
            for bbox in bounding_boxes[i+1]:
                
                corners2 = bbox.get_box_points()

                print("Corner1: " , np.asarray(corners1)[:,0])
                print("Corner2: " , np.asarray(corners2)[:,0])

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
                        bbox.color=bounding_boxes[i][j].color
                        matched_bounding_boxes.append(bbox)
                        data_writer.write_bbox_csv(i+21,map[bbox.color[0]+bbox.color[2]+bbox.color[1]],np.asarray(corners2)[0,0],np.asarray(corners2)[0,1],np.asarray(corners2)[0,2],np.asarray(corners2)[1,0],np.asarray(corners2)[1,1],np.asarray(corners2)[1,2],np.asarray(corners2)[2,0],np.asarray(corners2)[2,1],np.asarray(corners2)[2,2],np.asarray(corners2)[3,0],np.asarray(corners2)[3,1],np.asarray(corners2)[3,2],np.asarray(corners2)[4,0],np.asarray(corners2)[4,1],np.asarray(corners2)[4,2],np.asarray(corners2)[5,0],np.asarray(corners2)[5,1],np.asarray(corners2)[5,2],np.asarray(corners2)[6,0],np.asarray(corners2)[6,1],np.asarray(corners2)[6,2],np.asarray(corners2)[7,0],np.asarray(corners2)[7,1],np.asarray(corners2)[7,2])

    total_bounding_boxes=[]
    for row in bounding_boxes:
        for bbox in row:
            total_bounding_boxes.append(bbox)

        
    o3d.visualization.draw([*total_bounding_boxes],show_skybox=False)
    return total_bounding_boxes

