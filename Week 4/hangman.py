#Hangman Part 3
#Only let the user guess 6 times, and tell the user how many guesses they have left
#Keep track of the letters the user guessed.
#If the user guesses a letter they already guessed, don’t penalize them - let them guess again


import random

def pick_word():
    with open(r'C:\Users\14046\Desktop\Python Code Challenges\Week 4\sowpods.txt') as file: #open and read file
        word_list = [word for word in file]
        random_word = random.choice(word_list).strip()
    print("The word has been set")
    return random_word

choosen_word = pick_word()
print(choosen_word)

def guessing(word):

    blank = '_'
    guess_nbr = 1
    guess_remaining = 5 
    show = [blank for char in word]
    print("Welcome to Hangman!")
    print(' '.join(show))

    guesses = []

    while '_' in show and guess_nbr < 7:
        print("This is turn", guess_nbr, "you have", guess_remaining, "guesses remaining")
        user_guess = input("Guess your letter: ")
        if user_guess in guesses:
            print("You've already guessed that, try again :(")
            continue

        guesses.append(user_guess)

        if user_guess in word:
            guess_nbr += 1
            guess_remaining -= 1
            print("Correct, this is a letter in the word!")
            for i in range(len(word)):
                if word[i] == user_guess:
                    show[i] = user_guess
        else:
            guess_nbr += 1
            guess_remaining -= 1
            if guess_nbr == 7:
                print("You lose")
            else:
                print("Try again")

        print(' '.join(show))

    if '_' not in show:
        print("You win!")

guessing(choosen_word)

'''
Potential Improvements:
- Check if choosen word can be guessed in 6 tries, if not pick a new word
- Make sure user guess is actually a letter
- Make sure if user puts lower case letter it recognizes it
'''