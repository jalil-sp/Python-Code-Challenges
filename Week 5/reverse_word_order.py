#Ask for string
#Reverse the word order

def reversal(given):
    separation = given.split(" ")
    reverse_word = ' '.join(separation[::-1]) 
    return reverse_word

word = input("Give me a word and I'll reverse the word order: ")
reversed_word = reversal(word)
print(reversed_word)
