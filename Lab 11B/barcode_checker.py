# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 11B
# Date:         5 November 2026




f = input("Enter the name of the file: ")


with open(f) as file:  
    for line in file:
        barcode = file.readLine()
        first_group = []
        second_group = []
        
        for digit in barcode[::2]:
            number = int(digit)
            first_group.append(number)
        
        for digit in barcode[1::2]:
            number = int(digit)
            second_group.append(number)
        
        sum1 = 0
        for s in second_group:
           sum1 += int(s)
           
        sum1 *= 3
        
        sum2 = 0
        
        for s in first_group:
            sum2 += int(s)
        
        sum3 = sum2 + sum1
        final_num = sum3 - 10
        
        count = 0
        if final_num == int(barcode[12:13]):
            count += 1
        
print(f"There are {count} valid barcodes.")
        
        
        
        
        
        
        
            
            
    





