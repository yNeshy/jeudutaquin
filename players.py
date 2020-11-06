from random import randrange
from copy import copy
import queue
import time

class AstarAlgorithm():
    def __init__(self):
        self.solved = False
        self.previous_move = ''

    def distance_de_manhattan(self, xA, yA, xB, yB ):
        return abs(xB-xA) + abs(yB-yA)

    def possible_moves(self):
        tmp = []
        empty = self.board.index(0)
        upper = empty - int(self.config['cols'])
        lower = empty + int(self.config['cols'])
        tmp.append(upper)
        tmp.append(lower)
        if( ( empty  % int(self.config['cols']) != 0 )):
            left = empty - 1
            tmp.append(left)
        if( ((empty-1)%int(self.config['cols']) != 0 )):
            right = empty + 1
            tmp.append(right)
        valid_moves = [self.board[i] for i in tmp if i in range(int(self.config['cols']) * int(self.config['rows'])) ]
        return valid_moves

    def heuristic(self, board):
        total_manhattan = 0
        for i in range(len(board)):
            xA = int(board[i])/3
            yA = int(board[i])%3
            xB = i/3
            yB = i%3
            total_manhattan += self.distance_de_manhattan(xA, yA, xB, yB)
        return total_manhattan

    def move(self, board, config):
        self.board = board
        self.config = config
        options = self.possible_moves()
        min_heuristic = 9**9    # worst case scenario
        final_move = None
        for move in possible_moves():
            if (move != self.previous_move):
                local_board = copy(board)
                _out = self.BOARD.index(0)
                _in = self.BOARD.index(move)
                
                local_board[_out] , local_board[_in] = local_board[_in] , local_board[_out]
                curr_heuristic = self.heuristic(local_board)
                if(curr_heuristic <= min_heuristic):
                    min_heuristic = curr_heuristic
                    final_move = move
        self.previous_move = final_move
        return final_move

# implement move(board, config)
class RandomPlayer():

    def possible_moves(self, board, config):   
        tmp = []
        empty = board.index(' ')
        upper = empty - int(config['cols'])
        lower = empty + int(config['cols'])
        tmp.append(upper)
        tmp.append(lower)
        if( ( empty  % int(config['cols']) != 0 )):
            left = empty - 1
            tmp.append(left)
        if( ((empty-1)%int(config['cols']) != 0 )):
            right = empty + 1
            tmp.append(right)
        valid_moves = [board[i] for i in tmp if i in range(int(config['cols']) * int(config['rows'])) ]
        return valid_moves

    def move(self, board, config):
        allowed_moves = self.possible_moves(board , config)
        move = allowed_moves[randrange(len(allowed_moves))]
        return (move)

class CLIPlayer():
    def move(self, board, config):
        piece = int(input("Piece to move: "))
        return str(piece)

class LimitedDepthPlayer():

    def __init__(self):
        self.max_depth = 5 # experiment with this here
        self.solved = False
        self.searched_once = False
        self.solution = []

    def set_max_depth(self, depth):
        self.max_depth = depth

    def wins(self, board):
        won = True
        i = 0
        while (won &(i< (len(board) -1))):
            i = i+1
            won = (int(board[i-1]) <= int(board[i]))
        return won

    def __possible_moves(self, board):   
        tmp = []
        empty = board.index(0)
        upper = empty - int(self.config['cols'])
        lower = empty + int(self.config['cols'])
        tmp.append(upper)
        tmp.append(lower)
        if( ( empty  % int(self.config['cols']) != 0 )):
            left = empty - 1
            tmp.append(left)
        if( ((empty-1)%int(self.config['cols']) != 0 )):
            right = empty + 1
            tmp.append(right)
        valid_moves = [int(board[i]) for i in tmp if i in range(int(self.config['cols']) * int(self.config['rows'])) ]
        return valid_moves

    def __simulate_move(self, move, board):
        new_board = copy(board)
        old_0 = new_board.index(0)
        new_0 = new_board.index(int(move))
        new_board[old_0], new_board[new_0] = new_board[new_0], new_board[old_0]
        return new_board

    def __search(self, board, trace, depth, previous_move):
        if (self.wins(board)):
            self.solution = trace
            self.solution.reverse()
            self.solved = True
            self.searched_once = True
            print(1/0)
            return

        if(depth >= self.max_depth):
            return False
        children = [ self.__simulate_move(move, board) for move in self.__possible_moves(board) ]

        for move in self.__possible_moves(board) :
            if(move != previous_move) :    
                curr_board = self.__simulate_move(move, board)
                trace.append(move)
                self.__search(curr_board, trace, depth+1, move)
                trace.remove(move)
        return

    def move(self, board, config):
        
        print("My max depth is : "+str(self.max_depth))
        if not self.searched_once :
            print("Calculating...")
            self.board = copy(board)
            self.board[self.board.index(' ')] = 0
            self.board = [ int(ele) for ele in self.board ]
            self.config = config
            if(self.wins(self.board)):
                return board[0]
            try:
                start_time = time.time()
                self.__search(self.board, [], 0, 0)
                print("--- %s seconds ---" % (time.time() - start_time))
                self.searched_once = True
            except(ZeroDivisionError):
                print("SOLVED")
                self.solved = True
                self.searched_once = True
                
        if self.solved:
            return str(self.solution.pop() )  # no i want the other extremity hon
        else :
            print("Failed to find a solution in reasonable time.")
            input()
            return '3'


if __name__ == "__main__":
    debug_board = ['1',' ','2','3','4','5','6','7','8']
    debug_config={
        'rows':3,
        'cols':3,
        'sir':'Undefined',}

    p = LimitedDepthPlayer()
    p.move(debug_board, debug_config)
        # _________________
        # |     |     |     |
        # |  1  |     |  2  |
        # |_____|_____|_____|
        # |     |     |     |
        # |  3  |  4  |  5  |
        # |_____|_____|_____|
        # |     |     |     |
        # |  6  |  7  |  8  |
        # |_____|_____|_____|