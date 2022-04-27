import numpy as np
from math import sin, cos, pi
 
def rotate_x(theta):
    return np.matrix([[1, 0, 0],
                    [0, cos(theta),-sin(theta)],
                    [0, sin(theta), cos(theta)]])
 
def rotate_y(theta):
    return np.matrix([[cos(theta), 0, sin(theta)],
                    [0, 1, 0],
                    [-sin(theta), 0, cos(theta)]])
 
def rotate_z(theta):
    return np.matrix([[cos(theta), -sin(theta), 0],  
                    [sin(theta), cos(theta) , 0],
                    [0, 0, 1]])

n = int(input())

points=n*[0]
for i in range(n):
    points[i] = list(map(float, input().split()))
    
vector = np.array(points)

x, y, z = map(float, input().split()) 


rotation_vector= rotate_x(2*pi-x) * rotate_y(2*pi-y) * rotate_z(2*pi-z)

np.set_printoptions(formatter={'int': '{:0.0f}'.format}, threshold=np.inf)
print(vector*rotation_vector)

  
