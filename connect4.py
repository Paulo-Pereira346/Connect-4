import numpy as np

class InputError(Exception):
    pass

def check_input(x):
    if(x < 0 or x > 6):
        raise InputError("Invalid Input!! Please Enter a Valid input")

def create_board():
    return np.zeros((6,7))

board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        try:
            selection = int(input("Player 1 Make your Selection (0-6): "))
            check_input(selection)
            print(selection)
        except InputError as e:
            print(e)
            continue
               
    else:
        try:
            selection = int(input("Player 2 Make your Selection (0-6): "))
            check_input(selection)
            print(selection)
        except InputError as e:
            print(e)
            continue
        
    turn = ( turn + 1)%2