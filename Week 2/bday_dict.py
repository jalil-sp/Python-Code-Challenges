#Part 1 of 4 of birthday data exercise
#Create dictionary of names and birthdays
##Display all keys
#Ask user to enter name
#Return their birthday


bdays = { 'jalil': '05/24/2000' , 'mom': '07/18/1971', 'dad': '11/10/1970', 'malik': '06/18/1996', 'talib': '11/27/2002', 'seth': '10/24/2007'}

def bday_finder():
    print("Welcome to the birthday dictionary. We know the birthday of: ")
    for names in bdays:
        print(names.capitalize())

    while True:
        input_name = input("Who's birthday do you want to look up? ").lower()
        if input_name == ' ' or input_name not in bdays:
            print("That is not a valid input. Please enter one of names above")
        else:
            break
    
    print(input_name.capitalize() +"'s birthday is", bdays[input_name])


bday_finder()


#Some of part 2 of 4
#writing JSON file
    #import json library
    #save dictionary to disk
import json

with open("bday.json","w") as file:
    json.dump(bdays,file)

