#Randomly generatea a 4 digit number
#Ask user to guess a 4 digit number
#Every digit guess correctly (in the correct place) they have a "cow"
#Every digit guess correctly (in the wrong place) is a "bull"
#Once full 4 digit number guessed correctly, the game is over
#Keep track of number of guesses and display at end

import random

def comparing(known_nbr, user_nbr):
    cowbull = [0, 0]
    known_str = str(known_nbr)
    user_str = str(user_nbr)

    for i in range(len(known_str)):
        if known_str[i] == user_str[i]:
            cowbull[0] += 1
        else:
            cowbull[1] += 1
    return cowbull

if __name__ == "__main__":
    playing = True
    random_nbr = random.randint(1000, 9999)
    print(random_nbr)
    guesses = 0

    print("Let's play a game of Cowbull!")
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")

    while playing:
        user_guess = input("Enter a 4-digit number or type 'exit' to quit: ")

        if user_guess == "exit":
            break

        if user_guess.isdigit() and len(user_guess) == 4:
            print("That is a valid input")
            cowbull_count = comparing(random_nbr, user_guess)
            guesses += 1
            print(f"{cowbull_count[0]} cows, {cowbull_count[1]} bulls")
            
            if cowbull_count[0] == 4:
                playing = False
                print(f"You win the game after {guesses} tries! The number was {random_nbr}")
                break
        else:
            print("Invalid input, try again")