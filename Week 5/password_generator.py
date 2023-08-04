#Write a password generator
#Mix of lowercase, uppercase, numbers, and symbols
#Generate new password everythime user asks for new password
#Include run-time code in a main method
#EXTRA
    #Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list

#import needed modules
import string
import random

#define different list
all_letters = string.ascii_letters
all_numbers = string.digits
all_symbols = string.punctuation
easy_words = ['cat','dog','mouse','house','password']

full_list = all_letters + all_numbers + all_symbols
easy_list = all_numbers + all_symbols

password = ''
if __name__ == "__main__":
    while True:
        new_password = input("Would you like a password? Enter 'yes' or 'no': ")
        if new_password == 'no':
            print("Goodbye")
            break
        elif new_password =='yes':
            pass_strength = input("Do you want a 'weak' or 'strong' password? ")
            #weak password: random word with a mix of numbers and symbols
            if pass_strength == 'weak':
                password += random.choice(easy_words) + ''.join(random.choice(easy_list))
            #strong password: random choice of lowercase,uppercase, numbers and symbols
            elif pass_strength == 'strong':
                pass_length = int(input("How long would you like your password: "))
                for i in range(pass_length):
                    password += ''.join(random.choice(full_list))
            else:
                print("Invalid input. Please try again")
                continue
        else:
            print("Invalid input. Please try again")
            continue
print(f"Your password is: {password}")


'''
Potential Improvements:
- seperate weak and strong password generators into separate function
- use list comprehension for strong password generating
'''