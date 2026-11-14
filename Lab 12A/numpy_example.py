# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 12A
# Date:         11 November 2026 


# As a team, we have gone through all required sections of the
# tutorial and each team member understands the material

import numpy as np


a = np.arange(0,12).reshape(3,4)

b = np.arange(0,8).reshape(4,2)

c = np.arange(0,6).reshape(2,3)

d = a @b @c

d_t = d.T

e = (np.sqrt(d)) / (2)


