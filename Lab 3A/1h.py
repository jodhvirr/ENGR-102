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


m1 = float(input("Type your richter scale value: "))
m2 = float(input("Type your second richter scale value: "))

energy_ratio = 10 ** (1.5 * (m1 - m2))

print(energy_ratio, "is the ratio of energy released.")