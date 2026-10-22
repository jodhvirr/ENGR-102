# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 6B
# Date:         10 October 2026

# 2a--------------------------------------------------------------------------

n = int(input("Type an integer value that is positive: "))

iterations = 0

if n > 0:
    # print first number
    print(n, end = " ")
    # while n does not equal 1
    while n != 1:
    
    # if n is even
        if n % 2 == 0:
        # n / 2
            n //= 2
        
    # if n is odd
        else:
        # 3n + 1
            n = 3 * n + 1
        # add 1 to iterations
        iterations += 1
        print(n, end = " ")

    print("")
    print("It took", iterations, "iteration(s)")

    
    
else:
    print("Error! Please use a positive value! ")
    
# 2b --------------------------------------------------------------------------

total = 0
length = 0
minimum = 0
maximum = 0

# read the first measurement
measure = float(input("Insert measurements. (When you are done, type a negative value): "))

# only process while the value is not negative
while measure >= 0:
    length += 1
    total += measure

    # first value sets both min and max
    if length == 1:
        minimum = measure
        maximum = measure
    else:
        if measure < minimum:
            minimum = measure
        if measure > maximum:
            maximum = measure

    # read the next measurement
    measure = float(input("Insert measurements. (When you are done, type a negative value): "))

# only calculate and print if at least one measurement was entered
if length > 0:
    average = total / length
    print("The average is:", average)
    print("The minimum value is:", minimum)
    print("The maximum value is:", maximum)
else:
    print("No measurements were entered.")
    
# 2c---------------------------------------------------------------------------

# i is the bigger number (Y), from 2 to 100
for i in range(2, 101):
    # j is the possible divisor (X), from 2 up to i
    for j in range(2, i + 1):

        # if j goes into i evenly, print it
        if i % j == 0:
            print(j, "divides", i)
            
            