# Highly divisible triangular number

# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

def triangle(number):
    trian = (number * (number + 1)) // 2
    return trian

def divisors(num):
    count = 0
    for j in range(1, num):
        if num % j == 0:
            count += 1
    return count, num

def main():
    i = 1
    while True:
        x, y = divisors(triangle(i))
        if x != 500:
            i += 1
        if x == 500:
            break
    print(f'The value is {y}')

if __name__ == '__main__':
    main()