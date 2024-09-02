from ctypes import *
import matplotlib.pyplot as plt
rel1 = CDLL('./mp.so')
rel2 = CDLL('./f1.so')
rel3 = CDLL('./f2.so')
a = -5
b = -4
c = 7
d = 5
mp = rel1.mp
mp.restype = c_float
f1 = rel2.f1
f1.restype = c_float
f2 = rel3.f2
f2.restype = c_float


# Data for plotting
filename = 'main.txt'

with open(filename, 'r') as file:
    data = file.readlines()

print (data) 

x = [-5, -4, mp(c_float(a), c_float(b)), f1(c_float(a), c_float(c)) , f1(c_float(b), c_float(d))]
y = [7, 5, mp(c_float(c), c_float(d)), f2(c_float(a), c_float(c)), f2(c_float(b), c_float(d))]
labels = ['A(-5,-4)', 'B(7,5)', 'C', 'D', 'E']

# Create a scatter plot
plt.scatter(x, y)

# Label each point
for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, fontsize=12, ha='right')
    plt.plot (x, y, color='red', linestyle='-')

# Add title and labels
#plt.title('Scatter Plot with Labels')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()

