#For Image
x_lines = ' --- '
y_lines = '| {} |'

# Making and Displaying board
def board_dim(size):
    global game_board
    game_board = [[0 for _ in range(size)] for _ in range(size)]

    for row in game_board:
        print(x_lines * size)
        print(''.join(y_lines.format(cell) for cell in row))
        print(x_lines * size)

    return game_board

# Assigning Player
def assign_player():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1 choose X or O: ")
    
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

# Function to check for a winner
def check_winner(row, player1, player2):
    if len(set(row)) == 1:
        if row[0] == player1:
            return "Player 1 wins"
        elif row[0] == player2:
            return "Player 2 wins"
    return "No Winner"

# Playing the game
def playing(player1, player2):
    count = 0
    if player1 == 'X':
        who_is_x = player1
        who_is_y = player2
        current_player = "Player 1"

    else:
        who_is_x = player2
        who_is_y = player1
        current_player = "Player 2"

    while count < 9:
        if count % 2 == 0:
            current_marker = who_is_x
        else:
            current_marker = who_is_y
            current_player = "Player 2"

        coord = input(f"{current_player}, it's your turn. Enter coords as row,col: ").strip().split(',')
        mark = [int(x) for x in coord]
        r = mark[0]
        c = mark[1]

        if game_board[r-1][c-1] == 0 and count % 2 == 0:
            game_board[r-1][c-1] = who_is_x
            print_board(game_board)
            
        elif game_board[r-1][c-1] == 0 and count % 2 != 0:
            game_board[r-1][c-1] = who_is_y
            print_board(game_board)

        else:
            print("Invalid Position")
            print_board(game_board)
            continue
        
        count += 1
        print(f'Turn:{count}')

        # Check for a winner
        top_row = game_board[0]
        mid_row = game_board[1]
        bot_row = game_board[2]

        # Check row
        row_winner = check_winner(top_row, player1, player2) or check_winner(mid_row, player1, player2) or check_winner(bot_row, player1, player2)
        if row_winner != "No Winner":
            print("We have a winner!")
            print(row_winner)
            return

        # Check column
        grid = len(game_board)
        for i in range(grid):
            column = [top_row[i], mid_row[i], bot_row[i]]
            column_winner = check_winner(column, player1, player2)
            if column_winner != "No Winner":
                print("We have a winner!")
                print(column_winner)
                return

        # Check diagonal
        if top_row[0] == mid_row[1] == bot_row[2]:
            diagonal_winner = check_winner([top_row[0], mid_row[1], bot_row[2]], player1, player2)
        elif top_row[2] == mid_row[1] == bot_row[0]:
            diagonal_winner = check_winner([top_row[2], mid_row[1], bot_row[0]], player1, player2)
        else:
            diagonal_winner = "No Winner"

        if diagonal_winner != "No Winner":
            print("We have a winner!")
            print(diagonal_winner)
            return

    print("Game Over")

def print_board(game_board):
    size = len(game_board)
    for row in game_board:
        print(x_lines * size)
        print(''.join(y_lines.format(cell) for cell in row))
        print(x_lines * size)

grid = int(input("What size game board do you want (enter the size of the square grid): "))
game_board = board_dim(grid)
player1, player2 = assign_player()
playing(player1, player2)

# Re-display the board
print_board(game_board)