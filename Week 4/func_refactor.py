#Refactor code snippet from tictactoe using function
'''
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
'''
def horizontal(size):
    horizontal_line = " "
    for i in range(size):
        horizontal_line += "--- "
    return horizontal_line
#horizontal(4)

def vertical(size):
    vertical_line = "|"
    for i in range(size):
        vertical_line += '   |'
    return vertical_line
#vertical(4)

size = 4 
print(horizontal(size))
for i in range(size):
    print(vertical(size))
    print(horizontal(size))


