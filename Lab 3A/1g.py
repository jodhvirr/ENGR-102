# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 3A
# Date:         9 September 2026 

from math import *

voltage = float(input("How much Voltage are you trying to convert to Voltage Level?: "))
voltage_level = 20 * log10(voltage)
print(voltage_level , "dBV")

