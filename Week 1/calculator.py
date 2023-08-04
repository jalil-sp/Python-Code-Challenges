#accepts 3 parameters
    #first parameter is integer
    #second parameter one of following math operators: +,-,/,* (add,subtract,divide,multiply)
    #third parameter is integer
def calc(num1,operator,num2):
    #while loop for number input
    while True:
        try:
            #if both numbers are integers break out of while loop
            num1 = int(input("First Number: "))
            num2 = int(input("Second Number: "))
            break
        #if not integer notify and start loop over
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

    #while loop to for operator input
    while True:
        #ask for operator
        operator = input("Enter an operator('+','-','/','*'): ")
        #do math based on operator, once math is done break out of while loop
        if operator == '+':
            calculation = (num1 + num2)
            break
        elif operator == '-':
            calculation = (num1 - num2)
            break 
        elif operator == '/':
            calculation = (num1 / num2)
            break  
        elif operator == '*':
            calculation = (num1 * num2)
            break
        else:
            #if not acceptable output notify and start loop over
            print(f"{operator} is not a valid operator")        
            continue

    #print results
    print("Calculation:",calculation)

#initializing parameters to allow function to run and prompt for user input 
num1 = None
num2 = None
operator = None

calc(num1,operator,num2)

'''
#version that accepts parameter and includes input validation:

def calc(num1, operator, num2):
    # Check for valid number inputs
    # if num1 is not an instance of float or int OR if num2 is not an instance of float or int
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Invalid input, please enter a number.")
        return

    # Check for valid operator input
    if operator not in ['+', '-', '/', '*']:
        print("Invalid operator, please enter a valid operator ('+', '-', '/', '*').")
        return

    # Perform calculation based on operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = num1 * num2

    print("Result:", result)

#example function call
calc(5,'+',4)
'''