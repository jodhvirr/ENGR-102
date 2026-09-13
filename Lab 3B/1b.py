# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 3B
# Date:         12 September 2026

from math import *
normal_stress = float(input("What is the normal stress?: "))
cohesion = float(input("What is the cohesion?: ")) 
angle_of_internal_friction = float(input("What is the angle of internal friction?: "))

shear_stress = normal_stress * tan(radians(angle_of_internal_friction)) + cohesion

print("The shear stress is", shear_stress)