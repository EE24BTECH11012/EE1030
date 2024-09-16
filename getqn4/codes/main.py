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



x = [0,2,0,3,0,5,0,3,0,8]
y = [0,3,0,-4,0,-1,0,2,0,1]
z = [0,-4,0,-5,0,-9,0,-3,0,-12]
label=['A(2,3,-4)', 'B(3,-4,-5)', 'C(3,2,-3)', 'D(8,1,-12)', 'E(0,0,0)','F(5,-1,-9)']
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, color='b', s=100)  # s is the size of the points

ax.text(x[0],y[0],z[0],label[4])
ax.text(x[1],y[1],z[1],label[0])
ax.text(x[2],y[2],z[2],label[4])
ax.text(x[3],y[4],z[3],label[1])
ax.text(x[4],y[4],z[4],label[4])
ax.plot(x,y,z,color='b',linestyle='-')

x1=[5,2,5,3]
y1=[-1,3,-1,-4]
z1=[-9,-4,-9,-5]
ax.text(x1[0],y1[0],z1[0],label[5])
ax.text(x1[1],y1[1],z1[1],label[0])
ax.text(x1[2],y1[2],z1[2],label[5])
ax.text(x1[3],y1[3],z1[3],label[1])
ax.plot(x1,y1,z1,color='r',linestyle=':',label='F=A+B')

x2=[0,5,0,3,0,8]
y2=[0,-1,0,2,0,1]
z2=[0,-9,0,-3,0,-12]
ax.text(x2[0],y2[0],z2[0],label[4])
ax.text(x2[1],y2[1],z2[1],label[5])
ax.text(x2[2],y2[2],z2[2],label[4])
ax.text(x2[3],y2[3],z2[3],label[2])
ax.text(x2[4],y2[4],z2[4],label[4])
ax.text(x2[5],y2[5],z2[5],label[3])
ax.plot(x2,y2,z2,color='b',linestyle='-')

x3=[8,5,8,3]
y3=[1,-1,1,2]
z3=[-12,-9,-12,-3]

ax.text(x3[0],y3[0],z3[0],label[3])
ax.text(x3[1],y3[1],z3[1],label[5])
ax.text(x3[2],y3[2],z3[2],label[3])
ax.text(x3[3],y3[3],z3[3],label[2])
ax.text(x3[3],y3[3],z3[3],label[2])
ax.text(x3[3],y3[3],z3[3],label[2])
ax.text(x3[3],y3[3],z3[3],label[2])
ax.plot(x3,y3,z3,color='g',linestyle=':',label='D=A+B+C')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
plt.show()

