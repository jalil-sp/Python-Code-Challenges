#Given a .txt file
#Count how many names in file 
#Print results 


counter = {} #intitalize a dictionary for names
with open(r'C:\Users\14046\Desktop\Python Code Challenges\Week 2\nameslist.txt') as file: #open and read file
    line = file.readline() #read line if there is not text sets line == False
    while line: #while there is text on a line
        line = line.strip() #remove the whitespace and return name
        if line in counter: #checks if returned name is already in counter
            counter[line]+= 1 #if it is add to count of that name
        else:
            counter[line] = 1 #if name is not in counter start the count 
        line = file.readline() #go to next line

print(counter) #print dictionary

