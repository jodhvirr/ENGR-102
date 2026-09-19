# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 4B
# Date:         17 September 2026


num1 = float(input("What's your first number?: "))
num2 = float(input("Whats your second number?: "))
num3 = float(input("Whats your third number?: "))

if num1 > num2 and num1 > num3 :
    print(num1, "is the largest number out of those 3 numbers")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number out of those 3 numbers")
elif num3 > num1 and num3 > num2:
    print(num3, "is the largest number out of those 3 numbers")
else:
    print("2 or more of the numbers are equal")
