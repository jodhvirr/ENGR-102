# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 2A
# Date:         1 September 2026 





time = 37

initial_time = 30
initial_distance = 50

final_time = 45
final_distance = 615

slope = (final_distance - initial_distance) / (final_time - initial_time)




if time >= initial_time and time <= final_time:
    distance = slope * (time - initial_time) + initial_distance
    print("Time: ", time)
    print("Distance" , distance, "meters past the starting line")
    
else:
    print("You got an error")
    

