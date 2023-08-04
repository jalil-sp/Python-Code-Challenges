import datetime

def smart_decade():
    name_input = input("What is your name? ")
    age_input = int(input("How old are you? "))

    today = datetime.date.today()
    year = today.year

    calc_year = (100-age_input) + year

    print(f"{name_input}, you'll turn 100 in {calc_year}")

smart_decade()
#print(today)
#print(year)
#print(type(year))

