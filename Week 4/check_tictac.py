#Check if there is winner with tictactoe
#Determine which player is the winner
#represent game as lists of list

#no winner check
#game = [[1, 2, 0],[2, 1, 2],[1, 1, 2]]
#row winner check
#game = [[2, 2, 2],[2, 1, 1],[1, 1, 2]]
#column winner check
#game = [[1, 2, 0],[0, 2, 2],[1, 1, 2]]
#diagonal winner check
game = [[2, 1, 1],[2, 2, 1],[1, 1, 2]]

top_row = game[0]
mid_row = game[1]
bot_row = game[2]

#win if 3 in a row - either in a row, column, or diagonal

def check_winner(row):
    if len(set(row)) == 1:
        if row[0] == 1:
            return "Player 1 wins"
        elif row[0] == 2:
            return "Player 2 wins"
    return "No Winner"

#row
row_winner = check_winner(top_row) or check_winner(mid_row) or check_winner(bot_row)

if row_winner != "No Winner":
    print("We have a winner!")
    print(row_winner)
else:
    #column
    for i in range(3):
        column = [top_row[i], mid_row[i], bot_row[i]]
        column_winner = check_winner(column)
        if column_winner != "No Winner":
            print(column_winner)
            break
    else:
        #diagonal
        if top_row[0] == mid_row[1] == bot_row[2]:
            diagonal_winner = check_winner([top_row[0], mid_row[1], bot_row[2]])
        elif top_row[2] == mid_row[1] == bot_row[0]:
            diagonal_winner = check_winner([top_row[2], mid_row[1], bot_row[0]])
        else:
            diagonal_winner = "No Winner"
        
        if diagonal_winner != "No Winner":
            print("We have a winner!")
            print(diagonal_winner)
        else:
            print("No Winner")
