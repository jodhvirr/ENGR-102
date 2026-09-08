# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 2Bonus
# Date:         26 August 2026

import math


print("\nThis shows the evaluation of sin(x)/x as x approaches 0")
print("My guess is 1")
print(math.sin(1)/1)
print(math.sin(.1)/.1)
print(math.sin(.01)/.01)
print(math.sin(.001)/.001)
print(math.sin(.0001)/.0001)
print(math.sin(.00001)/.00001)
print(math.sin(.000001)/.000001)
print(math.sin(.0000001)/.0000001)

print("\nThis shows the evaluation of (1-cos(x))/x^2 as x approaches 0")
print("My guess is 1/2")
print((1-math.cos(1))/(1**2))
print((1-math.cos(0.1))/(0.1**2))
print((1-math.cos(0.01))/(0.01**2))
print((1-math.cos(0.001))/(0.001**2))
print((1-math.cos(0.0001))/(0.0001**2))
print((1-math.cos(0.00001))/(0.00001**2))
print((1-math.cos(0.000001))/(0.000001**2))
print((1-math.cos(0.0000001))/(0.0000001**2))


print("\nThis shows the evaluation of (1+1/x)^x as x approaches infinity")
print("My guess is 0")
print((1 + 1/1)**1)
print((1 + 1/10)**10)
print((1 + 1/100)**100)
print((1 + 1/1000)**1000)
print((1 + 1/10000)**10000)
print((1 + 1/100000)**100000)
print((1 + 1/1000000)**1000000)
print((1 + 1/10000000)**10000000)





