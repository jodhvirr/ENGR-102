# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 5B
# Date:         29 September 2026


# Ask the user for a strain value and make sure its a float
strain = float(input("What is the strain value in the range of 0 - 0.27?: "))
# Enter the values of the endpoints into the variables B_x, B_y, C_x, C_y, etc
O_x = 0
O_y = 0

B_x = 0.01
B_y = 44

C_x = 0.06
C_y = 44

D_x = 0.18
D_y = 60

E_x = .27
E_y = 51

stress = -1


# Find the slope between 0 to B and store it in slope1
slope1 = (B_y - O_y) / (B_x - O_x)

# Find the slope between B_x to C_x and store it in slope2
slope2 = (C_y - B_y) / (C_x - B_x)

# Find the slope between C_x and D_x and store it in slope3
slope3 = (D_y - C_y) / (D_x - C_x)

# Find the slope between D_x and E_x and store it in slope4
slope4 = (E_y - D_y) / (E_x - D_x)



if strain < 0:
    print("Error! The strain value cannot be negative!")
# Write if elif statements to determine which segment the strain falls under
elif strain <= 0.01:
    # Use the slope to calculate the stress
    # Store the answer in the stress variable
    stress = (slope1 * strain) + O_y


elif strain <= 0.06:
    stress = B_y + slope2 * (strain - B_x)

elif strain <= 0.18:
    stress = C_y + slope3 * (strain - C_x)

elif strain <= 0.27:
    stress = D_y + slope4 * (strain - D_x)
else: 
    print("Error! The strain value cannot be outside the range!")

# Check if stress is still -1. If it still is then the user inputted out of range value to strain
if stress == -1:
    print()
else:
    # Display the stress variable
    print("For a strain of", strain, "the calculated stress is", stress)





