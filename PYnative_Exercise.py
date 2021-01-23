# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:02:04 2020

@author: Magdalena
"""

# =============================================================================
# Exercise 1: Print First 10 natural numbers using while loop (from 0)
# Expected output:
# 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# =============================================================================

print('\nExercise 1\n')

x = 0

while x <= 10:
    print (x)
    x += 1

    
# =============================================================================
# Exercise 2: Print the following pattern
# 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# =============================================================================

print('\nExercise 2\n')

pattern = ''

for x in range(1, 6):
    pattern += str(x) + ' '
    print(pattern)


# =============================================================================
# Exercise 3: Accept number from user and calculate the sum of all number
# between 1 and given number
# For example user given 10 so the output should be 55
# =============================================================================


print('\nExercise 3\n')

guess = int(input('Give any natural number: '))
sum = 0

for x in range(1, guess+1):
    sum += x
print('The sum of the numbers is:', sum)


# =============================================================================
# Exercise 4: Print multiplication table of given number
# For example num = 2 so the output should be
# 
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# =============================================================================


print('\nExercise 4\n')

num = int(input('Give any integer: '))
    
for x in range(1, 11):
    print(num * x)


# =============================================================================
# Exercise 5: Given a list iterate it and display numbers which are divisible 
# by 5 and if you find number greater than 150 stop the loop iteration
# 
# 
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# =============================================================================


print('\nExercise 5\n')

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for item in list1:
    if item > 150:
        break
    elif item % 5 == 0:
        print(item)


# =============================================================================
# Exercise 6: Given a number count the total number of digits in a number
# For example, the number is 75869, so the output should be 5
# =============================================================================


print('\nExercise 6\n')

num = int(input('Give any integer: '))
ans = 0

for x in str(num):
    ans += 1
print(ans)


# =============================================================================
# Exercise 7: Print the following pattern using for loop
# 
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# =============================================================================

print('\nExercise 7\n')

number = 5

for item1 in range(0,6):
    for item2 in range(number-item1,0,-1):
        print(item2,end=' ')
    print()


# =============================================================================
# Exercise Question 8: Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]
# 
# Expected output:
# 
# 50
# 40
# 30
# 20
# 10
# =============================================================================

print('\nExercise 8\n')

list1 = [10, 20, 30, 40, 50]

for item in reversed(list1):
    print(item)


# =============================================================================
# Exercise Question 9: Display -10 to -1 using for loop
# Expected output:
# 
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
# =============================================================================

print('\nExercise 9\n')

for number in range(-10, 0):
    print(number)


# =============================================================================
# Exercise Question 10: Display a message “Done” after successful execution of 
# for loop
# For example, the following loop will execute without any error.
# 
# for i in range(5):
#     print(i)
# So the Expected output should be:
# 
# 0
# 1
# 2
# 3
# 4
# Done!
# =============================================================================

print('\nExercise 10\n')

for i in range(5):
    print(i)
print('Done!')

# =============================================================================
# Exercise Question 11: Python program to display all the prime numbers within 
# a range
# Note: A Prime Number is a whole number that cannot be made by multiplying 
# other whole numbers
# 
# Examples:
# 
# 6 is not a Prime Number because it can be made by 2×3 = 6
# 37 is a Prime Number because no other whole numbers multiply together to 
# make it.
# 
# Given:
# 
# start = 25
# end = 50
# Expected output:
# 
# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47
# =============================================================================

print('\nExercise 11\n')

start = 25
end = 50

print('Prime numbers between', start, 'and', end, 'are:')
for i in range(start, end+1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)


# =============================================================================
# Exercise Question 12: Display Fibonacci series up to 10 terms
# Expected output:
# 
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
# =============================================================================

print('\nExercise 12\n')

a = 0
b = 1

print('Fibonacci sequence:')
for item in range(10):
    if item == 0:
        print(a, end = ' ')
    elif item == 1:
        print(b, end = ' ')
    else:
        c = a + b
        a = b
        b = c
        print(c, end = ' ')


# =============================================================================
# Exercise Question 13: Write a loop to find the factorial of any number
# The factorial (symbol: !) means to multiply all whole numbers from our chosen 
# number down to 1.
# 
# For example: calculate the factorial of 5
# 
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:
# 
# 120
# =============================================================================

print('\nExercise 13\n')

number = int(input('Give any integer: '))

factorial = 1

if number < 0:
    print("factorial doesn't exist")
elif number == 0:
    print("factorial of 0 equals 1")
else:
    for num in range(1, number+1):
        factorial *= num
    print('factorial of number', number, 'is:', factorial)

# =============================================================================
# Exercise Question 14: Reverse a given integer number
# Given:
# 
# 76542
# 
# Expected output:
# 
# 24567
# =============================================================================

print('\nExercise 14\n')

number = int(input('Give any integer number: '))


reverse_num = 0
for x in range(len(str(number))):
    R = number % 10
    new_number = number // 10
    reverse_num = reverse_num * 10 + R
    number = new_number
print('Reverse number is:', reverse_num)


# =============================================================================
# Exercise Question 15: Use a loop to display elements from a given list which 
# are present at even positions
# Given:
# 
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# 
# Expected output:
# 
# 20 40 60 80 100
# =============================================================================

print('\nExercise 15\n')

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('elements which are present at even positions:')
position = 0

for item in my_list:
    if position % 2 != 0:
        print(item, end = ' ')
    position += 1

# =============================================================================
# Exercise Question 16: Display the cube of the number up to a given integer
# Given:
# 
# input_number = 6
# 
# Expected output:
# 
# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216
# =============================================================================

print('\nExercise 16\n')

input_number = 6

for number in range(1, input_number+1):
    cube = number ** 3
    print('Current Number is:', number, 'and the cube is', cube)


# =============================================================================
# Exercise 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# Given:
# 
# number_of_terms = 5
# 
# So series will become 2 + 22 + 222 + 2222 + 22222
# 
# Expected output:
# 
# 24690
# =============================================================================

print('\nExercise 17\n')

number_of_terms = 5

series = 0
sum_series = 0

for number in range(number_of_terms):
    series = series*10 + 2
    sum_series += series
print(sum_series)

# =============================================================================
# Exercise Question 18: Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# =============================================================================

print('\nExercise 18\n')

for x in range(2):
    if x == 0:
        for y in range(1,6):
            print('* ' * y)
    else:
        for z in range(4,0,-1):
            print('* ' * z)


        