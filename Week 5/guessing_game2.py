#User has a mystery number between 1-100 in their head
#Program will try to guess number
#User will say if guess is too high,too low, or if the guess is correct
#Once number is guessed correct print out how many guesses it took

#Always guess the middle 
import math

lowest = 1
highest = 100
count = 1

#initial guess
guess = math.floor((lowest+highest)/2)

while True:
    user_input = (input(f"Is your guess {guess}? Enter 0 if guess is too low, 1 if guess is your number, 2 if guess is too high\n"))

    try:
        user_num = int(user_input)
        if user_num == 0:
            lowest = guess + 1
        elif user_num == 1:
            break
        elif user_num == 2:
            highest = guess - 1
        else:
            print("Invalid input, try again")
            continue 

        #new guess
        guess = math.floor((lowest+highest)/2)
        count += 1

    except ValueError:
        print("Invalid input, try again")

print(f"We guessed your number in {count} tries")