#takes list of numbers
#returns new list of only first and last element
#write inside function

from random import shuffle

def ends():
    A = [i for i in range(10)]
    shuffle(A)

    first = A[0]
    last = A[-1]
    Z = [first,last]

    print(A)
    print(Z)

ends()

'''
Potential Improvements:
-Ask user for size of first list

'''