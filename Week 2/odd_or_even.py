#ask user input for number
#print out different message 

user_input = int(input("Please provide a number: "))

def divisible(number):
    if number % 2 == 0:
        print("That's an even number!")
    else:
        print("That's an odd number!")
    
divisible(user_input)

'''
Potential Improvements:
-Check to make sure number input is actual integer
-If number is multiple of 4, print out a different message
-Ask user for two numbers:  
    -one number to check (call it num)
    -one number to divide by (check)
    #If check divides evenly into num, tell that to user
    #If not, print a different appropriate message

'''