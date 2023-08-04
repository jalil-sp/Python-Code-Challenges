#Part 3 of 4 of birthday data exercise
#load JSON file fom disk
#extract all birthday months 
#count how many names have a birthday in each month extracted

import json
import calendar
from collections import Counter

with open("bday.json","r") as file:
        birthdays = json.load(file)

#takings the months from the birthday dictionary and storing in list
months = []
for i in list(birthdays.values()):
    months.append(int(i[:2]))

#converting the numerical months into the calendar months and putting in list
calendar_months = [calendar.month_name[month] for month in months]

#counted the occurances of the objects(months) in the calender_months list
counted = Counter(calendar_months)

#creating list of the months from the calendar_months variable in the order that they appear in a calendar
ordered_months = [month for month in calendar.month_name if month in calendar_months]

#print the months in order with their counts of occurance
for month in ordered_months:
      print(f"{month}: {counted[month]}")