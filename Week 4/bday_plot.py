#Part 4 of 4 of the birthday data exercise
#Use bokeh library to plot histogram of birthday months in json file
#What has to be done:
    #Load data
        #load into 2 seperate list for x and y axis
    #Display data

#Basic Format:
# need to import at least 3 things to make your bokeh plots work
'''from bokeh.plotting import figure, show, output_file

# we specify an HTML file where the output will go
output_file("plot.html")

# load our x and y data
x = [10, 20, 30]
y = [4, 5, 6]

# create a figure
p = figure()

# create a histogram
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)'''

#Since we are dealing with months (a categorical variable)...
#to draw axis correctly we need to specify a special call to figure() to pass an x_range

import json
import calendar
import math
from collections import Counter
from bokeh.plotting import figure, show, output_file

#we specify an HTML file where the output will go
output_file("bday_plot.html")

with open("bday.json","r") as file:
        birthdays = json.load(file)

#takings the months from the birthday dictionary and storing in list
months = []
for i in list(birthdays.values()):
    months.append(int(i[:2]))

#converting the numerical months into the calendar months and putting in list
calendar_months = [calendar.month_name[month] for month in months]
#print(calendar_months)

#counted the occurances of the objects(months) in the calender_months list
counted = Counter(calendar_months)

#x-axis labels
all_months = [month for month in calendar.month_name][1:]
#x axis labels with a y-value
ordered_months = [month for month in calendar.month_name if month in calendar_months]

#y-values
y_val = []
for month in ordered_months:
      y_val.append(counted[month])

#dont change for now
p = figure(x_range=all_months)
p.xaxis.major_label_orientation = math.pi/4
p.vbar(x=ordered_months, top=y_val, width=0.5)

show(p)