# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 10Bonus
# Date:         3 November 2026


from math import *

def count_sets(num):
    count = 0
    
    for a in range(0, int(sqrt(num)) + 1):
        for b in range(a, int(sqrt(num)) + 1):
            for c in range(b, int(sqrt(num)) + 1):
                rest = num - a ** 2 - b **2 - c ** 2
                if rest < 0:
                    break
                else:
                    d = int(sqrt(rest))
                    
                    if d ** 2 == rest and d >= c:
                        count += 1
    
    return count



print(count_sets(10))
                
                
        
    
    
