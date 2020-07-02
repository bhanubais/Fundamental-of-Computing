'''Challenge:
Given numbers a, b, and c, the quadratic equation `ax^2 + bx + c = 0` can have zero, one or two real solutions (i.e; values for x that satisfy the equation). The quadratic formula `x = (-b+-sqrt(b^2-4ac))/2a can be used to compute these solutions. The expression `b^2-4ac` is the `discriminant` associated with the equation. If the `discriminant` is positive, the equation has two solutions. If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, the equation has no solutions. Write a Python function `smaller_root` that takes an input the numbers `a`, `b` and `c` and returns the smaller solution to this equation if one exists. If the equation has no real solution, print the message "Error: No real solutions" and simply return. Note that, in this case, the function will actually return the special Python value None.
'''
# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.

def smaller_root(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("Error: No real solutions")
        return None
    elif discriminant == 0:
        return (-b + discriminant**0.5 )/(2*a)
    else:
        roots = (-b + discriminant**0.5 )/(2*a), (-b - discriminant**0.5 )/(2*a)
        return roots[0] if roots[0] < roots[1] else roots[1]

###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    """Tests the smaller_root function."""

    print("The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:")
    print(str(smaller_root(a, b, c)))


test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None
