"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""
from gettext import install
from statistics import stdev

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
import numpy as np
import random
# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

Std_A = stdev(random_list_A)
Std_B = stdev(random_list_B)
if Std_A > Std_B:
    print("Standard Deviation of largest list is:", Std_A)
    GreaterStd = random_list_A
    longest_list_is = random_list_A
    print("Longest list is: Random List A")
if Std_B > Std_A:
    print("Standard Deviation of largest list is:", Std_B)
    GreaterStd = random_list_B
    longest_list_is = random_list_B
    print("Longest list is: Random List B")
