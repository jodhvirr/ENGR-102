# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 11A
# Date:         9 November 2026

file_name = input("Enter the name of the file: ")
required = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]
count = 0

outfile = open("valid_passports.txt", "w")

with open(file_name, "r") as file:
    data = file.read()
    passports = data.strip().split("\n\n")
    
    
    for i in range(len(passports)):
        isValid = True
        for r in required:
            if r not in passports[i]:
                isValid = False
        if isValid:
            
            if count > 0:
                outfile.write("\n\n")
            count += 1    
            outfile.write(passports[i])
                
print("There are", count, "valid passports")
                

           
outfile.close()
            
        

