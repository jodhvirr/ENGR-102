# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 11Bonus
# Date:         10 November 2026



max_temp = float('-inf')
min_temp = float('inf')

with open("WeatherData.csv", "r") as file:
    lines = file.readlines()

for line in lines[1:]:
    data = line.strip().split(",")

    if not data[5] == "" and max_temp < int(data[5]):
        max_temp = int(data[5])

    if not data[6] == "" and min_temp > int(data[6]):
        min_temp = int(data[6])

print("10-year maximum temperature:", max_temp, "F")
print("10-year minimum temperature:", min_temp, "F")

month = input("Please enter a month: ")
year = input("Please enter a year: ")

months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
          "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

temp_total = 0
temp_count = 0
humidity_total = 0
humidity_count = 0
wind_total = 0
wind_count = 0
precip_days = 0
days_total = 0

for line in lines[1:]:
    data = line.strip().split(",")
    date = data[0].split("/")

    if int(date[0]) == months[month] and date[2] == year:

        if not data[4] == "":
            temp_total += float(data[4])
            temp_count += 1

        if not data[3] == "":
            humidity_total += float(data[3])
            humidity_count += 1

        if not data[1] == "":
            wind_total += float(data[1])
            wind_count += 1

        if not data[2] == "" and float(data[2]) > 0:
            precip_days += 1

        if not data[2] == "":
            days_total += 1

print(f"For {month} {year}:")
print(f"Mean average daily temperature: {temp_total / temp_count:.1f} F")
print(f"Mean relative humidity: {humidity_total / humidity_count:.1f}%")
print(f"Mean daily wind speed: {wind_total / wind_count:.2f} mph")
print(f"Percentage of days with precipitation: {precip_days / days_total * 100:.1f}%")
            
            
            
        
        
       
            
        
        
        
        
        
    
    
    
    