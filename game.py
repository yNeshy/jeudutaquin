from copy import copy
from time import sleep
from random import shuffle
import os
from players import CLIPlayer, RandomPlayer, AstarAlgorithm, LimitedDepthPlayer
import time


class TemplateTaquinPlayer :
    def __init__(self):
        pass    
    def help(self):
        return "move the space from source to destination"
    def move(self, board, config):
        return piece_to_move

class CLITaquin():
    def __init__(self):
        self.player = LimitedDepthPlayer()
        self.player.set_max_depth(8)
        
        
        self.END = 0
        self.TEMPLATE = """
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
        self.TEMPLATE_LIST = ['(','é','"','@','&','ç','-','è',')']
        self.BOARD = [' ', '1', '2', '3', '4', '5', '6', '7', '8'] # initial board
        self.CONFIG = {
            'rows':3,
            'cols':3,
            'sir':'Undefined'}
        self.ROUND = 0

    def clear(self):
        # for mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # for windows platfrom
            _ = os.system('cls')

    def is_empty(self, case):
        """ return if a case is empty the board """
        if (case < 0):
            return False
        if (case >= len(BOARD)):
            return False
        if (BOARD[case] != ' '):
            return False
        return True

    def draw(self):
        curr_BOARD = copy(self.TEMPLATE)
        for i in range(len(self.BOARD)):
            curr_BOARD = curr_BOARD.replace(self.TEMPLATE_LIST[i], self.BOARD[i])
        print("sir {} is playing. Do not disturb.".format(self.CONFIG['sir']))
        print("Round: "+str(self.ROUND))
        print(curr_BOARD)
        del curr_BOARD
    
    def update(self):
        self.clear()
        self.draw()
        x = self.player.move(self.BOARD, self.CONFIG)
        print("Sir {} asked to move {}.".format(self.CONFIG['sir'], x))
        input()
        if (self.is_valid(x)):
            space = self.BOARD.index(' ')
            new_space = self.BOARD.index(x)
            self.BOARD[space] , self.BOARD[new_space] = self.BOARD[new_space] , self.BOARD[space]
            if self.is_won():
                self.END=1
        else :
            self.END=-1

    def is_won(self):
        won = True
        i = 0
        while (won &
         (i< (len(self.BOARD) -1))
         ):
            i = i+1
            won = (self.BOARD[i-1] <= self.BOARD[i])
        return won

    def setup(self):
        
        self.BOARD = ['1','4','2',' ','7','5','3','6','8']

        self.ROUND = 0
        self.END = 0
        #print("How should I call you fine sir?: ")
        no_name = True
        while(no_name):
            self.CONFIG['sir'] = "algorithm"  #str(input()).capitalize()
            no_name = ( len(self.CONFIG['sir']) == 0 )
        print("Setup complete.")
        print(self.CONFIG['sir'] + ", let us begin.")

    def is_valid(self, x):
        # x being the piece we want to move
        tmp = []
        empty = self.BOARD.index(' ')
        upper = empty - int(self.CONFIG['cols'])
        lower = empty + int(self.CONFIG['cols'])
        tmp.append(upper)
        tmp.append(lower)
        if( ( empty  % int(self.CONFIG['cols']) != 0 )):
            left = empty - 1
            tmp.append(left)
        if( ((empty-1)%int(self.CONFIG['cols']) != 0 )):
            right = empty + 1
            tmp.append(right)
        valid_moves = [self.BOARD[i] for i in tmp if i in range(int(self.CONFIG['cols']) * int(self.CONFIG['rows'])) ]
        
        return (x in valid_moves)

    def main(self):
        print("Enter to enter.")
        while(str(input()) == ''):
            self.setup()
            self.draw()
            print("Enter a character to begin.")

        sleep(1)  
        while(self.END==0):
            self.ROUND += 1
            self.update()
            sleep(0.5)

        if (self.END == -1):
            print("Pathetic.")
        else :
            self.draw()
            print("Decent enough. I will grant you passage.")


if __name__ == "__main__":
    CLITaquin().main()