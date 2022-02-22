# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import numpy as np

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

limit = 1000000
sum = 0

vector = np.arange(2,limit)
arr = []

for j, value in np.ndenumerate(vector):
    if prime(value):
        arr = np.append(arr, value)
        # sum += value


# for j in range(2, limit):
#     if prime(j):
#         sum += j

print(f'The sum of primes below to {limit} are {int(arr.sum())}')