# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def primeFactor(n):
    count = 0
    for j in range(2, n):
        if n % j == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

x = 13195 // 2
largest = ''
for i in range(2, x):
    if primeFactor(i):
        if 13195 % i == 0:
            largest = i

print(f'The largest prime factor of 13195 is {largest}')