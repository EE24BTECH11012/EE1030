import numpy as np
import matplotlib.pyplot as ply

points = np.loadtxt("main.txt", delimiter=',',max_rows=len(list(open("./main.txt")))-1)

x = points[:,0]
y = points[:,1]

A = np.array([1,2])
B = np.array([1,6])
C = np.array([-4,2])
D = np.array([4,1])
ply.plot(x, y, label='Circle')

ply.scatter(A[0], A[1], color='green', marker='o', label='Point A (1,2)')
ply.scatter(B[0], B[1], color='red', marker='o', label='Point B (1,6)')
ply.scatter(C[0], C[1], color='purple', marker='o', label='Point C (-4,2)')
ply.scatter(D[0], D[1], color='orange', marker='o', label='Point D (4,1)')

ply.xlabel("X-axis")
ply.ylabel("Y-Axis")
ply.title("Points A, B")
ply.grid(True)
ply.legend()
ply.axis("equal")
ply.savefig('../figs/fig.jpg')
ply.show()
