#two player rock paper scissors game
#ask for player input
#compare inputs
#print message congratulating winner
#ask if players want to start new game

def playing():
    hands = []
    options = ['rock','paper', 'scissors']

    #Player 1 input validation
    while True:
        player_1 = input("Player 1, choose rock, paper, or scissors:")
        if player_1 in options:
            hands.append(player_1)
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors")

    #Player 2 input validation
    while True:
        player_2 = input("Player 2, choose rock, paper, or scissors:")
        if player_2 in options:
            hands.append(player_2)
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors")

    #Determine winner
    if 'rock' in hands and 'scissors' in hands:
        winner = 'rock'
    elif 'scissors' in hands and 'paper' in hands:
        winner = 'scissors'
    elif 'paper' in hands and 'rock' in hands:
        winner = 'paper'
    else:
        winner = 'draw'

    #Display results
    if winner == player_1 and winner != 'draw':
        print("Player 1 wins!")
    elif winner == player_2 and winner != 'draw':
        print("Player 2 wins")
    elif winner == "draw":
        print("It's a draw")    

#ask about playing new game
while True:
    playing()
    next_move = input("Would you like to start a new game? (Y/N): ").capitalize()
    if next_move != 'Y':
        print("Goodbye")
        break
