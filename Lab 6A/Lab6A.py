# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 6A
# Date:         9 October 2026


# Test Cases:
# Input: A = 1, B = 1, C = 1, D = 1, [-2, 0] Output: -1
# Input: A = 3, B = 5, C = 7, D = 9, [-5, -1] Output: -1.46872
# Input: A = -2, B = 4, C = -6, D = 8, [-10, 10] Output: 1.65063
# Input: A = -1, B = 1, C = -1, D = 2, [-100, 100] Output: 1.35321

# Read the coefficients of the polynomial from the user 
print("The equation for a cubic polynomial is Ax^3 + Bx^2 + Cx + D")
print()
print("This program will find the root of the cubic polynomial at any given interval")
print()
a = float(input("What is the value of A?: "))
b = float(input("What is the value of B?: "))
c = float(input("What is the value of C?: "))
d = float(input("What is the value of D?: "))


# Read in the upper and lower bounds around a single root of the polynomial 

x1 = float(input("What is the lower bounds? (x1): "))
x2 = float(input("What is the upper bounds? (x2): "))

error = x1 >= x2 

if x1 >= x2:
    print("You can't set x1 to be greater than or equal to x2")
    

    

# Determine the value of the root to within 10^-6
if not error:
    f_x1 = a * (x1 ** 3) + b * (x1 ** 2) + c * x1 + d
    f_x2 = a * (x2 ** 3) + b * (x2 ** 2) + c * x2 + d

    if f_x1 * f_x2 > 0:
        print("The interval does not contain a root.")

    else:
        f_p = 1
        iteration = 0

        while (x2 - x1) >= 1e-6:
            iteration += 1
            p = (x1 + x2) / 2

            f_p = a * (p ** 3) + b * (p ** 2) + c * p + d

            if f_p == 0:
                break
            elif f_x1 * f_p < 0:
                x2 = p
                f_x2 = f_p
            else:
                x1 = p
                f_x1 = f_p
        # Print the result of that root finding as a single number
        print()
        print(p)
        # Print out how many iterations it took to find that root. 
        print("It took", iteration, "iteration(s) to find the root!")
        

