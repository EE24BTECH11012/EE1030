import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('value.dat', skiprows=0)
labels = ['A(0,4)', 'B(-2,3)', 'C(2,5)' ]
x = data[:, 0]# Extract x-coordinate data from values.dat
y = data[:, 1]# Extract y-coordinate data from values.dat
plt.plot(x,y, color='blue', marker='o')
#plt.figure(figsize=(100, 100))
for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, fontsize=12, ha='right', va='bottom')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Finding the other end point of the given line segment.')
plt.grid()
plt.savefig("value1.jpg")
plt.show()


