# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jodhvir Singh
#               Chase Sims
#               Rayyan Dulvi
#               Vraj Desai
# Section:      550
# Assignment:   Lab 8A
# Date:         20 October 2026


time = input("What is the time?: ")

digits = list(time)

patterns = { 
           "0": ["000", "0 0", "0 0", "0 0", "000"],
           "1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
           "2": ["222", "  2", "222", "2  ", "222"],
           "3": [" 3 ", "333", "3  ", "  3", "333"],
           "4": ["444", "444", " 4 ", "44 ", "444"],
           "5": ["555", "5  ", "555", "  5", "555"],
           "6": ["666", "6  ", "666", "6 6", "666"],
           "7": ["  7", "7  ", "777", "7  ", "  7"],
           "8": ["888", "88 ", " 88", " 8 ", "88 "],
           "9": ["9 9", "999", "999", "999", "9 9"] 
    }

for rows in range(5):
    
    for num in digits:
        if num == ":":
            if rows == 1 or rows == 3:
                print(":", end = " ")
            else:
                print(" ", end = " ")
        
        else:
            print(patterns[num][rows], end = " ")
    print()
    




