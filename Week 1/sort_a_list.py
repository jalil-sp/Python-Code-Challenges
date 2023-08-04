    #accepts 2 parameters
        #list of numbers
        #string that is one of following: 
            #(asc,desc,none)
            #asc - return list with nbrs in ascending
            #desc - return list w/ nbrs in descending
            #none - return orginal list

def sort_list(numbers, order):
    if order == "asc":
        return sorted(numbers)
    elif order == "desc":
        return sorted(numbers, reverse=True)
    else:
        return numbers

num_list = input("Enter a list of numbers separated by spaces: ")
numbers = [int(n) for n in num_list.split()]

order = input("Enter 'asc' to sort the list in ascending order, 'desc' to sort it in descending order, or 'none' to leave it unaltered: ")

sorted_numbers = sort_list(numbers, order)

print("Original list:", numbers)
print("Sorted list:", sorted_numbers)
