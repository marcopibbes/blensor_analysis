import csv
import open3d as o3d

def write_bbox_csv(timestamp,id,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5,x6,y6,z6,x7,y7,z7,x8,y8,z8):

    #new_data=['timestamp','id','x1','y1','z1','x2','y2','z2','x3','y3','z3','x4','y4','z4','x5','y5','z5','x6','y6','z6','x7','y7','z7','x8','y8','z8']
    new_data=[timestamp,id,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5,x6,y6,z6,x7,y7,z7,x8,y8,z8]
    
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_data)

    file.close()

