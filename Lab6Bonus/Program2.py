# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 6Bonus
# Date:         11 October 2026

# make a boolean 

count = 0
# make a for loop from 2 - 100
for i in range(2, 101):
    isPrime = True
    # make a nested loop from 2 - the number in the for loop
    for j in range(2, i):
        # if i % j == 0, then its not prime
        if i % j == 0:
           isPrime = False
        
    if isPrime == True:
        print(i, "is prime")
        count += 1
    else:
        print(i, "is not prime")
        
 # print # of primes between 2 and 100
print("There are", count, "number of primes between 2 and 100")
            
