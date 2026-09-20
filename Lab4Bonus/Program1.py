# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 4Bonus
# Date:         20 September 2026


characteristic_velocity = float(input("What is the characteristic velocity of the flow (m/s)?: "))
diameter = float(input("What is the pipe's diameter (m)?: "))
kinematic_viscosity = float(input("What is the fluid kinematic viscosity (m^2/s)?: "))

reynolds_number = (characteristic_velocity * diameter) / (kinematic_viscosity)
print("Reynolds number:", reynolds_number)
if reynolds_number > 2900:
    print("The flow of the pipe is fully turbulent")

elif reynolds_number < 2300:
    print("The flow of the pipe is laminar")

else:
    print("The flow of the pipe is in transition")