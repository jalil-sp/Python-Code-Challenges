#Part 2 of birtday data exercise
#Modify code from part 1 to load the birthday dictionary from a JSON file on disk
#What needs to be done:
#load JSON file
#function to 
#function for viewing names
#function for asking for name to show bday
#BONUS
    #ask for name and birthday to add to dictionary
    #update JSON file
import json 

bdays = {}
with open("bday.json","r") as file:
    bdays = json.load(file)


#function for viewing names
def viewing():
    for names in bdays:
        print(names.capitalize())

#function for asking for name to show bday
def asking():
    while True:
        input_name = input("Who's birthday would you like to know?\n").lower()
        if input_name in bdays:
            print(f"{input_name.capitalize()}'s birthday is", bdays[input_name])
            break
        else:
            print("That name is not known. Try again")

#function for adding names and bdays
def adding():
    while True:
        new_name = input("What is the name that you would like to add\n").lower()
        if new_name not in bdays:
            new_bday = input("What is their birthday? Format as mm/dd/yyyy.\n")
            break
        else:
            print("That name is already present, try again")
    with open("bday.json","w") as file:
        bdays[new_name] = new_bday
        file.seek(0)
        json.dump(bdays,file)
        file.truncate()
'''
with open("bday.json", "r") as file:
    updated_data = json.load(file)

# Print the updated data
print(updated_data)
'''

print("Welcome")
while True:
    task = input("What would you like to do: 'view','add','ask', or 'quit'?\n").lower()
    if task == 'view':
        viewing()
    elif task == 'add':
        adding()
    elif task == 'ask':
        asking()
    if task == 'quit':
        print("Goodbye")
        raise SystemExit(0)

'''
Potential Improvements:

'''