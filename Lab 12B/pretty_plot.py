# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 12B
# Date:         17 November 2026


import numpy as np
import matplotlib.pyplot as plt

v = np.array([0,1]).reshape(2, 1)

M = np.array([1.02, 0.095, -0.095, 1.02]).reshape(2,2)

x = [v[0,0]]
y = [v[1,0]]


for i in range(250):
    new_v = M @ v
    v = new_v
    x.append(v[0][0])
    y.append(v[1][0])
    
plt.plot(x,y, color = "red", label = "Spiral")
plt.title("Outward Spiral")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
    

