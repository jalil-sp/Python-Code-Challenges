#write function that takes 3 variables
#returns the largest of the three
#DO NOT USE max() function


def largest():
    a,b,c = map(int, input("Enter 3 numbers separated by a space: ").split())
    
    if a > b and a > c:
        print(a,"is the largest")
    elif b > a and b > c:
        print(b,"is the largest")
    elif c > a and c > b:
        print(c,"is the largest")
    
largest()

'''
Potential Improvements:
-Deal with 2 or more inputs being the same value

'''

