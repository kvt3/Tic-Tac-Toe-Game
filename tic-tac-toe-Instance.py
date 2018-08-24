import random

'''''
* This function will return all the possible valid moves
  of given instance of board otherwise it will return
  empty list of moves
'''
def get_moves(board):
    rowNum = 0
    moves = []
    player = []
    valid, choosePlay = validate_board(board)

    if(choosePlay == 0):
        player.append('X')
        player.append('O')
    else:
        player.append('O' if choosePlay == 1 else 'X')

    if (valid):
        for i,x in enumerate(board):
            if i > 0 and i % 3 == 0:
                rowNum += 1

            if (x == None):
                for currPlayer in player:
                    move = (rowNum, i%3, currPlayer)
                    moves.append(move)

    return moves

'''''
* If move is invalid, function will return unmodified board
  else it will apply move and return board
'''

def do_move(board, move):
    moves = get_moves(board)
    if move not in moves:
        print("Invalid move! Give valid move")
        return board
    board[3 * move[0] + move[1]] = move[2]
    return board


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
* Function checks whether current board is valid for next move or not
* input : board
* output: boolean, nextPlayer
* function will return False,0 if one of the player won the game
    or board is not in valid state
'''
def validate_board(board):
    rowCnt = [0, 0, 0]
    colCnt = [0, 0, 0]
    diagonalCnt = 0
    antidiagonalCnt = 0

    n = 0
    rowNum = 0
    player = 0
    map = {'X': 1, 'O': -1}

    for i, x in enumerate(board):
        if i > 0  and i % 3 == 0:
            rowNum += 1

        n = map.get(x, 0)

        player += n
        rowCnt[rowNum] += n
        colCnt[i%3] += n
        if i in (0,4,8):
            diagonalCnt += n
        if i in (2,4,6):
            antidiagonalCnt += n

        if(abs(rowCnt[rowNum]) == 3 or abs(colCnt[i%3]) == 3 or
            abs(diagonalCnt) == 3 or abs(antidiagonalCnt) == 3):
            print("Player {0} has won the game".format(x))
            return False,0

    if abs(player) > 1:
        print("Invalid board")
        return False,0

    return True,player


'''''
main function for testing
'''

'''''
if __name__ == '__main__':
    board = [None, None, 'X', None, 'O', None, None, 'O', None]
    for i in range(10):
        print_board(board)
        moves = get_moves(board)
        print(moves)
        if len(moves) == 0:
            print("No More Valid Moves")
            break
        move = moves[random.randint(0, len(moves)-1)]
        board = do_move(board,move)
'''