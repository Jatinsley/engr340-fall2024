import math
from distutils.command.build_py import build_py
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    a2 = (a + b) / 2
    b2 = (a*b)**(1/2)
    p2 = 2*p
    t2 = t - (p*(a2-a)**2)
    a = a2
    b = b2
    p = p2
    t = t2
    print("new values", a2, b2, p2, t2)

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1/ (2**(1/2))
t = 1/4
p = 1

# perform 10 iterations of this loop
pi_estimate = ((a2 + b2) ** 2) / (4 * t2)


print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))







