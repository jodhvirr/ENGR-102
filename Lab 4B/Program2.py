# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 4B
# Date:         17 September 2026



print("The quadratic equation is Ax^2 + Bx + C")
a = float(input("What is the coefficent of x^2 (A)?: "))
b = float(input("What is the coefficent of x (B)?: "))
c = float(input("What is the value of C?: "))

discriminant = (b**2) - (4 * a * c)


if a != 0:
    if discriminant >= 0:
        solution1 = (-b + (discriminant ** 0.5)) / (2 * a)
        solution2 =  (-b - (discriminant ** 0.5)) / (2 * a)
        print("The roots are:", solution1, "and", solution2)
    else:
        imaginary_value = str(abs((discriminant) ** 0.5) / abs((2 * a)))
        starting_value = str((-b) / (2 * a))
        
        print("The roots are: " + starting_value + " + " + imaginary_value + "i")
        print("The roots are: " + starting_value + " - " + imaginary_value + "i")
        
    

elif b != 0:
    solution = -c/b
    print("The root is:", solution)
    

elif c == 0:
    print("Infinite Solutions")
    
else:
    print("Error, no solution.")


