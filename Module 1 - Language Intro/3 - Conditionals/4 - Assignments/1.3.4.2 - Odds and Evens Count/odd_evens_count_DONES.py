# bring in randomness cause we need it in our lives
import random
from telnetlib import theNULL


### Begin Dr. Forsyth Code. Do Not Modify ###

# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# set the maximum length of the list
max_length = 100

# set the maximum upper bound for the list
upper_bound = 1000

# generate a random lists of integers
nums = generate_random_int_list(max_length, upper_bound)

# create two variables to hold the final answers
evens_list = 0
odds_list = 0
list_length = len(nums)

for n in nums:
    if n % 2 ==0:
        evens_list = evens_list + 1
    else :
        odds_list = odds_list + 1

print(nums)
print("Number of evens in our list is: ", evens_list)
print("Number of odds in our list is: ",  odds_list)

### YOUR CODE BEGINS HERE ###