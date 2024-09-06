from ctypes import*
import matplotlib.pyplot as plt
import numpy as np
rel = CDLL('./func.so')
a = 10
b = -6
c = 22
d = 4
mp = rel.mp
mp.restype = c_float
norm = rel.norm
norm.restype = c_float

filename = 'main.txt'

with open(filename,'r') as file:
    data = file.readlines()
    print (data)

dist = norm(c_float(a), c_float(b), c_float(c), c_float(d)) 
print(dist)

x = [10, 22, mp(c_float(a), c_float(c)) ]
y = [-6, 4, mp(c_float(b), c_float(d)) ]
label = ['A(10,-6)', 'B(22,4)', 'M(16,-1)']

plt.scatter(x,y)

plt.text(x[0], y[0], label[0], fontsize=12, ha='right')
plt.text(x[1], y[1], label[1], fontsize=12, ha='right')
plt.text(x[2], y[2], label[2], fontsize=12, ha='right')
plt.plot (x,y,color='red', linestyle='-')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.show()
