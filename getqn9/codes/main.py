import numpy as np
import matplotlib.pyplot as ply

# Load points from the file
points = np.loadtxt("main.txt", delimiter=' ', max_rows=len(list(open("main.txt")))-1)

# Extract x and y values
x = points[:, 0]
y = points[:, 1]

# Define points A, B, C, D
A = np.array([0, 0])
B = np.array([4, 4])
C = np.array([6, 9])
D = np.array([8, 16])

# Plot the parabola
ply.plot(x, y, label='Parabola')

# Plot the specific points
ply.scatter(A[0], A[1], color='green', marker='o', label='Point A (0,0)')
ply.scatter(B[0], B[1], color='red', marker='o', label='Point B (4,4)')
ply.scatter(C[0], C[1], color='purple', marker='o', label='Point C (6,9)')
ply.scatter(D[0], D[1], color='orange', marker='o', label='Point D (8,16)')

# Create an x range for shading
x_fill = np.linspace(0, 6, 400)
y_fill = np.linspace(2.82, 0, 400)
y_parabola = np.interp(x_fill, x, y)
x_parabola = np.interp(y_fill, y, x)

# Define the y values for the lines
y1 = 2 * np.ones_like(x_fill)  # Line y = 2
y2 = 4 * np.ones_like(x_fill)  # Line y = 4

# Shade the region between the lines and the parabola
# Ensure we fill only the area between y1 and the parabola
ply.fill_between(x_fill, y2, np.minimum(y_parabola, y2), where=(y_parabola >= y1) & (y_parabola <= y2), color='gray', alpha=0.5, label='Shaded region')
ply.fill_between(y_fill, 2, 4, color='gray', alpha=0.5)

# Plot the lines
ply.plot(x_fill, y1, label='y = 2', color='blue')
ply.plot(x_fill, y2, label='y = 4', color='orange')

# Set axis limits
ply.xlim(0, 6)  # Set x-axis limits
ply.ylim(0, 12)  # Set y-axis limits

# Add labels and title
ply.xlabel("X-axis")
ply.ylabel("Y-Axis")
ply.title("Points A, B and Shaded Region Along Parabola")

# Add grid and legend
ply.grid(True)
ply.legend()

# Save the figure
ply.savefig('../figs/fig.jpg')
ply.show()

