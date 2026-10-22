# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 8B
# Date:         17 October 2026


# Reading in word as a string.

running = True

while running:
    string = input("What is the word that you want to convert to pig latin? (Type stop if you are done): ")
    print()

    # Looping for words until “stop” reached.
    if string.lower() == "stop":
        running = False
        break
        
        
# Identifying the first letter as a vowel/consonant.
    if (string[0] in "aeiouy" or string[0] in "AEIOUY"):
        # Correctly adding “yay” for words starting with vowel.
        print(string + "yay")
        print()
    

# Correctly moving starting consonants to the end of the word and adding “ay” if starting
# with a consonant.
    else:
        for i in range(len(string)):
            if(string[i] in "aeiouy" or string[i] in "AEIOUY"):
                print(string[i:len(string)] + string[0:i] + "ay")
                print()
                break
    
    

    