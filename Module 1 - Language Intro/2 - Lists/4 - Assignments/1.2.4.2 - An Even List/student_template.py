import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""

# use len() to find the length of the list
list_length = len(even_list) #modify this line to perform the correct operation

# now calculate the middle index of the list
middle_index_1 = (list_length//2) - 1
middle_index_2 = (list_length//2) #modify this line to perform the correct operation

# use [] to access the middle element. Set it equal to middle_element
middle_element_1 = even_list[middle_index_1] #modify this line to perform the correct operation
middle_element_2 = even_list[middle_index_2]
# this is the final result. Modify this line, and the empty lines above, to solve the assignment
print("Middle element 1 is: ", middle_element_1)
print("Middle element 2 is: ", middle_element_2)
middle_average = (middle_element_1+middle_element_2)/2

# the average of middle elements is
print("The average is: ", middle_average)
