# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 6B
# Date:         9 October 2026

from math import * 

# Part A

# Ask the user inputs for a cubic polynomial (4 coefficients)
print("The equation for a cubic polynomial is Ax^3 + Bx^2 + Cx + D")
print()

a = float(input("What is the value of A?: "))
b = float(input("What is the value of B?: "))
c = float(input("What is the value of C?: "))
d = float(input("What is the value of D?: "))

print()

print("The derivative is 3Ax^2 + 2Bx + C")

# ask the user for a x value 
x_value = float(input("Insert a value of x to find the derivative: "))

# substitute that x value using the derivative equation calculated earlier

f_prime_x_value = (3 * a * x_value ** 2) + (2 * b * x_value) + c

print("The value of the derivative at x =", x_value, "is", f_prime_x_value)


#------------------------------------------------------------------------------

# Part B

# define variables
delta_x = 0.1
estimate = 0
previous_estimate = 0
iteration = 0

# keep going until the guesses are really close to each other
while iteration == 0 or abs(estimate - previous_estimate) >= 10 ** -6:
    iteration += 1
    previous_estimate = estimate
    f_a_x = (a * (x_value + delta_x) ** 3) + (b * (x_value + delta_x) ** 2) + (c * (x_value + delta_x)) + d
    f_x = (a * (x_value) ** 3) + (b * (x_value) ** 2) + (c * (x_value)) + d
    # slope formula
    estimate = (f_a_x - f_x) / (delta_x)
    delta_x /= 2
    
# show results and compare to the real answer
print()
print("Numerical estimate:", estimate)
print("Number of iterations:", iteration)
print("Actual derivative:", f_prime_x_value)
print("Absolute error:", abs(estimate - f_prime_x_value))

#------------------------------------------------------------------------------

# Part C

# Functions:
# tan(x) at x = 1 
# ln(x) at x = 2  
# e^x at x = 3 
# 3^x at x = 4 

for i in range(1,5):
    if i == 1:
       name = "tan(x)" 
       x = 1 
    if i == 2:
        name = "ln(x)"
        x = 2
    if i == 3:
        name = "e^x"
        x = 3
    if i == 4:
        name = "3^x"
        x = 4
      
    # define variables
    delta_x = 0.1
    estimate = 0
    previous_estimate = 0
    iteration = 0

    # keep going until the guesses are really close to each other
    while iteration == 0 or abs(estimate - previous_estimate) >= 10 ** -6:
        iteration += 1
        previous_estimate = estimate
        
        if i == 1:
            # calculate f(x + delta_x) and f(x) for the current function
            f_new = tan(x + delta_x)
            f_old = tan(x)
            
        if i == 2:
            # calculate f(x + delta_x) and f(x) for the current function
            f_new = log(x + delta_x)
            f_old = log(x)
            
        if i == 3:
            # calculate f(x + delta_x) and f(x) for the current function
            f_new = e ** (x + delta_x)
            f_old = e ** x
            
        if i == 4:
            # calculate f(x + delta_x) and f(x) for the current function
            f_new = 3 ** (x + delta_x)
            f_old = 3 ** (x)    
        
        estimate = (f_new - f_old) / delta_x
        delta_x /= 2
        
    # print the output
    print()
    print("Derivative of", name, "at x =", x, "is about", estimate, "and took", iteration, "steps")
   




