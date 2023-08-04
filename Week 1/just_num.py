#accepts list of any length that contains a mix of non-negative integers and strings
#return list with only integers from the original list in same order 

def only_nums():
    unedit = list(input("Provide Input: "))
    #print(unedit)
    #print(type(unedit))
    edited = []

    for i in unedit:
        if i.isdigit():
            edited.append(i)

    print("Numbers Appeared:",edited)
    #print(type(edited))

only_nums()