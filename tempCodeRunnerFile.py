import random # Importing the random module for generating random numbers
import matplotlib.pyplot as plt # Importing matplotlib

num_points = 10000 # Defining the number of random points to generate
inside_circle = 0  # Counter for points that fall inside the circle
x_inside, y_inside = [], [] # Lists to store coordinates of points inside the circle
x_outside, y_outside = [], [] # Lists to store coordinates of points outside the circle

for _ in range(num_points):  # Loop to generate num_points random points
    x, y = random.uniform(-1, 1), random.uniform(-1,1) # Generate a random point (x, y) in the range [-1, 1]
    if x**2 + y**2 <= 1: # Check if the point lies inside the unit circle (x² + y² ≤ 1)
        inside_circle += 1 # Increment counter if the point is inside the circle
        x_inside.append(x) # Store x-coordinate of inside point
        y_inside.append(y) # Store y-coordinate of inside point
    else:
        x_outside.append(x) # Store x-coordinate of outside point
        y_outside.append(y)  # Store y-coordinate of outside point

pi_estimate = (inside_circle / num_points) * 4 # Estimate the value of π using the Monte Carlo method
print(f"Estimated pi  {pi_estimate}")


plt.figure(figsize=(5, 5)) # Create a figure with a square aspect ratio
plt.scatter(x_inside, y_inside, color='blue', s=1)  # Plot points inside the circle in blue
plt.scatter(y_outside, x_outside, color='red', s=1)  # Plot points outside the circle in red

plt.xlabel("X") # Label for x-axis
plt.ylabel("Y")  # Label for y-axis
plt.title("Monte Carlo Simulation for PI Approximation") # Title of the plot
plt.show()  # Display the plot

