from copy import copy
from time import sleep
from random import shuffle
import os
from players import CLIPlayer

END = 0
TEMPLATE = """
  _________________
 |     |     |     |
 |  (  |  é  |  "  |
 |_____|_____|_____|
 |     |     |     |
 |  @  |  &  |  ç  |
 |_____|_____|_____|
 |     |     |     |
 |  -  |  è  |  )  |
 |_____|_____|_____|
 """
    
    # î
    # | columns and rows identifiers.

TEMPLATE_LIST = ['(','é','"','@','&','ç','-','è',')']

BOARD = [' ', '1', '2', '3', '4', '5', '6', '7', '8'] # initial board

CONFIG = {
    'rows':3,
    'cols':3,
    'sir':'Undefined',
}


class TemplateTaquinPlayer :
    def __init__(self):
        pass    
    def help(self):
        return "move the space from source to destination"
    def move(self, board, config):
        return piece_to_move



player = CLIPlayer()

def clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def is_empty(case):
    """ return if a case is empty the board """
    if (case < 0):
        return False
    if (case >= len(BOARD)):
        return False
    if (BOARD[case] != ' '):
        return False
    return True

def draw():
    curr_BOARD = copy(TEMPLATE)
    for i in range(len(BOARD)):
        curr_BOARD = curr_BOARD.replace(TEMPLATE_LIST[i], BOARD[i])
    print("sir {} is playing. Do not disturb.".format(CONFIG['sir']))
    print(curr_BOARD)

def update():
    clear()
    draw()
    x = player.move(BOARD, CONFIG)
    if (is_valid(x)):
        space = BOARD.index(' ')
        new_space = BOARD.index(x)
        BOARD[space] , BOARD[new_space] = BOARD[new_space] , BOARD[space]
    else :
        END=-1

def setup():
    shuffle(BOARD)
    END = 0
    print("How should I call you fine sir?: ")
    no_name = True
    while(no_name):
        CONFIG['sir'] = str(input()).capitalize()
        no_name = ( len(CONFIG['sir']) == 0 )
    print("Setup complete.")
    print(CONFIG['sir'] + ", let us begin.")

def is_valid(x):
    # x being the piece we want to move
    empty = BOARD.index(' ')
    new = BOARD.index(x)
    upper = empty - int(CONFIG['cols'])
    lower = empty + int(CONFIG['cols'])
    left = empty - 1
    right = empty + 1
    valid_moves = [upper, lower, left, right]
    return (new in valid_moves)

def main():
    setup()
    sleep(1)
    while(END==0):
        update()
        sleep(3)

    if (END == -1):
        print("Pathetic.")

    else :
        print("Decent enough. I will grant you passage.")


if __name__ == "__main__":
    main()