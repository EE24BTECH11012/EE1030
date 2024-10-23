from ctypes import *
import matplotlib.pyplot as plt
import numpy as np
rel = CDLL('./mp.so')
a = -5
b = -4
c = 7
d = 5
mp = rel.mp
mp.restype = c_float
f1 = rel.f1
f1.restype = c_float
f2 = rel.f2
f2.restype = c_float
determinant = rel.determinant
determinant.restype = c_int


# Data for plotting
filename = 'main.txt'

with open(filename, 'r') as file:
    data = file.readlines()

print (data) 
e = np.array([1,1,1])
f = np.array([0,2,-4])
g = np.array([-3,-7,5])
#det = determinant(np.array([e,f,g]))
det = 0 
print(det)
      


x = [-5, -4, mp(c_float(a), c_float(b)), f1(c_float(a),c_float(c)), f1(c_float(b),c_float(d)) ]
y = [7, 5, mp(c_float(c), c_float(d)), f2(c_float(a),c_float(c)), f2(c_float(b),c_float(d))]
label = ['A(-5,7)', 'B(-4,5)', 'C(-6,9)', 'D(0,-3)', 'E(1,-5)']

# Create a scatter plot
plt.scatter(x, y)

# Label each point
plt.text(x[0], y[0], label[0], fontsize=12, ha='right')
plt.text(x[1], y[1], label[1], fontsize=12, ha='right')
plt.text(x[2], y[2], label[2], fontsize=12, ha='right')
plt.text(x[3], y[3], label[3], fontsize=12, ha='right')
plt.text(x[4], y[4], label[4], fontsize=12, ha='right')
plt.plot (x, y, color='red', linestyle='-')

# Add title and labels
#plt.title('Scatter Plot with Labels')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()

