from ctypes import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

rel = CDLL('./func.so')
a=2
b=3
c=-4
d=3
e=-4
f=-5
g=3
h=2
i=-3
mod = rel.mod
mod.restype = c_float

filename = 'main.txt'

with open(filename,'r') as file:
    data = file.readlines()
    print(data)

abs_value = mod(c_float(a), c_float(b), c_float(c), c_float(d), c_float(e), c_float(f), c_float(g), c_float(h), c_float(i))

print(abs_value)



x = [2,3,3,8,0]
y = [3,-4,2,1,0]
z = [-4,-5,-3,-12,0]
label=['A(2,3,-4)', 'B(3,-4,-5)', 'C(3,2,-3)', 'D(8,1,-12)', 'E(0,0,0)']
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, color='b', s=100)  # s is the size of the points

ax.text(x[0],y[0],z[0],label[0])
ax.text(x[1],y[1],z[1],label[1])
ax.text(x[2],y[2],z[2],label[2])
ax.text(x[3],y[3],z[3],label[3])
ax.text(x[4],y[4],z[4],label[4])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()

