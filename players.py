from random import randrange
from copy import copy
import time
from iplayer import IPlayer

# definetly not a*. doesnt even work ffs
class AstarAlgorithm(IPlayer):
    def __init__(self):
        self.name = "Fake A* algorithm that definitely doesn't work"
        self.solved = False
        self.previous_move = ''

    def distance_de_manhattan(self, xA, yA, xB, yB ):
        return abs(xB-xA) + abs(yB-yA)

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
        options = self._possible_moves(board, config)
        min_heuristic = 9**9    # worst case scenario
        final_move = None
        for move in options:
            if (move != self.previous_move):
                local_board = copy(board)
                _out = self.board.index(0)
                _in = self.board.index(move)
                
                local_board[_out] , local_board[_in] = local_board[_in] , local_board[_out]
                curr_heuristic = self.heuristic(local_board)
                if(curr_heuristic <= min_heuristic):
                    min_heuristic = curr_heuristic
                    final_move = move
        self.previous_move = final_move
        return final_move 

# implement move(board, config)
class RandomPlayer(IPlayer):
    def __init__(self):
        self.name = "Choji"
        self.is_setup = False

    def move(self, board, config):
        if not self.is_setup :
            self.config = config
        allowed_moves = self._possible_moves(board, config)
        move = allowed_moves[randrange(len(allowed_moves))]
        return (move)

class CLIPlayer(IPlayer):
    def __init__(self):
        self.name = "Interactive command line interface player."
        self.is_setup = False

    def move(self, board, config):
        if not self.is_setup :
            self.config = config
            self.is_setup = True
        piece = int(input("Piece to move: "))
        return str(piece)

class LimitedDepthPlayer(IPlayer):

    def __init__(self):
        """Default max depth set to 25 iterations. You can and should change it through the set_max_depth(depth) method"""
        self.max_depth = 25 # experiment with this here
        self.name = "Limited-depth search"
        self.solved = False
        self.searched_once = False
        self.solution = []

    def set_max_depth(self, depth):
        self.max_depth = depth

    def __search(self, board, trace, depth, previous_move):
        if (self._wins(board)):
            self.solution = trace
            self.solution.reverse()
            self.solved = True
            self.searched_once = True
            print(1/0)
            return

        if(depth >= self.max_depth):
            return False
        self.iterations += 1
        for move in self._possible_moves(board, self.config) :
            if(move != previous_move) :    
                curr_board = self._simulate_move(move, board)
                trace.append(move)
                self.__search(curr_board, trace, depth+1, move)
                trace.remove(move)
        return

    def move(self, board, config):
        
        print("My max depth is : "+str(self.max_depth))
        if not self.searched_once :
            self.iterations = 0
            print("Calculating...")
            self.board = copy(board)
            self.board[self.board.index(' ')] = 0
            self.board = [ int(ele) for ele in self.board ]
            self.config = config
            if(self._wins(self.board)):
                return board[0]
            try:
                start_time = time.time()
                self.__search(self.board, [], 0, 0)
                self.searched_once = True
                if self.solved :
                    print("--- SOLVED in {}seconds ({} iterations) ---".format((time.time() - start_time), self.iterations ))
            except(ZeroDivisionError):
                print("--- SOLVED in {}seconds ({} iterations) ---".format((time.time() - start_time), self.iterations ))

                self.solved = True
                self.searched_once = True
                
        if self.solved:
            return str(self.solution.pop() )  # no i want the other extremity hon
        else :
            print("Failed to find a solution in reasonable time. Did {} iterations".format(self.iterations))
            input()
            return '3'

class LimitedDepthBreadthPlayer(LimitedDepthPlayer):
    def __init__(self):
        super().__init__()
        self.name = "Limited-width search"

    def __search(self, node_trace_tuples, depth):
        next_tuples = node_trace_tuples
        while(depth < self.max_depth):   
            depth += 1
            tuples = next_tuples ## current layer being examinated
            for node_trace in tuples :
                # setup of current node
                self.iterations += 1
                board = node_trace[0]
                trace = node_trace[1]
                len_trace = len(trace) - 1

                if(self._wins(board)):
                    self.solution = trace
                    self.solution.reverse()
                    self.solved = True
                    self.searched_once = True
                    raise ZeroDivisionError
                
                # create the next nodes
                for move in self._possible_moves(board, self.config):                    
                    if(len_trace >= 0):
                        if(move != trace[len_trace]):
                            tuples.append([self._simulate_move(move, board), trace+[move]])
                    else :
                        tuples.append([self._simulate_move(move, board), trace+[move]])
                #procede to the next iteration

        self.solved = False
        self.searched_once = True

    def move(self, board, config):    
        print("My max depth is : "+str(self.max_depth))
        if not self.searched_once :
            self.iterations = 0
            print("Calculating...")
            self.board = copy(board)
            self.board[self.board.index(' ')] = 0
            self.board = [ int(ele) for ele in self.board ]
            self.config = config
            if(self._wins(self.board)):
                return board[0]
            try:
                start_time = time.time()
                self.__search([[self.board,[]]], 0)
                self.searched_once = True
                if self.solved :
                    print("--- SOLVED in %s seconds ---" % (time.time() - start_time))
            except(ZeroDivisionError):
                print("--- SOLVED in %s seconds ---" % (time.time() - start_time))

                self.solved = True
                self.searched_once = True
                
        if self.solved:
            return str(self.solution.pop() )  # no i want the other extremity hon
        else :
            print("Failed to find a solution in reasonable time. Did {} iterations".format(self.iterations))
            input()
            return '3'        


if __name__ == "__main__":
    debug_board = ['1','4','2',' ','3','5','6','7','8']
    debug_config={
        'rows':3,
        'cols':3,
        'sir':'Undefined',}

    p = LimitedDepthBreadthPlayer()
    p.set_max_depth(3)
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