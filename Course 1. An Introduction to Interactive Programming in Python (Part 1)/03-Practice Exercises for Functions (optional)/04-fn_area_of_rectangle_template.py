'''Write a Python function rectangle_perimeter that takes two parameters width and height corresponding to the lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches.'''
# Compute the area of a rectangle, given its width and height.

###################################################
# Rectangle area formula
# Student should enter function on the next lines.

def rectangle_area(w, h):
    return w * h

###################################################
# Tests
# Student should not change this code.

def test(width, height):
    print("A rectangle " + str(width) + " inches wide and " + str(height), end=" ")
    print("inches high has an area of", end=" ")
    print(str(rectangle_area(width, height)) + " square inches.")

test(4, 7)
test(7, 4)
test(10, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.
