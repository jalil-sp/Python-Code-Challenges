#accepts string containing any type and number of characters
#counts number of Xs and Os 
    #would be nice to see count
#checks if number of Xs equals number of Os
#return boolean value of either True or False

def compare():
    #ask for input
    string = input("Please enter a string: ").lower()
    #unpacking input into list of elements
    string_char = [*string]

    #count number of 'o' in string
    o_count = string_char.count('o')
    #count number of 'x' in string    
    x_count = string_char.count('x')
    #print results
    print("Number of Os: ", o_count)
    print("Number of Xs: ", x_count)
    print("The number of Os match the number of Xs:",o_count == x_count)
#call function
compare()