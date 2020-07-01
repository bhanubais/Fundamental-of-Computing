'''Write a Python function `future_value` that takes three parameters `present_value`, `annual_rate` and `years` and returns the future value of `present_value` dollars invested at `annual_rate` percent interest, compounded annually for `years` years.
'''
# Compute the future value of a given present value, annual rate, and number of years.

###################################################
# Future value formula
# Student should enter function on the next lines.

def future_value(pv, ar, yr):
    return pv * (1+ar/100)**yr

###################################################
# Tests
# Student should not change this code.

def test(present_value, annual_rate, years):
    """Tests the future_value function."""

    print("The future value of $" + str(present_value) + " in " + str(years), end=" ")
    print("years at an annual rate of " + str(annual_rate) + "% is", end=" ")
    print("$" + str(future_value(present_value, annual_rate, years)) + ".")


###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

test(1000, 7, 10)
test(200, 4, 5)
test(1000, 3, 20)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.
