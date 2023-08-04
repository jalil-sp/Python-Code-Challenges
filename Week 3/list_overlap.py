#Take two list
#return new list containing common elements(no duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap = []

for x in a:
    for y in b:
        if x == y and y not in overlap:
            overlap.append(y)

print(overlap)

'''
Potential Improvements:
-make modular by encapsulating in function
-randomly generate lists
-write in one line
'''