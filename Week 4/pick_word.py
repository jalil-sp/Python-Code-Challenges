#function that picks random word from a list of words from the SOWPODS dictionary
#download file
#save file in same directory as code

import random

#word_list = [] #intitalize a dictionary for words
with open(r'C:\Users\14046\Desktop\Python Code Challenges\Week 4\sowpods.txt') as file: #open and read file
    word_list = [word for word in file]
print(f' The word is {random.choice(word_list)}')
    #for line in file:
        #line = line.strip()
        #word_list.append(line)
#rando = random.choice(word_list)
#print(rando)

'''
Potential Improvements:
- Make into mutable function
'''