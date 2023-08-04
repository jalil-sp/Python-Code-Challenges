#take list
#return elements that are less than 5

'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([x for x in a if x < 5]) #One liner
'''

#Generate random list
#Ask user for number
#Return list smaller than input

import random

num_list = [random.randint(0,100) for i in range(10)]
print(num_list)

def less_than():
    num_input = int(input("Enter number 0-100: "))
    print([new_list for new_list in num_list if new_list < num_input])

less_than()


'''
Potential Improvements:
-make modular by encapsulating in function
- write in one line of code (DONE)
-don't print elements one by one, print in new list(DONE)
-ask user for number and return list of elements smaller than input
'''