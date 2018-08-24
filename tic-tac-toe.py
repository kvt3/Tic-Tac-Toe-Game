rowCnt = [0,0,0]
colCnt = [0,0,0]
diagonalCnt = 0
antidiagonalCnt = 0
player = ''


'''''
* This function will return all the possible valid moves
  of given instance of board otherwise it will return
  empty list of moves
'''
def get_moves(board):
    rowNum = 0
    moves = set()

    for i, cell in enumerate(board):
        if i > 0 and i % 3 == 0:
            rowNum += 1

        if cell is None:
            move = (rowNum, i%3)
            moves.add(move)

    return moves


'''''
* move is apply on board
'''
def do_move(board, move):
    board[3*move[0] + move[1]] = player
    return validate_move(move)


'''''
This function will print the visual board
'''
def print_board(board):
    print('-----------')

    for i, cell in enumerate(board, 1):
        if cell is None:
            cell = ' '

        print(cell, end=' | ', flush=True)

        if i%3 == 0:
            print()
            print('-----------')


'''''
* Function checks, which player won the game
* and board is valid for the next move or not
'''

def validate_move(move):
    global rowCnt
    global colCnt
    global diagonalCnt
    global antidiagonalCnt

    row = move[0]
    col = move[1]
    diagonal = 3*move[0] + move[1]

    n = 1 if player == 'X' else -1

    rowCnt[row] += n
    colCnt[col] += n

    if diagonal in (0,4,8):
        diagonalCnt += n
    if diagonal in (2,4,6):
        antidiagonalCnt += n

    if (abs(rowCnt[row]) == 3 or abs(colCnt[col]) == 3 or
        abs(diagonalCnt) == 3 or abs(antidiagonalCnt) == 3):
            print("\n")
            print("Game Over! player {0} has Won".format(player))
            return False

    return True
'''
This function will take valid input form user
'''

def valid_player():
    global player
    valInput = False

    while not valInput:
        try:
            player = input("Start with player 'X or 'O' ?: ")

            if player not in ('X', 'O'):
                print("Provide Valid Input")
            else:
                valInput = True

        except Exception as e:
            print(e)


'''
This function will take valid input form user
'''
def valid_input_move(moves):
    validInput = False

    while not validInput:
        try:
            x, y = input("{0} Player Enter Move (row, col): ".format(player)).split()

            move = (int(x), int(y))
            if move not in moves:
                print("Invalid move! Provide valid move")
            else:
                validInput = True
        except Exception as e:
            print(e)

    return move

'''
Start Game
'''
if __name__ == '__main__':
    board = [None,None,None,None,None,None,None,None,None]
    valid_player()
    print_board(board)
    moves = get_moves(board)

    valid = True
    while(valid) :
        print("remaining moves",moves)
        move = valid_input_move(moves)
        valid = do_move(board,move)
        moves.remove(move)
        if (len(moves) == 0 and valid):
            print("\n")
            print("Game Over! It's a draw")
            valid = False
        print_board(board)
        player = 'O' if player == 'X' else 'X'