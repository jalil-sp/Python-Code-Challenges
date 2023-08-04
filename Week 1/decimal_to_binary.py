#accepts decimal number
    #will always be less than 1024
#returns equivalent binary number
    #will always be less than ten digits
'''
Successive Division Method:
    Dividing by 2 down to 0 and remainders indicate 1 or 0 for bin conversion.
    Read from bottom up, i.e last division to first division.
'''

def dec_to_bin():
    #input for decimal number
    try:
        dec_num = (int(input("What decimal number would you like converted? ")))
    except ValueError:
        print("The provided value is not an integer")
    #empty list for binary
    bin_list = []
    #print Decimal Number for results
    print("Decimal Number:",dec_num)

    #while loop#check if whole number part of quotient is not 0
    while dec_num != 0:
        #mod to get remainder part
        bin_num = dec_num % 2
        #append to list
        bin_list.append(bin_num)
        #update with whole number part of quotient
        dec_num = dec_num//2
    #reverse list
    bin_list.reverse()
    #print Binary Equivalent for results
    print("Binary Equivalent: ",end='')
    for bin in bin_list:
        print(bin,end='')
 
#call function
dec_to_bin()