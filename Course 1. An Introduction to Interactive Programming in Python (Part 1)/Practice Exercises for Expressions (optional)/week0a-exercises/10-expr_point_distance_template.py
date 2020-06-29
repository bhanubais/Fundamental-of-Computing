'''The distance between two points `(x_0, y_0)` and `(x_1, y_1)` is `sqrt((x_0-x_1)^2 + (y_0-y_1)^2)`. Write a Python statement that calculates and prints the distance between the points (2,2) and (5,6)
'''
# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Distance formula
# Student should enter statement on the next line.

# Hint: You need to use the power operation ** .

x_0, y_0 = 2, 2
x_1, y_1 = 5, 6

distance = ((x_0-x_1)**2 + (y_0-y_1)**2)**(1/2)
print(distance)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#5.0
