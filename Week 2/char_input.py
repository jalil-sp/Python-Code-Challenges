#input:
    #name
    #age
#output:
    #print message addressed to user that tells them the year that they'll turn 100

name_input = input("What is your name? ")
age_input = int(input("How old are you? "))
current_year = 2023

def ageer(name,age):
    year = (100-age) + current_year
    print("Hello",name + "!", "You'll be turning 100 in", year)
    
ageer(name_input,age_input)

'''
Potential Improvements:
-Check to make sure age input is actual integer
-Ask user for another number and printing out THAT many copies of the message
-Print out THAT many copies of the previous message on separate lines

'''