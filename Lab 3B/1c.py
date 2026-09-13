# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 3B
# Date:         12 September 2026

initial_production_rate = float(input("What is the initial production rate?: "))
decline_rate = float(input("What is the decline rate?: "))
hyperbolic_constant =  float(input("What is the hyperbolic constant?: "))
days = float(input("How many days?: "))
 
production_rate = (initial_production_rate) / ((1 + decline_rate * hyperbolic_constant * days) ** (1/hyperbolic_constant))
print("The production rate is", production_rate)