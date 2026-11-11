# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 11Bonus
# Date:         10 November 2026


def is_valid(passport): 
    list = passport.split()
    my_dict = {}
    
    for i in range(len(list)):
        list2 = list[i].split(":")
        my_dict[list2[0]] = list2[1]
    
    isValid = True
    
    
    hgt1 = my_dict["hgt"][:-2]
    if hgt1.isdigit():
        hgt = int(hgt1)    
    units = my_dict["hgt"][-2:]
    
    
    if not (1920 <= int(my_dict["byr"]) <= 2007):
        isValid = False
        
    if not (2013 <= int(my_dict["iyr"]) <= 2023):
        isValid = False
        
    if not (2023 <= int(my_dict["eyr"]) <= 2033):
        isValid = False
        
    if not ((units == "in" and 59 <= hgt <= 76) or (units == "cm" and 150 <= hgt <= 193)):
        isValid = False
    
    
    hcl = my_dict["hcl"]
    if not (len(hcl) == 7 and hcl[0] == "#"):
        isValid = False
        
    characters = "1234567890abcdef"
    
    if len(hcl) == 7:
        for j in range(1,7):
            if not (hcl[j] in characters):
                isValid = False
    
    pid = my_dict["pid"]
    if not (len(pid) == 9 and pid.isdigit()):
        isValid = False
        
    cid = my_dict["cid"]

    if not (len(cid) == 3 and cid.isdigit() and cid[0] != "0"):
        isValid = False

    return isValid;



file_name = input("Enter the name of the file: ")
passport = ""
required = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "pid:", "cid:"]
count = 0
outfile = open("valid_passports2.txt", "w")


with open(file_name, "r") as file:
    data = file.read()
    passports = data.strip().split("\n\n")
    
    
    
    for i in range(len(passports)):
        isValid = True
        for r in required:
            if r not in passports[i]:
                isValid = False
    
        if isValid:
            isValid = is_valid(passports[i])
            
        if isValid:
            if count > 0:
                outfile.write("\n\n")
            count += 1    
            outfile.write(passports[i])
       
              
print("There are", count, "valid passports")
outfile.close()

