# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:56:14 2020

@author: Magdalena
"""

# =============================================================================
# 1. Write a python program to print the square of all numbers from 0 to 10
# =============================================================================

print('Exercise 1\n')

for number in range(0, 11):
    print(number ** 2, end = ' ')

# =============================================================================
# 2. Write a python program to find the sum of all even numbers from 0 to 10
# =============================================================================

print('\nExercise 2\n')

sum_of_all_even_numbers = 0

for number in range(0, 11):
    if number % 2 == 0:
        sum_of_all_even_numbers += number
print(sum_of_all_even_numbers)


# =============================================================================
# 3. Write a python program to read three numbers (a,b,c) and check how many
# numbers between ‘a’ and ‘b’ are divisible by ‘c’
# =============================================================================

print('\nExercise 3\n')

a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
c = int(input('Enter the number c: '))

number_of_numbers_divisible_by_c = 0

while a <= b:
    for numbers in range(a, b+1):
        if numbers % c == 0:
            number_of_numbers_divisible_by_c += 1
    break
else:
    for numbers in range(b, a+1):
        if numbers % c == 0:
            number_of_numbers_divisible_by_c += 1

print('number of numbers divisible by c: ', number_of_numbers_divisible_by_c)


# =============================================================================
# 4. Write a python program to get the following output
# 1-----99
# 2-----98
# 3-----97
# . .
# . .
# . .
# 98-----2
# 99-----1
# =============================================================================

print('\nExercise 4\n')

sum = 100
for x in range(1, 100):
    print(x, sum - x, sep = "-----")


# =============================================================================
# 5. Write a python program to read a number and print the binary of that
# number (hint: if ‘a’ is a string , a[::-1] will be reverse of that string)
# =============================================================================

print('\nExercise 5\n')

number = int(input('Enter the number: '))

answer = ''

while number >= 1:
    new_number = int(number/2)
    R = int(number % 2)
    number = new_number
    answer += str(R)
print(answer[::-1])


# =============================================================================
# 6. Write a python program to read four numbers (representing the four
# octets of an IP) and print the next five IP address
# Eg:
# Input:
# 192 168 255 252
# ----------Output---------
# 192 168 255 253
# 192 168 255 254
# 192 168 255 255
# 192 169 0 0
# 192 169 0 1
# =============================================================================

print('\nExercise 6\n')

print('Enter IP address: ', end = ' ')
IP = input('')

new_IP = IP.split()
ip1, ip2, ip3, ip4 = int(new_IP[0]), int(new_IP[1]), int(new_IP[2]), int(new_IP[3])

number = 1

while  number <= 5:
    ip4 += 1
    if ip4 == 256:
        ip4 = 0
        if ip3 == 255:
            ip3 = 0
            ip2 += 1
    print(ip1, ip2, ip3, ip4)
    number += 1


# =============================================================================
# 7. Write a python program to print the factorial of a given number
# =============================================================================

print('\nExercise 7\n')

number = int(input('Enter the natural number: '))
answer = 1

# I wariant
for x in range(1, number + 1):
    answer *= x
print('wariant I: ', answer)
    
# II wariant
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
print('wariant II: ', factorial(number))


# =============================================================================
# 8. Write a python program to print the first 10 numbers Fibonacci series
# =============================================================================

print('\nExercise 8\n')

number = 10


# wariant I
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

for item in range(1, number + 1):
    print(fibonacci(item))

# wariant II

number = 10

a = 0
b = 1
for item in range(number + 1):
    if item == 0:
        print(a)
    elif item == 1:
        print(b)
    else:
        c = a + b
        a = b
        b = c
        print(c)
    

# =============================================================================
# 9. Write a python program to read a number and print a right triangle
# using "*"
# Eg :
# Input : 5
# ----------Output---------
# *
# * *
# * * *
# * * * *
# * * * * *
# =============================================================================

print('\nExercise 9\n')

number = int(input('Enter the natural number: '))

ans = ''
for item in range(1, number + 1):
    ans = ('* ') * item
    print(ans)

# =============================================================================
# 10. Write a python program to check given number is prime or not
# =============================================================================

print('\nExercise 10\n')

number = int(input('Enter the natural number: '))

def prime(x):
    while True:
        if x <= 1:
            return('not prime number')
        elif x == 2 or x == 3 or x == 5:
            return('prime number')
        else:
            if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
                return('not prime number')
            else:
                return('prime number')
        break
    
print(prime(number))
     

# =============================================================================
# 11. Write a python program to print all prime numbers between 0 to 100 ,
# and print how many prime numbers are there.
# =============================================================================

print('\nExercise 11\n')

prime_numbers = ''
number_of_prime_numbers = 0

for item in range(0, 101):
    if prime(item) == 'prime number':
        number_of_prime_numbers += 1
        prime_numbers += str(item) + ', '
print('number of prime numbers:', number_of_prime_numbers)
print('prime numbers:', prime_numbers)


# =============================================================================
# 12. a, b, c = 0, 0, 0 . Write a python program to print all permutations
# using those three variables
# Output : 000 , 001 ,002, 003, 004, 0005 ,006, 007, 008, 009, 010, 011 …… 999
# =============================================================================

print('\nExercise 12\n')

a, b, c = 0, 0, 0

for x in range(10):
    for y in range(10):
        for z in range(10):
            print(str(x)+str(y)+str(z), end = ', ')

