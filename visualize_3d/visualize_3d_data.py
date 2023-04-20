import numpy as np 
import pandas as pd
import os
import matplotlib.pyplot as plt
from math import cos, sin, pi, floor
import cv2

colnames=['Bool', 'Quality', 'theta', 'dist'] 
mesure = pd.read_csv('measurements.txt',names=colnames, sep='\t') 
        
def process_data(data):
    max_distance = 0

    x_point3d=[]
    y_point3d=[]
    z_point3d=[]
 
    z=0
    cpt = 1
    
    while cpt < 67553:
        z += 1
        prevAngle = 0
        currAngle = 1
        
        while (currAngle - prevAngle) > -100:
            distance = float(data["dist"][cpt])
            prevAngle = data["theta"][cpt-1]
            currAngle = data["theta"][cpt]
            
            cpt += 1
            if distance > 0:                  # ignore initially ungathered data points
                max_distance = max([min([5000, distance]), max_distance])
                radians = currAngle * pi / 180.0
                x = distance * cos(radians)
                y = distance * sin(radians)
                x_point = 160 + int(x / max_distance * 160)
                y_point = 120 + int(y / max_distance * 120)
                
                x_point3d.append(x_point)
                y_point3d.append(y_point)
                z_point3d.append(z)
            
            
            if cpt == 67553:
                break;
        
    return x_point3d,y_point3d,z_point3d


x,y,z=process_data(mesure)

#Applatit le plot pour meilleur visualisation
x.append(0)
y.append(0)
z.append(2000)

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')
ax.grid()

ax.scatter(x, y, z,c=z,s=2)

ax.set_title('3D Parametric Plot')
ax.view_init(50, 35)

# Set axes label
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

plt.show()