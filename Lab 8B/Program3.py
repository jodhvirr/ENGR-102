# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 8B
# Date:         17 October 2026


# define the variables
login_dict = {}
usernames = []
passwords = []

# ask how many pairs of username/password there are
num = int(input("How many username/password pairs are there?: "))

# Read in original list of usernames/passwords.
for i in range(num):
    usernames.append(input("What is the username?: "))

for i in range(num):
    passwords.append(input("What is the password?: "))    
    
# Store pairs in a dictionary.
for i in range(num):
    login_dict[usernames[i]] = passwords[i]


# Loop asking the user to enter until the correct pair entered.
running = True
print()
print("Log-In Page:")
while running:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    # Correctly checking whether a user’s username/password combination is correct.
    for key, value in login_dict.items():
        if key == username and value == password:
            # Output to the user as specified
            print("You are allowed in the system!")
            running = False
            break
    else:
        # Output to the user as specified
        print("The username/password is incorrect. Try again.")



