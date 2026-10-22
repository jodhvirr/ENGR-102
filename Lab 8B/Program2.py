# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 8B
# Date:         17 October 2026

from math import *

# Read in dimensions, and then read in vectors into lists.
dimensions = int(input("How many dimensions are we dealing with?: "))

vector_a = []
vector_b = []


for i in range(dimensions):
    a = float(input(f"Enter component {i + 1} of the first vector: "))
    vector_a.append(a)
    
for j in range(dimensions):
    b = float(input(f"Enter component {j + 1} of the second vector: "))
    vector_b.append(b)
    
    
    
# Compute magnitude of each
sum_a = 0
for vector in vector_a:
    sum_a += vector ** 2
magnitude_a = sqrt(sum_a)

sum_b = 0
for vector in vector_b:
    sum_b += vector ** 2
magnitude_b = sqrt(sum_b)


# Compute addition and subtraction.
addition = []
subtraction = []
for i in range(dimensions):
    addition.append(vector_a[i] + vector_b[i])
    subtraction.append(vector_a[i] - vector_b[i])


# Compute dot product.
dot_product = 0
for i in range(dimensions):
    dot_product += vector_a[i] * vector_b[i]


# Output of all results, clearly labeled.
print()
print("The magnitude of the first vector is", magnitude_a)
print("The magnitude of the second vector is", magnitude_b)
print()
print("The first vector plus the second vector equals", addition)
print("The first vector minus the second vector equals", subtraction)
print()
print("The dot product of the two vectors is", dot_product)