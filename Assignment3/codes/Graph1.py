import matplotlib.pyplot as plt

# Define the coordinates of the points
points = {
    'A(2,5)': (2,5),
    'B(-2,3)': (-2,3),
    'M(0,4)': (0,4)
}

# Create a new figure
plt.figure()

# Plot each point
for label, (x, y) in points.items():
    plt.plot(x, y, 'o', label=f'Point {label}')  # Plot point with label
    plt.text(x, y, f' {label}', fontsize=12, ha='right')  # Add text label next to point

# Draw lines between points
for (label1, (x1, y1)), (label2, (x2, y2)) in zip(points.items(), list(points.items())[1:] + list(points.items())[:1]):
    plt.plot([x1, x2], [y1, y2], 'k-')  # 'k-' is a black line

# Set labels and title
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Two Points A and B with midpoint M')

# Add a legend
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()

