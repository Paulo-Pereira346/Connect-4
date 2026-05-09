import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

class InputError(Exception):
    pass

def create_board():
    return np.zeros((ROW_COUNT,COLUMN_COUNT))
  
def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board,col):
    if(col < 0 or col > 6):
        raise InputError("Invalid Input!! Please Enter a Valid input")
    if(board[ROW_COUNT-1][col] != 0):
        raise InputError("This Column is Full!! Please try Another Column")
    
    return True

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if(board[r][col] == 0):
            return r

def print_board(board):
    print(np.flip(board, 0))
    
def winning_move(board,piece):
    #Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            
    #Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
            
    #Check for positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True   
    #Check for negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True  
            
            
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

                if winning_move(board, 1):
                    print("PLAYER 1 Wins!! Congrats!!!")
                    game_over = True
                
        except InputError as e:
            print(e)
            continue
               
    else:
        try:
            col = int(input("Player 2 Make your Selection (0-6): "))
            if is_valid_location(board,col):
                row = get_next_open_row(board,col)
                drop_piece(board,row,col,2)
                
                if winning_move(board, 2):
                    print("PLAYER 2 Wins!! Congrats!!!")
                    game_over = True
                
        except InputError as e:
            print(e)
            continue
    
    print_board(board)
    turn = (turn + 1) % 2

