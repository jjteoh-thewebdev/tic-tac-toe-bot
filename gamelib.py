from random import choice

# init game board
def initBoard():
    board = [' ', ' ',' ',' ',' ',' ',' ',' ',' ']

    return board


# check winner
# -1: not yet finish,
# 0: draw
# 1: O win
# 2: X win
def checkWinner(board):
    conditions = [[0,1,2], [3,4,5], [6,7,8],
                  [0,3,6], [1,4,7], [2,5,8],
                  [0,4,8], [2,4,6] ]
    
    for check in conditions:
        countO = 0
        countX = 0
        
        for hit in check:
            if board[hit] == 'O':
                countO += 1
            if board[hit] == 'X':
                countX += 1
        
        if countO == 3:
            return 1 # O won

        if countX == 3:
            return 2 # X won
        
    if ' ' not in board:
        return 0 # draw
    
    return -1 # not yet over



# display game board
def printBoard(board):
    output = ""
    i = 0

    for row in range(5):
        for col in range(5):
            if row % 2 != 0:
                output += "-"
            else:
                if col % 2 != 0:
                    output += "|"
                else:
                    output += board[i]
                    i += 1
        output += "\n"
    
    print(output)

# simulate the game
def simulateGame(verbose=False):
    board = initBoard()
    playerTurn = 'O'
    history = []

    while checkWinner(board) < 0:
        nextMove = choice([i for i,x in enumerate(board) if x == ' '])

        # next move
        board[nextMove] = 'O' if playerTurn == 'O' else 'X'
        # update history
        history.append((playerTurn, nextMove))
        # switch turn
        playerTurn = 'O' if playerTurn == 'X' else 'X'
        
        if verbose:
            print('Move ', len(history))
            printBoard(board)
            print('\n')

    result = checkWinner(board)

    if result == 1:
        print("Player O won!!!")
    elif result == 2:
        print("Player X won!!!")
    else:
        print("draw")
    
    return (history, result)

# show game stats
def stats(games):
    stats = {"O_Win": 0, "X_Win": 0, "Draw": 0}

    for game in games:
        result = game[1]
        if result == 0:
            stats["Draw"] += 1
        elif result == 1:
            stats["O_Win"] += 1
        else:
            stats["X_Win"] += 1
    
    totalGame = len(games)
    o_win_percent = stats["O_Win"] / totalGame * 100
    x_win_percent = stats["X_Win"] / totalGame * 100
    draw_percent = stats["Draw"] / totalGame * 100

    print(f"O wins: {stats['O_Win']} / {totalGame}, {o_win_percent:.2f}%" )
    print(f"X wins: {stats['X_Win']} / {totalGame}, {x_win_percent:.2f}%" )
    print(f"O wins: {stats['Draw']} / {totalGame}, {draw_percent:.2f}%")

# board = ['X','O','X','O','X','O','O','X','O']
# printBoard(board)
# print(checkWinner(board))

