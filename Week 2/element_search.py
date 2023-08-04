#write function that checks if number is inside list
#function returns appropriate boolean 

import random

random_numbers = [random.randint(1,100) for i in range(10)]

#print(type(random_numbers))

def element_guess():
    num_guess = input("Guess a number between 1-100: ")
    print("Is your guess in the list?")
    if int(num_guess) in random_numbers:
        print(True)
    else:
        print(False)
    
element_guess()
print(random_numbers)  