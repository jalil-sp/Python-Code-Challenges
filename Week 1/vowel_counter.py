#accepts a single word string
#returns number of vowels
    #vowels: ['a','e','i','o','u']

def counter():
    vowels = ['a','e','i','o','u']

    word = input("Enter a word: ").lower()
    #split string using unpack method
    ind_char = [*word]

    #checking if each letter in ind_char list matches one of letters in vowels list
    #if there is a match the vowel_count increases
    vowel_count = sum(item in ind_char for item in vowels)

    print("Vowel Count: ", vowel_count)


counter()
