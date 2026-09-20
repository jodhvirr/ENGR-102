# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 4Bonus
# Date:         20 September 2026



days = int(input("How many days has the machine been running? (1-100): "))
widgets = 0

if days < 1 or days > 100:
    print("Invalid day number. Please enter a number from 1 to 100.")
    print("The number of widgets after", days, "day(s) is", widgets)
elif days <= 10:
    widgets += days * 10
    print("The number of widgets after", days, "day(s) is", widgets)
elif days <= 60:
    widgets += 100 + (days-10) * 40
    print("The number of widgets after", days, "day(s) is", widgets)
else: 
    day = days - 60
    last = 100 - days
    widgets = 2100 + day * (39 + last) // 2
    print("The number of widgets after", days, "day(s) is", widgets)
