from numpy import random
import numpy as np
from numpy.ma.extras import average
from numpy.random import normal

# Parameters for distribution and samples to generate
# These values are fixed. Do not change.
mu = 1
std = 1.2

# Step 1: Set the number of samples you wish to take. This value is selected by you.
num_samples = 10000000

# Step 2: use normal to generate distribution samples
samples = random.normal(1,1.2,num_samples)

# Step 3: use mean() to determine the average of those samples
measured_mean = abs(np.mean(samples))

# Step 4: use std() to determine the standard deviation of samples
measured_deviation = abs(np.std(samples))

# check if sufficient samples were taken. Do not modify below this line
print("mu=", measured_mean, "stdev=", measured_deviation)

mean_error = abs(mu - measured_mean)
deviation_error = abs(std - measured_deviation)
print("Mean Error Is:", mean_error)
print("Deviation Error Is:", deviation_error)
if mean_error < 1E-3 and deviation_error < 1E-3:
    print('Solution within error tolerances')
else:
    print('Solution is not within error tolerances')