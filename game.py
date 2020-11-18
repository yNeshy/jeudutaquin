from copy import copy
from time import sleep
from random import shuffle
import os
from players import CLIPlayer, RandomPlayer, AstarAlgorithm, LimitedDepthPlayer, LimitedDepthBreadthPlayer, AstarAlgorithm
import time
from iplayer import IPlayer
from random import randrange

class CLITaquin():
    def __init__(self,player=RandomPlayer(), board=None):
        self.player = player
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
        
        if (board == None):
            self.BOARD = [' ', '1', '2', '3', '4', '5', '6', '7', '8'] # initial board
            self.randomize = True
        else :
            self.BOARD = board
            self.randomize = False
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
        if (case >= len(self.BOARD)):
            return False
        if (self.BOARD[case] != ' '):
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
    
    def move(self, x):
        space = self.BOARD.index(' ')
        new_space = self.BOARD.index(x)
        self.BOARD[space] , self.BOARD[new_space] = self.BOARD[new_space] , self.BOARD[space]

    def update(self):
        self.clear()
        self.draw()
        x = str(self.player.move(self.BOARD, self.CONFIG))
        print("Sir {} asked to move {}.".format(self.CONFIG['sir'], x))
        if (self.is_valid(x)):
            self.move(x)
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

    def shuffle(self, complexity):
        tools = IPlayer()
    
        for _ in range(complexity):
            options = [ str(o) for o in tools._possible_moves(self.BOARD, self.CONFIG) ]
            x = options[randrange(len(options))]
            self.move(x)

        return self.BOARD

    def setup(self):      
        self.ROUND = 0
        self.END = 0
        
        no_name = self.player.name
        while(len(no_name) < 1 ):
            print("How should I call you fine sir?: ")
            self.CONFIG['sir'] = str(input()).capitalize()
            no_name = ( len(self.CONFIG['sir']) == 0 )
        self.CONFIG['sir'] = no_name
        if(self.randomize):
            _i = None
            while (not _i):
                _i = input("Choose a complexity level: [1;oo[ : ")
            complexity = int(_i)
            self.shuffle(complexity)
            #self.player.set_max_depth(complexity + 3)

        print("Setup complete.")
        print(self.CONFIG['sir'] + ", let us begin.")

    def is_valid(self, x):
        # x being the piece we want to move
        zero = 0
        try :
            self.BOARD.index(zero)
        except ValueError :
            zero = ' '
        empty = self.BOARD.index(zero)
        valid_moves=[]
        # top
        if((empty-int(self.CONFIG['cols']) > 0)):
            valid_moves.append(self.BOARD[empty-int(self.CONFIG['cols'])])
        
        # bottom
        if((empty+int(self.CONFIG['cols'])) < (int(self.CONFIG['cols']*int(self.CONFIG['rows'])))):

            valid_moves.append(self.BOARD[empty+int(self.CONFIG['cols'])])
        
        # left
        if(empty % int(self.CONFIG['cols']) > 0 ):
            valid_moves.append(self.BOARD[empty-1])
        # right
        if ((empty+1) % int(self.CONFIG['cols']) > 0 ):
            valid_moves.append(self.BOARD[empty+1])

        return x in valid_moves

    def main(self):
        
        self.setup()
        self.draw()
        print("Enter to enter.")
        input()

        sleep(1)  
        while(self.END==0):
            self.ROUND += 1
            self.update()
            sleep(1)

        if (self.END == -1):
            print("Pathetic.")
        else :
            self.clear()
            self.draw()
            print("Decent enough. I will grant you passage.")


if __name__ == "__main__":
    print("The star")
    CLITaquin(AstarAlgorithm()).main()
    