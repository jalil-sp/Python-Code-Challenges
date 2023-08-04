#accepts two parameters
    #first parameter is reg price of item
    #second parameter is discount percentage
#return discounted price

def discounter(reg_cost,percent_off):
    if not isinstance(reg_cost,(int, float)) or not isinstance(percent_off,(int,float)):
        print("Invalid input. Please try again")
        return
    else:
        dis_cost = (1-(percent_off/100)) * reg_cost 
        
    print("Original Price:", reg_cost)
    print("Discounted Price:", dis_cost)
    print(type(reg_cost))

discounter(float(input("Original Price: ")),float(input("Percent off: ")))


'''
Potential Improvements:
-Be able to accept input as 2/2.00 or $2/$2.00
-Be able to accept input as 20 or 20%
-print float with $directly in front

'''