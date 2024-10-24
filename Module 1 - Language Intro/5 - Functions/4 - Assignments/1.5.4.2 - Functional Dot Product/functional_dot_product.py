import random
import numpy as np
from numpy.random import random_sample


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)
    # return the generated list
    return randoms
max_length = 10
maximum_value = 100
fixed_length = int(random.uniform(2, max_length))
vector_a = generate_random_int_list(fixed_length, maximum_value)
vector_b = generate_random_int_list(fixed_length, maximum_value)
length = len(vector_a)

length = len(vector_a)
def dot_product(a,b):
    dot_product = 0
    for i in range(length):
        dot_product = dot_product + (vector_a[i] * vector_b[i])
    print(dot_product)

    """
    A custom function to calculate the dot product of two lists
    :param a: List A of values
    :param b: List B of values
    :return: The dot product as a value between a * b
    """
    return dot_product
    print("Dot Product =", dot_product(vector_a,vector_b))
    ### YOUR CODE HERE ###


    ### CHANGE THIS RETURN VALUE. IT IS HERE SO THE CODE DOES NOT ERROR

"""
Step 1: Generate two "vectors" of equal length but full of random values
"""

"""
Step 2: Call your custom dot_product function
"""
result = dot_product(vector_a,vector_b)

"""
Step 3: Check your calculation against numpy
"""
true_result = np.dot(vector_a,vector_b)

"""
Step 4: See if you're correct....
"""
if result is None:
    print("Result is None. You didn't change the result statement in the function")

elif abs(result - true_result) < 0.0001:
    print("Correct!")

else:
    print("Result contains too much error!")
    print("Result", result,vector_a,vector_b)
    print("True Result", true_result,vector_a,vector_b)