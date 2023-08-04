def board_dim(size):
    x_lines = ' --- '
    y_lines = '|   |'

    for i in range(size):
        print(x_lines * size)
        print(y_lines * size)
        print(x_lines * size)

grid = int(input("What size game board do you want(enter first number of square grid): "))
board_dim(grid)

'''
Potential Improvements:
-Be able to print not square grid
'''