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
gender = input("Are you a female or a male?: ")
age = int(input("What is your age currently?: "))
isSmoker = input("Are you a smoker? (Y/N)?: ")
systolic_bp = float(input("What is your systolic blood pressure? (in mmHg): "))
hdl = float(input("What is your HDL cholesterol in (mg/dL)?: "))
is_bp_Treated = input("Have you been treated for high blood pressure? (Y/N)" )
family_heart_disease = input("Was there heart disease in father or brother beforeage 55; heart disease in mother or sister before age 65? (Y/N): ")


# Define a variable major_risk_factors to keep track on how many risk factors there are
major_risk_factors = 0

# Write if statements containing all the risk factors
# if a person has 2 or more risk factors, you can find their risk score

if isSmoker.lower() == "y":
    major_risk_factors += 1

if systolic_bp >= 140:
    major_risk_factors += 1
    
if hdl < 40:
    major_risk_factors += 1
    
if family_heart_disease.lower() == "y":
    major_risk_factors += 1

if (gender.lower() == "male" and age >= 45) or (gender.lower() == "female" and age):
    major_risk_factors += 1


 