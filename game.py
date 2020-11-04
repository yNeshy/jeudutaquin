from copy import copy
from time import sleep
from random import shuffle
import os

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
    def move(board, allowed_moves):
        return (source, destination)

def clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def empty(case):
    """ return if a case is empty the board """
    if (case < 0):
        return False
    if (case > len(BOARD)):
        return False
    if (BOARD[case] != ' '):
        return False
    return True

def possible_moves(x):
    upper = x - CONFIG['cols']
    lower = x + CONFIG['cols']
    left = x - 1
    right = x + 1
    result = []
    if (empty(upper) ): result.append(upper)
    if (empty(lower) ): result.append(lower)
    if (empty(left) ): result.append(left)
    if (empty(right) ): result.append(right)
    return result 

def draw():
    curr_BOARD = copy(TEMPLATE)
    for i in range(len(BOARD)):
        curr_BOARD = curr_BOARD.replace(TEMPLATE_LIST[i], BOARD[i])

    print(curr_BOARD)

def update():
    clear()
    draw()
    print(possible_moves(3))

def setup():
    shuffle(BOARD)
    
    print("How should I could I call you fine sir?: ")
    no_name = True
    while(no_name):
        CONFIG['sir'] = str(input())
        no_name = ( len(CONFIG['sir']) == 0 )
    print(no_name)
            
    print("Setup complete.")
    print(CONFIG['sir'] + ", let us begin.")

def main():
    setup()
    while(True):
        update()
        sleep(5)

main()