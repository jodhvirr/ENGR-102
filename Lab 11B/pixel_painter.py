# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 11B
# Date:         9 November 2026

file = input("Enter the filename: ")
character = input("Enter a character: ")

file_parts = file.split(".")
new_name = file_parts[0] + ".txt"

outfile = open(new_name, "w")


with open(file, "r") as f:
    for line in f:
        read_line = line.strip()
        parts = read_line.split(",")
        
        string = ""
        for i in range(len(parts)):
            if i % 2 == 0:
                for j in range(int(parts[i])):
                    string += " "
                    
            else:
                for j in range(int(parts[i])):
                    string += character
                    
        outfile.write(string + "\n")
            
print(new_name, "created!")
outfile.close()            
        

