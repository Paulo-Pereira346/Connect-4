import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

class InputError(Exception):
    pass

def create_board():
    return np.zeros((6,7))
  
def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board,col):
    if(col < 0 or col > 6):
        raise InputError("Invalid Input!! Please Enter a Valid input")
    if(board[5][col] != 0):
        raise InputError("This Column is Full!! Please try Another Column")
    
    return True

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if(board[r][col] == 0):
            return r

def print_board(board):
    print(np.flip(board, 0))
            

board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        try:
            col = int(input("Player 1 Make your Selection (0-6): "))
            if is_valid_location(board,col):
                row = get_next_open_row(board,col)
                drop_piece(board,row,col,1)
                
        except InputError as e:
            print(e)
            continue
               
    else:
        try:
            col = int(input("Player 2 Make your Selection (0-6): "))
            if is_valid_location(board,col):
                row = get_next_open_row(board,col)
                drop_piece(board,row,col,2)
                
        except InputError as e:
            print(e)
            continue
    
    print_board(board)
    turn = (turn + 1) % 2

