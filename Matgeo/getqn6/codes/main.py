import matplotlib.pyplot as plt

# Define the endpoints for the first line
x1_1, y1_1 = 2, 0
x2_1, y2_1 = 0, 2

# Define the endpoints for the second line
x1_2, y1_2 = 1, 1
x2_2, y2_2 = 3, 3

# Create a list of x and y values for both lines
x_values_1 = [x1_1, x2_1]
y_values_1 = [y1_1, y2_1]

x_values_2 = [x1_2, x2_2]
y_values_2 = [y1_2, y2_2]

# Create the plot
plt.plot(x_values_1, y_values_1, marker='o', label='Direction (1,-1)', color='blue')  # First line
plt.plot(x_values_2, y_values_2, marker='o', label='Direction (1,1)', color='orange')  # Second line

# Label the points for the first line
plt.text(x1_1, y1_1, f'({x1_1}, {y1_1})', fontsize=10, ha='right')
plt.text(x2_1, y2_1, f'({x2_1}, {y2_1})', fontsize=10, ha='left')

# Label the points for the second line
plt.text(x1_2, y1_2, f'({x1_2}, {y1_2})', fontsize=10, ha='right')
plt.text(x2_2, y2_2, f'({x2_2}, {y2_2})', fontsize=10, ha='left')

# Add labels, title, and legend
plt.title("Plot of Two Lines with Labeled Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Add grid
plt.grid()

# Show the plot
plt.xlim(0, 4)  # Adjust x-axis limits
plt.ylim(0, 4)  # Adjust y-axis limits
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # X-axis
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Y-axis
plt.show()

