#accepts credit card num(16 digits)
#return num with all character as asterisks except for last four
    #1234 5678 8900 5100 -> **** **** **** 5100

def card_num_encrpyt():
    #while loop to keep asking until given correct input
    while True:
        #input (should be string)
        raw_num = (input("Please give 16 digit card number(only numbers): "))
        num_count = len(raw_num)
        hidden = '************'

        #check if input in correct format
        if raw_num.isdigit():
            #checks if input is exactly 16 digits
            if num_count != 16:
                print("Please enter exactly 16 digits.")
                #redo while loop
                continue
            else:
                #hides first 12 digits
                updated_raw_num = raw_num.replace(raw_num[0:12],hidden)
                #creates list without brackets, '', and ,
                encrypted = ' '.join([updated_raw_num[i:i+4] for i in range(0,len(updated_raw_num),4)])
                break
        else:
            print("That is not an acceptable format, please try again.")
            #redo while loop
            continue
    
    print(encrypted)
card_num_encrpyt()