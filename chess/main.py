import numpy as np

## Declare constants
PAWN = 1
KNIGHT = 6
ROOK = 5
KING = 2
QUEEN = 3
BISHOP = 4

letter_mapper = {
    'P': 1,
    'K': 2,
    'Q': 3,
    'B': 4,
    'R': 5,
    'N': 6,
}


def print_board(board):
    """Flip and print the board in correct orientation."""
    b1 = np.flip(board, axis=0)

    print(b1)


# Initialization
board = np.zeros(shape=(8, 8), dtype=np.int)

board[0] = [5, 6, 4, 3, 2, 4, 6, 5]
board[1] = [1, 1, 1, 1, 1, 1, 1, 1]

board[7] = -board[0]
board[6] = -board[1]


turn = 1  # 1 or -1. 1 for white, -1 for black


# print(board)
# print_board(board)

def is_game_complete(board, turn):
    return False


def transform_notation(notation):
    """Takes board coordinates (eg. d2, c4) and transforms into matrix coordinates."""
    c, r = notation

    c = ord(c) - 97
    r = int(r) - 1

    return (r, c)


def transform_letter(x):
    number = letter_mapper[x]

    return number

while not is_game_complete(board, turn):
    print_board(board)
    if turn == 1:
        print('White to move: ')
    else:
        print('Black to move: ')

    notation = input()

    piece = turn * transform_letter(notation[0])

    start = notation[1:3]

    start = transform_notation(start)

    is_capture = (notation[3] is 'x')

    if is_capture:
        end = notation[4:6]
    else:
        end = notation[3:5]

    end = transform_notation(end)

    is_check = (notation[-1] is '+')

    print(piece, start, end, is_capture, is_check)

    turn = -turn

