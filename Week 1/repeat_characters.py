#accepts string
#return with each character from original string doubled
    #"now" -> "nnooww"
    #"123a!" -> "112233aa!!"

def doubler():
    provided = str(input("Please provide string: "))
    imp_list = list(provided)
    n = 2
    dub_list = ''.join(char * n for char in imp_list)

    print(imp_list)
    print(dub_list)    

    pass

doubler()