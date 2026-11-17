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
import matplotlib.pyplot as plt

# plot 1
x = np.linspace(-2, 2, 100)

y2 = x**2 * (1/(4*2))
y6 = x**2 * (1/(4*6))

plt.figure()

plt.plot(x, y2, color = "red", linewidth = 2.0, label = "f = 2")
plt.plot(x, y6, color = "blue", linewidth = 6.0, label = "f = 6")

plt.title("Parabola plots for varying focal length")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

plt.show()

#------------------------------------------------------------------------------

# plot 2 


x_2 = np.linspace(-4, 4, 25)
y_2 = (2 * x_2 ** 3) + (3 * x_2 ** 2) - 11 * x_2 - 6

plt.figure()

plt.plot(x_2, y_2, marker = "*", linestyle = "none", color = "green", markersize = 10, label = "Polynomial")

plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plot of cubic polynomial")
plt.legend()
plt.show()

#------------------------------------------------------------------------------

# plot 3



x_3 = np.linspace(-2 * np.pi, 2 * np.pi, 100)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x_3, np.sin(x_3), color = "blue", label = "sin(x)")
plt.title("sinx")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x_3, np.cos(x_3), color = "purple", label = "cos(x)")
plt.title("cosx")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()

plt.show()
