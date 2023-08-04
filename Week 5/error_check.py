#Add one level of error check to exercise 9 (Guessing Game 1)
#If user does not enter a number between 1-9 tell them
    #Don't count this guess against user


#Generate random number between 1-9 (including 1 and 9)
#Ask user to guess number
#Tell user if guess is too low, too high, or exactly right
#EXTRA:
    #Keep game going until user types "exit"
    #Keep track of number of guesses and print when game ends

import random

test = random.randint(1,9)
print(test)

count = 0

while True:
    user_input = input("Guess a number between 1 and 9 or type exit: ")
    
    if user_input == "exit":
        break 
    if user_input.isdigit(): 
        guess = int(user_input)
        if guess in range(1,10):
            if guess < test:
                print("Your guess is too low")
            elif guess > test:
                print("Your guess is too high")
            else:
                print(f"You guessed right! {test} was the number.")
                break
            count += 1
        else:
            print("Please choose number between 1-9")
    else:
        print("That is not a number")

if user_input != 'exit':
    print(f"You guessed it in {count+1} tries.")