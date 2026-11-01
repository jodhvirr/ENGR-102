# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 10B
# Date:         31 October 2026



def guessCalc():
    actual_num = 27
    total_guesses = 1
    running = True
    
    while(running):
        guess = userInput()
        if guess == actual_num:
            print(f"You guessed it! It took you {total_guesses} guesses.")
            running = False
            
        elif guess > actual_num:
            print("Too high!")
            
        else:
            print("Too low!")
        total_guesses += 1


def userInput():
    
    prompt = "What is your guess? "
    running = True
    while running:
        try:
            guess = int(input(prompt))
            running = False
            return guess
        except ValueError:
            prompt = "Bad input! Try again: "
    

def main():
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    guessCalc()
    
    


main()