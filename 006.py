# Sum square difference

# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
  
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the 
# square of the sum is. 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.

def squares():
    sum = 0
    for i in range(1, 101):
        sum += i**2
    
    return sum

def squaresSum():
    sum = 0
    for i in range(1, 101):
        sum += i
    
    return sum**2

print(squares())
print(squaresSum())
print(f'The difference between {squares()} and {squaresSum()} of the first one hundred numbers are {(squaresSum() - squares())}')