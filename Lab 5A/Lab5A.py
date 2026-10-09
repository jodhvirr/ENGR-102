# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 5A
# Date:         23 September 2026

# Construct the variables and ask the user for input
gender = input("Are you a female or a male? (f/m): ")
age = int(input("What is your age currently?: "))
isSmoker = input("Are you a smoker? (Y/N)?: ")
systolic_bp = float(input("What is your systolic blood pressure? (in mmHg): "))
hdl = float(input("What is your HDL cholesterol in (mg/dL)?: "))
is_bp_Treated = input("Have you been treated for high blood pressure? (Y/N): " )
total_cholesterol = float(input("What is the total cholesterol inside your body?: "))


    

# The total points will be used to add together the points
# from age, total cholesterol, smoking, HDL, and blood pressure
points = 0
risk_percent = ""

    
if gender.lower() == "m":
    # Determine age points based on the person's age
    if age >= 20 and age <= 34:
        points -= 9
    elif age >= 35 and age <= 39:
        points -= 4
    elif age >= 40 and age <= 44:
        points += 0
    elif age >= 45 and age <= 49:
        points += 3
    elif age >= 50 and age <= 54:
        points += 6
    elif age >= 55 and age <= 59:
        points += 8
    elif age >= 60 and age <= 64:
        points += 10
    elif age >= 65 and age <= 69:
        points += 11
    elif age >= 70 and age <= 74:
        points += 12
    elif age >= 75 and age <= 79:
        points += 13

    # Determine total cholesterol points based on age and cholesterol level
    if age >= 20 and age <= 39:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 4
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 7
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 9 
        elif(total_cholesterol >= 280):
            points += 11
            
    elif age >= 40 and age <= 49:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 3
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 5
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 6
        elif(total_cholesterol >= 280):
            points += 8       
        
    elif age >= 50 and age <= 59:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 2
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 3
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 4
        elif(total_cholesterol >= 280):
            points += 5  
        
    elif age >= 60 and age <= 69:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 1
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 1
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 2
        elif(total_cholesterol >= 280):
            points += 3        
        
    elif age >= 70 and age <= 79:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 0
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 0
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 1
        elif(total_cholesterol >= 280):
            points += 1

        
            
    # Determine smoking points based on smoking status and age
    if isSmoker.lower() == "n":
        points += 0
    
    
    elif isSmoker.lower() == "y":
        if age >= 20 and age <= 39:
            points += 8
        elif age >= 40 and age <= 49:
            points += 5
        elif age >= 50 and age <= 59:
            points += 3
        elif age >= 60 and age <= 69:
            points += 1
        elif age >= 70 and age <= 79:
            points += 1                
    
    # Determine HDL points based on the person's HDL cholesterol level
    if hdl >= 60:
        points -= 1
    elif hdl >= 50 and hdl <= 59:
        points += 0
    elif hdl >= 40 and hdl <= 49:
        points += 1
    elif hdl < 40:
        points += 2
    
    # Determine blood pressure points based on systolic blood pressure
    # and whether the person's blood pressure is being treated
    if(is_bp_Treated.lower() == "n"):
        if systolic_bp < 120:
            points += 0
        elif systolic_bp >= 120 and systolic_bp <= 129:
            points += 0
        elif systolic_bp >= 130 and systolic_bp <= 139:
            points += 1
        elif systolic_bp >= 140 and systolic_bp <= 159:
            points += 1
        elif systolic_bp >= 160:
            points += 2
        
    elif(is_bp_Treated.lower() == "y"):
        if systolic_bp < 120:
            points += 0
        elif systolic_bp >= 120 and systolic_bp <= 129:
            points += 1
        elif systolic_bp >= 130 and systolic_bp <= 139:
            points += 2
        elif systolic_bp >= 140 and systolic_bp <= 159:
            points += 2
        elif systolic_bp >= 160:
            points += 3
    
    # Convert the total Framingham points into the estimated 10-year risk
    if points < 0:
        risk_percent = "<1%"
    elif points < 5:
        risk_percent = "1%"
    elif points <= 6:
        risk_percent = "2%"
    elif points == 7:
        risk_percent = "3%"
    elif points == 8:
        risk_percent = "4%"
    elif points == 9:
        risk_percent = "5%"
    elif points == 10:
        risk_percent = "6%"
    elif points == 11:
        risk_percent = "8%"
    elif points == 12:
        risk_percent = "10%"
    elif points == 13:
        risk_percent = "12%"
    elif points == 14:
        risk_percent = "16%"
    elif points == 15:
        risk_percent = "20%"
    elif points == 16:
        risk_percent = "25%"
    else:
        risk_percent = ">=30%"
    
        

