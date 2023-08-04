#function
#takes list
#return new list of all elements without duplicates
'''
#proof of concept
num = [1, 1, 4, 5, 6, 4, 3, 2, 10]
dup = []
print(num)

for i in num:
    if i not in dup:
        dup.append(i)
'''

input_list = [int(num) for num in input("Enter a list of numbers separated by space: ").split()]

def no_dups(given):
    dup = []
    for i in given:
        if i not in dup:
            dup.append(i)
    print(dup)

no_dups(input_list)