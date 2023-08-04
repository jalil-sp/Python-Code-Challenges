
user_input = int(input("How many Fibonnaci numbers to generate: "))
#print(range(user_input))
def fibonnaci(num):
    fib=[]
    for i in range(num):
        if i < 2:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    print(fib)

fibonnaci(user_input)
