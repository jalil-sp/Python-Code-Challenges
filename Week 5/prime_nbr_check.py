#Ask for a number from user
#Determine if number is prime or not

#Optimized Iteration
#Improvements:
    #increased modularity in function
    #better input validation, letting user know invalid input
    #optimized divisilibity check

def check_prime(user_nbr):
    if user_nbr < 2:
        return False
    
    #optimized, only checking up to square root
    for value in range(2,(user_nbr ** 0.5)+1):
        if user_nbr % value == 0:
            return False 
        
    return True
        
while True:
    try:
        num = int(input("Enter a number: "))
        if check_prime(num):
            print(f'{num} is a prime number') 
        else:
            print(f'{num} is not a prime number')
        break
    except ValueError:
        print("Error: Invalid input. Try again")


#First Iteration:
'''
def check_prime(user_nbr):
    divisors = []
    for value in range(1,user_nbr+1):
        if user_nbr % value == 0:
            divisors.append(value) 
    
    if len(divisors) == 2:
        print(f'{user_nbr} is a prime number')
    else:
        print(f'{user_nbr} is not a prime number')

while True:
    try:
        num = int(input("Enter a number: "))
        check_prime(num)
        break
    except ValueError:
        print("Error, try again")
'''