# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 3B
# Date:         12 September 2026


mass = float(input("What is the mass (kg) of the object?: "))
velocity = float(input("How fast was the object going in m/s?: "))
one_half = 1/2 

kinetic_energy = one_half * mass * (velocity ** 2)
print("The kinetic energy is" , kinetic_energy, "Joules")

