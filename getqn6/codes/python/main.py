#Code by GVV Sharma
#July 22, 2024
#released under GNU GPL
#Line 


import sys
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


I = np.eye(2)
e1 = I[:,[0]]
e2 = I[:,[1]]

#Direction vector
m = np.array(([1, -1])).reshape(-1,1) 
n = np.array(([1, 1])).reshape(-1,1) 
c = 20

#Given points
A = np.array(([2, 0])).reshape(-1,1) 
B = np.array(([0, 2])).reshape(-1,1) 
a = np.array(([0, 0])).reshape(-1,1)
b = np.array(([2, 2])).reshape(-1,1)

#Section
k = (c-n.T@A)/(n.T@B-c)
print(k)
C = (k*B+A)/(k+1)
k1 = 20
k2 = 20
#Generating Lines
x_C = line_dir_pt(m,C,k1,k2)
x_AB = line_gen(A,B)
x_ab = line_gen(a,b)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='Direction vector ( $x+y=2$ )')
plt.plot(x_ab[0,:],x_ab[1,:],label='Normal vector ( $ x - y = 0 $)')
plt.plot(x_C[0,:],x_C[1,:])

colors = np.arange(10,10)
#Labeling the coordinates
tri_coords = np.block([A,B,C])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
    #plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,-5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')
plt.legend()
plt.show()
