# ask player to guess a letter
# display letters in the clue word that were guessed correctly
# display different message if guess is wrong

given_word = 'EVAPORATE'

def guessing(word):

    blank = '_'

    show = [blank for char in word]
    print("Welcome to Hangman!")
    print(' '.join(show))

    guesses = []

    while '_' in show:
        user_guess = input("Guess your letter: ")
        if user_guess in guesses:
            print("You've already guessed that, try again :(")
            continue

        guesses.append(user_guess)

        if user_guess in word:
            print("Correct, this is a letter in the word!")
            for i in range(len(word)):
                if word[i] == user_guess:
                    show[i] = user_guess
        else:
            print("Try again")

        print(' '.join(show))
    print("You've won,Congrats!")
guessing(given_word)