# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def multiple(number):
    for i in range(1, 20):
        if number % i == 0:
            pass
        else:
            return False
    return True

number = 0
counter = 11;
while not number:
    if multiple(counter):
        number = counter
    counter += 1
    
print(f'The smallest number divisible from 1 to 20 is {number}')