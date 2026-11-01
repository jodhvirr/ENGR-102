# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 9A
# Date:         25 October 2026

def get_data_points():
# 1. Get Data Points
    points = []
    
# 1.1 Ask how many points
    running = True
    while running:
        n = int(input("How many points?: "))
        
        if n <= 1:
            print("Only print integer numbers greater than 1")
        else:
            running = False
            
# 1.2 Get x and y values
    
    for i in range(n):
        x = float(input("Enter x value: "))
        y = float(input("Enter y value: "))
        # 1.3 Store data points
        points.append([x,y])

    return points; 
    
    
def get_x_value():
    
    # 2. Get Target X
    #2.1 Ask for x-value
    running = True
    while running:
        try:
            x_value = float(input("What is the target x value?: "))
            running = False
        except ValueError:
            print("Invalid Output!")
    return x_value
    #2.2 Validate input
    
    
    
def calculate():
 # 3. Calculate Estimated Y
     # 3.1 Find nearest points
     data = get_data_points()
     data.sort()
     target_x = get_x_value()
     
     # 3.2 Choose interpolation or extrapolation
     for i in range(len(data) - 1):
         
         if target_x < data[0][0]:
             point1 = data[0]
             point2 = data[1]
             method = "Extrapolation"
             break
        
         elif target_x > data[-1][0]:
             point1 = data[-2]
             point2 = data[-1]
             method = "Extrapolation"
             break         
         
         elif data[i][0] <= target_x <= data[i+1][0]:
             point1 = data[i]
             point2 = data[i+1]
             method = "Interpolation"
             break
        
    # 3.3 Calculate y-value
        
    
     x1 = point1[0]
     x2 = point2[0]
     y1 = point1[1]
     y2 = point2[1]
        
     # calculate slope   
     slope = (y2-y1) / (x2-x1)
     # calculate estimated y value
     solution = y1 + slope * (target_x - x1)
     
     return solution, method, target_x
 

def display(solution, method, target_x):
    # 4. Display Result
    # 4.1 Print y-value
    # 4.2 Print a descriptive sentence
    print(f"The estimated y value at x = {target_x} is {solution}. This was calculated using {method}.")
     
     
        
solution, method, target_x = calculate()
display(solution, method, target_x)        








        
        
