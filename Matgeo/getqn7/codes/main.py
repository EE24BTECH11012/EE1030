import matplotlib.pyplot as plt


# Create a list of x and y values for both lines
x1 = [-4, 4]
y1 = [2, 2]

x2 = [2, 2]
y2 = [-4, 4]

# Create the plot
plt.plot(x1, y1, marker='o', label='y=2 with Direction (1,0)', color='blue')  # First line
plt.plot(x2, y2, marker='o', label='x=2 with Direction (0,1)', color='orange')  # Second line

# Label the points for the first line
plt.text(x1[0], y1[0], f'({x1[0]}, {y1[0]})', fontsize=10, ha='right')
plt.text(x1[1], y1[1], f'({x1[1]}, {y1[1]})', fontsize=10, ha='left')

# Label the points for the second line
plt.text(x2[0], y2[0], f'({x2[0]}, {y2[0]})', fontsize=10, ha='right')
plt.text(x2[1], y2[1], f'({x2[1]}, {y2[1]})', fontsize=10, ha='left')

# Add labels, title, and legend
plt.title("Plot of Two Lines with Labeled Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Add grid
plt.grid()

# Show the plot
plt.xlim(-5, 5)  # Adjust x-axis limits
plt.ylim(-5, 5)  # Adjust y-axis limits
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # X-axis
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Y-axis
plt.show()

