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





# print(board)
# print_board(board)

def game_is_complete(board, turn):
    return False


def transform_location(location):
    """Takes board coordinates (eg. d2, c4) and transforms into matrix coordinates."""
    c, r = location

    c = ord(c) - 97
    r = int(r) - 1

    return (r, c)


def transform_letter_to_piece(letter):
    letter = letter.upper()
    number = letter_mapper[letter]

    return number


def transform_notation(notation):
    piece = transform_letter_to_piece(notation[0])

    start = notation[1:3]

    start = transform_location(start)

    is_capture = (notation[3] is 'x')

    if is_capture:
        end = notation[4:6]
    else:
        end = notation[3:5]

    end = transform_location(end)

    is_check = (notation[-1] is '+')

    return piece, start, end, is_capture, is_check


def init():
    """Initializes a new board and set the pieces.

    Returns:
        dict: an "object" that contains the turn and the board
    """

    # Initialization
    board = np.zeros(shape=(8, 8), dtype=np.int)

    board[0] = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
    board[1] = [PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN]

    board[7] = -board[0]
    board[6] = -board[1]

    turn = 1  # 1 or -1. 1 for white, -1 for black

    state = {
        "turn": turn,
        "board": board
    }

    return state


def move_piece(board, initial_pos, final_pos):
    new_board = np.array(board)

    piece = new_board[initial_pos[0]][initial_pos[1]]
    new_board[initial_pos[0]][initial_pos[1]] = 0

    new_board[final_pos[0]][final_pos[1]] = piece

    return new_board

def main():
    state = init()
    turn = state['turn']
    board = state['board']

    while not game_is_complete(board, turn):
        print_board(board)
        if turn == 1:
            print('White to move: ')
        else:
            print('Black to move: ')

        notation = input()

        piece, start, end, is_capture, is_check = transform_notation(notation)
        piece = turn * piece  # Set the color for this piece

        board = move_piece(board, start, end)


        turn = -turn


main()
