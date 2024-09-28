from ctypes import*
import matplotlib.pyplot as plt
import numpy as np
rel = CDLL('./func.so')
a = np.array(([1,2])).reshape(1,-1)
b = np.array(([4,6])).reshape(1,-1)
c = 2
area = rel.area
area.restype = c_double

filename = 'main.txt'

with open(filename,'r') as file:
    data = file.readlines()
    print (data)

dist = 78.5
print(dist)

center = (1, 2)
point = (4, 6)
label=('A(1,2)', 'B(4,6)')
radius = np.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)

theta = np.linspace(0, 2 * np.pi, 100)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Circle')
plt.scatter(*center, color='red', label='Center (1, 2)')
plt.scatter(*point, color='blue', label='Point (4, 6)')
plt.text(center[0], center[1], label[0], color='red')
plt.text(point[0], point[1], label[1], color='blue')
plt.xlim(-5, 10)  
plt.ylim(-5, 10) 
plt.gca().set_aspect('equal', adjustable='box') 
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Circle with Center (1, 2) and Point (4, 6)')
plt.legend()
plt.show()

