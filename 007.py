# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

counter = 0
j = 1
place = 10001

while counter != place:
    j += 1
    if prime(j):
        counter += 1

print(f'The {place}st prime is {j}')
