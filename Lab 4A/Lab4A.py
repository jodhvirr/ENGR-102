# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 4A
# Date:         16 September 2026 

from math import *

# Example 1:
a = 1/7
b = a * 7
c = a + a + a + a + a + a + a

print(b)
print(c)
print(f"Is 1/7 * 7 the same as adding 1/7 seven times? {b == c}", "\n")


# Example 2: 
a = 0.1 + 0.2
b = 0.3

print(a)
print(b)
print(f"Is 0.1 + 0.2 the same as 0.3? {a == b}", "\n")


# Example 3:
a = 0
a = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 
b = 0.1 * 10
print(a)
print(b)
print(f"Is .1 * 10 the same thing as adding .1 ten times? {a==b}", "\n")


# Part 2: Tolerance Check for b and e
TOL = 1e-10
a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)

if abs(b-e) < TOL:
    print("b and e are equal within tolerance of", TOL, "\n")
else:
    print("b and e are NOT equal within tolerance of", TOL, "\n")
    
# Part 2: Tolerance check for y and z



x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)

if abs(y-z) < TOL:
    print("y and z are equal within tolerance of", TOL, "\n")
else:
    print("y and z are NOT equal within tolerance of", TOL, "\n")