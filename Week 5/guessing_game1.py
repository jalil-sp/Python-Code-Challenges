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
    user_input = input("Guess a number or type exit: ")
    
    if user_input == "exit":
        break 

    guess = int(user_input)

    if guess < test:
        print("Your guess is too low")
    elif guess > test:
        print("Your guess is too high")
    else:
        print(f"You guessed right! {test} was the number.")
        break
    count += 1

if user_input != 'exit':
    print(f"You guessed it in {count+1} tries.")