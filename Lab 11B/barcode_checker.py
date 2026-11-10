# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 11B
# Date:         5 November 2026




f = input("Enter the name of the file: ")
count = 0

outfile = open("valid_barcodes.txt", "w")
               
with open(f, "r") as file:  
    for line in file:
        barcode = line.strip()
        
        if len(barcode) == 13:
            first_group = []
            second_group = []
        
            for digit in barcode[0:12:2]:
                first_group.append(int(digit))
        
            for digit in barcode[1:12:2]:
                second_group.append(int(digit))
        
            sum1 = 0
            for s in second_group:
                sum1 += int(s)
           
            sum1 *= 3
        
            sum2 = 0
        
            for s in first_group:
                sum2 += int(s)
        
            sum3 = sum2 + sum1
        
            last_digit = int(str(sum3)[-1])
            final_num = 10 - last_digit

        
        
            if final_num == int(barcode[12:13]):
                count += 1
                outfile.write(barcode + "\n")
print(f"There are {count} valid barcodes.")
        
        
outfile.close()   
        
        
        
        
            
            
    





