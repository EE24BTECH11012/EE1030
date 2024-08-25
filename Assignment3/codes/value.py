import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('value.dat', skiprows=0)

MidPoint = data[:, 0]# Extract x-coordinate data from values.dat
OnePoint = data[:, 1]# Extract y-coordinate data from values.dat
plt.plot(MidPoint,OnePoint, color='blue', marker='o')
#plt.figure(figsize=(100, 100))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Finding the other end point of the given line segment.')
plt.grid()
plt.savefig("value1.jpg")
plt.show()


