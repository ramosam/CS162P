def displayInstructions():
    print('\nThis is a game of Tic-Tac-Toe.')
    print('It requires two players, and player "X" gets to go first.')
    print('Please enter in the number of the square that you want to claim.\n')


def showBoard(board):
    print('The board is:\n')
    boardLayout = ''
    count = 0
    for square in board:
        boardLayout += '[' + square + ']'
        count += 1
        # Keep layout based on index
        if count in [3, 6, 9]:
            boardLayout += '\n'
    print(boardLayout)

def getMove(board, player_turn):
    valid_move = False
    current_player = ''
    player_symbol = ''
    # Determine if player is X or O, X is set as true.
    if player_turn:
        current_player = 'Player X'
        player_symbol = 'X'
    else:
        current_player = 'Player O'
        player_symbol = 'O'
    while(not valid_move):
        player_choice = input(current_player + ', choose a square. ')
        # Check for match
        if player_choice in board:
            # Exception: Cannot reclaim a square already owned
            if player_choice == 'X' or player_choice == 'O':
                print('That is not a valid move.')
            # Must be a valid option and can be claimed
            else:
                pos = board.index(player_choice)
                board[pos] = player_symbol
                valid_move = True
        # No match, try again.
        else:
            print('That is not a valid move.')
        
def checkWin(board):
    # Rows
    win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
    # Columns
    [0, 3, 6], [1, 4, 7], [2, 5, 8], \
    # Diagonals
    [0, 4, 8], [2, 4, 6]]
    for line in win_lines:
        symbol = board[line[0]]
        if symbol == board[line[1]] and symbol == board[line[2]]:
            print(symbol + ' is the winner!')
            return True
    return False

def checkDraw(board):
    for index in range(len(board)):
        # If there are any numbers still available
        if (board[index] != 'X' and board[index] != 'O'):
            return False
    # Board is filled up  
    print("It's a draw!")  
    return True

def playTurn(board, playerX_turn, game_over):
    getMove(board, playerX_turn)
    # Check for win
    if (checkWin(board)):
        game_over = True        
    showBoard(board)
    return game_over


def play_game(board, playerX_turn, game_over):
    showBoard(board)
    while (not game_over):
        # Player's turn, checks for win after each player turn
        if playTurn(board, playerX_turn, game_over):
            game_over = True
            continue
        # Check for draw
        if checkDraw(board):
            game_over = True
            continue
        playerX_turn = not playerX_turn

    if game_over:
        new_game = input("Would you like to play again? Y/y for a new game. Any other character to quit. ")
    if new_game.lower() == 'y':
        new_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        new_playerX_turn = True
        new_game_over = False
        play_game(new_board, new_playerX_turn, new_game_over)
    else:
        print("Until next time!")


board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
playerX_turn = True
game_over = False
displayInstructions()
play_game(board, playerX_turn, game_over)



    
