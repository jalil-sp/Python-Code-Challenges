#Handling user input


player1 = 'X'
player2 = 'O'

print(player1,player2)

game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
#game = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print(game)
#print(game[0][2])
#print(game[2][2])
#Ask where user wants to put mark

count = 0
turn = 'player 1'

while count < 9:
    coord = input("Enter coords as row,col: ").strip().split(",")
    mark = [int(x) for x in coord]
    r = mark[0]
    c = mark[1]  
    if game[r-1][c-1] == 0 and count %2 == 0:
        game[r-1][c-1] = player1
        print(game)
        turn='player 2'
    elif game[r-1][c-1] == 0 and count %2 != 0:
        game[r-1][c-1] = player2
        print(game)
        turn='player 1'
    else:
        print("invalid position")
        print(game)
        continue
    count += 1
    print(count)


print("Game Over")
print(game)
