# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 3B
# Date:         12 September 2026



arrival_rate = float(input("What is the arrival rate?: "))
service_rate = float(input("What is the service rate?: "))

average_length = arrival_rate / (service_rate - arrival_rate)

print("The average number of packets in the system is", average_length)
