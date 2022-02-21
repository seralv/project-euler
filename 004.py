# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(number):
    newNumber = int(str(number)[::-1])
    if number == newNumber:
        return True
    else:
        return False

limit = 1000
for i in range(limit):
    for j in range(limit):
        mult = i * j
        if palindrome(mult):
            firstValue = i
            secondValue = j

print(f'The largest numbers product a palindrome are {firstValue} x {secondValue} = {(firstValue * secondValue)}')