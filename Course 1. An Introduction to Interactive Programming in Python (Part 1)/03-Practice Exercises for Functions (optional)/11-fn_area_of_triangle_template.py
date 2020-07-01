'''Challenge: Write a Python function `triangle_area` that takes the parameters x0,y0, x1,y1, and x2,y2, and returns the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). (Hint: use the function `point_distance` as a helper function and apply Heron's formula.)
'''
# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Also define point_distance as use it as a helper function.

def point_distance(x1, y1, x2, y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def triangle_sides(x0, y0, x1, y1, x2, y2):
    a = point_distance(x0,y0, x1,y1)
    b = point_distance(x1,y1, x2,y2)
    c = point_distance(x2,y2, x0,y0)
    return a, b, c

def triangle_area(x0, y0, x1, y1, x2, y2):
    a, b, c = triangle_sides(x0, y0, x1, y1, x2, y2)
    s = (a+b+c) / 2

    return ( s*(s-a)*(s-b)*(s-c) )**0.5

###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1, x2, y2):
    print("A triangle with vertices (" + str(x0) + "," + str(y0) + "),", end=" ")
    print("(" + str(x1) + "," + str(y1) + "), and", end=" ")
    print("(" + str(x2) + "," + str(y2) + ") has an area of", end=" ")
    print(str(triangle_area(x0, y0, x1, y1, x2, y2)) + ".")

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
