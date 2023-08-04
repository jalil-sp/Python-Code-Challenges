#similar to char_input.py 
#ask user for name and age
#print out year they will turn 100
#use f string instead of + operator to print message

def decade():
    name_input = input("Please enter name: ")
    age_input = int(input("Enter your age: "))
    year = 2023

    calc_year = (100-age_input) + year

    print(f"{name_input}, you'll turn 100 in {calc_year}")

decade()