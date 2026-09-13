# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 3B
# Date:         12 September 2026

from math import *

observer_x = float(input("What is the observer's x position?: "))
observer_y = float(input("What is the observer's y position?: "))
observer_z = float(input("What is the observer's z position?: "))

point1_x = float(input("What is the x position for point 1?: "))
point1_y = float(input("What is the y position for point 1?: "))
point1_z = float(input("What is the z position for point 1?: "))

point2_x = float(input("What is the x position for point 2?: "))
point2_y = float(input("What is the y position for point 2?: "))
point2_z = float(input("What is the z position for point 2?: "))


v1_x = point1_x - observer_x
v1_y = point1_y - observer_y
v1_z = point1_z - observer_z

v2_x = point2_x - observer_x
v2_y = point2_y - observer_y
v2_z = point2_z - observer_z

v1_magnitude = sqrt(v1_x ** 2 + v1_y ** 2 + v1_z ** 2)
v2_magnitude = sqrt(v2_x ** 2 + v2_y ** 2 + v2_z ** 2)

v1_x_normalized = v1_x / v1_magnitude
v1_y_normalized = v1_y / v1_magnitude
v1_z_normalized = v1_z / v1_magnitude

v2_x_normalized = v2_x / v2_magnitude
v2_y_normalized = v2_y / v2_magnitude
v2_z_normalized = v2_z / v2_magnitude

dot_product = (v1_x_normalized * v2_x_normalized) + (v1_y_normalized * v2_y_normalized) + (v1_z_normalized * v2_z_normalized)

angle = degrees(acos(dot_product))

print("The angle is", angle, "degrees")