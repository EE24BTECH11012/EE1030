from ctypes import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

rel = CDLL('./func.so')
point1 = [2,3,-4]
point2 = [3,-4,-5]
point3 = [3,2,-3]
mod = rel.mod
mod.restype = c_float

filename = 'main.txt'

with open(filename,'r') as file:
    data = file.readlines()
    print(data)



x = [0,2,0,3,0,3,0,8]
y = [0,3,0,-4,0,2,0,1]
z = [0,-4,0,-5,0,-3,0,-12]
label=['A(2,3,-4)', 'B(3,-4,-5)', 'C(3,2,-3)', 'D(8,1,-12)', 'E(0,0,0)']
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, color='b', s=100)  # s is the size of the points

ax.text(x[0],y[0],z[0],label[4])
ax.text(x[1],y[1],z[1],label[0])
ax.text(x[2],y[2],z[2],label[4])
ax.text(x[3],y[3],z[3],label[1])
ax.text(x[4],y[4],z[4],label[4])
ax.text(x[5],y[5],z[5],label[2])
ax.text(x[6],y[6],z[6],label[4])
ax.text(x[7],y[7],z[7],label[3])
ax.plot(x, y, z, color='red', linestyle='-', label='D=A+B+C')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
plt.show()

