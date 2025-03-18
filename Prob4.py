# Write a program that takes a a coordinate and tell which quadrant the coordinate falls.

var_x = (input("Enter x-coordinate: "))
var_y = (input("Enter y-coordinate: "))
x = int(var_x)
y = int(var_y)

if x > 0 and y > 0:
    print("The point is in Quadrant I.")
elif x < 0 and y > 0:
    print("The point is in Quadrant II.")
elif x < 0 and y < 0:
    print("The point is in Quadrant III.")
elif x > 0 and y < 0:
    print("The point is in Quadrant IV.")
elif x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point is on the y-axis.")
else:
    print("The point is on the x-axis.")
