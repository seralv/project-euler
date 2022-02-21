# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

finder = 100

for i in range(1, 101):
    for j in range(i + 1, 101):
        for k in range(j + 1, 101):
            if (i**2 + j**2) == (k**2):
                if (k**2) == finder:
                    print(f'The product of {i}^2 + {j}^2 = {k}^2 ó {finder}')
                    break
