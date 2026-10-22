# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 6Bonus
# Date:         11 October 2026


# Ask the user for a positive integer
num = int(input("Enter a positive integer: "))
print()

# Find the sum from 0 to the number entered


# for loop
summation = 0
for i in range(0, num + 1):
    summation += i
print("For Loop: ")
print(f"The sum of all integers from 0 to {num} is {summation}")
print()

# while loop
addition = 0
k = 0
while(num >= k):
    addition += k
    k += 1
print("While Loop: ")
print(f"The sum of all integers from 0 to {num} is {addition}")
print()


# Find the product of all integers from 1 to the number entered.

# for loop
product = 1
for i in range(1, num+1):
    product *= i
print("For Loop: ")
print(f"The product of all integers from 1 to {num} is {product}")
print()

# while loop
multiply = 1
j = 1
while(num >= j):
    multiply *= j
    j += 1
print("While Loop: ")
print(f"The product of all integers from 1 to {num} is {multiply}")
print()


    