# ---------------------------------------------------------------------------------
# If the gender is female, use the female Framingham point tables
elif gender.lower() == "f":
    
    # Determine age points based on the person's age
    if age >= 20 and age <= 34:
        points -= 7
    elif age >= 35 and age <= 39:
        points -= 3
    elif age >= 40 and age <= 44:
        points += 0
    elif age >= 45 and age <= 49:
        points += 3
    elif age >= 50 and age <= 54:
        points += 6
    elif age >= 55 and age <= 59:
        points += 8
    elif age >= 60 and age <= 64:
        points += 10
    elif age >= 65 and age <= 69:
        points += 12
    elif age >= 70 and age <= 74:
        points += 14
    elif age >= 75 and age <= 79:
        points += 16

    # Determine total cholesterol points based on age and cholesterol level
    if age >= 20 and age <= 39:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 4
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 8
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 11
        elif(total_cholesterol >= 280):
            points += 13
            
    elif age >= 40 and age <= 49:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 3
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 6
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 8
        elif(total_cholesterol >= 280):
            points += 10
        
    elif age >= 50 and age <= 59:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 2
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 4
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 5
        elif(total_cholesterol >= 280):
            points += 7
        
    elif age >= 60 and age <= 69:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 1
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 2
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 3
        elif(total_cholesterol >= 280):
            points += 4     
        
    elif age >= 70 and age <= 79:
        if total_cholesterol < 160:
            points += 0
        elif(total_cholesterol >= 160 and total_cholesterol <= 199):
            points += 1
        elif(total_cholesterol >= 200 and total_cholesterol <= 239):
            points += 1
        elif(total_cholesterol >= 240 and total_cholesterol <= 279):
            points += 2
        elif(total_cholesterol >= 280):
            points += 2
            
    # Determine smoking points based on smoking status and age
    if isSmoker.lower() == "n":
        points += 0
    
    
    elif isSmoker.lower() == "y":
        if age >= 20 and age <= 39:
            points += 9
        elif age >= 40 and age <= 49:
            points += 7
        elif age >= 50 and age <= 59:
            points += 4
        elif age >= 60 and age <= 69:
            points += 2
        elif age >= 70 and age <= 79:
            points += 1
    
    # Determine HDL points based on the person's HDL cholesterol level
    if hdl >= 60:
        points -= 1
    elif hdl >= 50 and hdl <= 59:
        points += 0
    elif hdl >= 40 and hdl <= 49:
        points += 1
    elif hdl < 40:
        points += 2

    # Determine blood pressure points based on systolic blood pressure
    # and whether the person's blood pressure is being treated
    if(is_bp_Treated.lower() == "n"):
        if systolic_bp < 120:
            points += 0
        elif systolic_bp >= 120 and systolic_bp <= 129:
            points += 1
        elif systolic_bp >= 130 and systolic_bp <= 139:
            points += 2
        elif systolic_bp >= 140 and systolic_bp <= 159:
            points += 3
        elif systolic_bp >= 160:
            points += 4
        
    elif(is_bp_Treated.lower() == "y"):
        if systolic_bp < 120:
            points += 0
        elif systolic_bp >= 120 and systolic_bp <= 129:
            points += 3
        elif systolic_bp >= 130 and systolic_bp <= 139:
            points += 4
        elif systolic_bp >= 140 and systolic_bp <= 159:
            points += 5
        elif systolic_bp >= 160:
            points += 6
            
    # Convert the total Framingham points into the estimated 10-year risk
    if points < 9:
        risk_percent = "<1%"
    elif points <= 12:
        risk_percent = "1%"
    elif points <= 14:
        risk_percent = "2%"
    elif points == 15:
        risk_percent = "3%"
    elif points == 16:
        risk_percent = "4%"
    elif points == 17:
        risk_percent = "5%"
    elif points == 18:
        risk_percent = "6%"
    elif points == 19:
        risk_percent = "8%"
    elif points == 20:
        risk_percent = "11%"
    elif points == 21:
        risk_percent = "14%"
    elif points == 22:
        risk_percent = "17%"
    elif points == 23:
        risk_percent = "22%"
    elif points == 24:
        risk_percent = "27%"
    else:
        risk_percent = ">=30%"
 

 
# Display the final total points and estimated 10-year risk
print()
print("Your total Framingham points are:", points)
print("Your estimated 10-year heart attack risk is:", risk_percent)


            