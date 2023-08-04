#Ask user for string
#Print if string is palindrome or not

word = input("Give me a word: ")
#print(type(word))
#print(word[::-1].lower())
#print(word == word[::-1])
def palindrome(word):
    if word.lower() == word[::-1].lower():
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
palindrome(word)
