from copy import copy
from time import sleep
from random import shuffle
import os
from players import CLIPlayer



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
    # î columns and rows identifiers.
TEMPLATE_LIST = ['(','é','"','@','&','ç','-','è',')']

BOARD = [' ', '1', '2', '3', '4', '5', '6', '7', '8'] # initial board

CONFIG = {
    'rows':3,
    'cols':3,
    'sir':'Undefined',
}


class TemplateTaquinPlayer :
    def __init__():
        pass    
    def help():
        return "move the space from source to destination"
    def move(board, config):
        return (source, destination)



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
    (source, dest) = player.move(BOARD, CONFIG)
    if (is_valid(int(source), int(dest)) ):
        print("it is valid")
    else :
        print("invalid")

def setup():
    shuffle(BOARD)
    
    print("How should I could I call you fine sir?: ")
    no_name = True
    while(no_name):
        CONFIG['sir'] = str(input()).capitalize()
        no_name = ( len(CONFIG['sir']) == 0 )
    print(no_name)
    
    print("Setup complete.")
    print(CONFIG['sir'] + ", let us begin.")



def is_valid(source, destination):
    upper = source - int(CONFIG['cols'])
    lower = source + int(CONFIG['cols'])
    left = source - 1
    right = source + 1
    valid_moves = []
    if (is_empty(upper) ): valid_moves.append(upper)
    if (is_empty(lower) ): valid_moves.append(lower)
    if (is_empty(left) ): valid_moves.append(left)
    if (is_empty(right) ): valid_moves.append(right)
    return (destination in valid_moves)


def main():
    setup()
    while(True):
        update()
        sleep(7)

main()