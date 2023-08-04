#Ask user for number
#Print out list of all divisors of that number

num = int(input("Enter a number: "))
divisors = []

for value in range(1,num+1):
    if num % value == 0:
        divisors.append(value)
print(divisors)

'''
Potential Improvements:
-make modular by encapsulating in function
'''