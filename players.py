from random import randrange
from copy import copy
import time
from iplayer import IPlayer

# definetly not a*. doesnt even work ffs
class AstarAlgorithm(IPlayer):
    def __init__(self):
        self.name = "A* algorithm with manhattan distance as heuristic"
        self.solved = False
        self.searched_once = False
        self.solution = []
        self.iterations = 0
        self.depth = -1

    def set_max_depth(self, depth):
        self.depth = depth

    def distance_de_manhattan(self, xA, yA, xB, yB ):
        return abs(xB-xA) + abs(yB-yA)

    class Node():
        # could be a node factory, with heuristic implemented here. but yeah
        # this is ugly. but yeah
        def __init__(self, parent, move, board):
            
            self.parent = parent
            self.move = move
            self.board = board
            if self.parent == None:
                self.g = 0
            else :
                self.g = self.parent.g + 1
            self.h = 0
            self.cost = self.h + self.g

        def equals(self, node):
            return (self.board == node.board)

        def in_list(self, node_list):
            for node in node_list:
                if(self.equals(node)):
                    return True
            return False

        def __str__(self):
            return str(self.board) + " : costs "+ str(self.cost)

    def heuristic(self, board):
        total_manhattan = 0
        for i in range(len(board)):
            if(board[i] != 0):
                xA = int(board[i])/3
                yA = int(board[i])%3
                xB = i/3
                yB = i%3    
                total_manhattan += self.distance_de_manhattan(xA, yA, xB, yB)
        return total_manhattan

    def Astar(self, initial_board):
        
        # Initlialize the graph for A* :
        node0 = self.Node(parent=None, move=None, board=initial_board) # initial node
        node0.g = 0
        node0.h = self.heuristic(initial_board)
        node0.cost = node0.h + node0.g

        final_board = [i for i in range(9)] # stop condition
        open_nodes = [node0]
        closed_nodes = []
        
        if (initial_board == final_board):
            self.solved = True
            self.solution = [0]

        self.searched_once = True
        self.iterations += 1
        max_depth = self.depth

        # We search while there are nodes to search on.
        while( (len(open_nodes) > 0) & (max_depth != 0) ):
            max_depth -= 1
            self.iterations += 1
            # select next best node :
            curr_node = None
            for node in open_nodes:
                if (curr_node != None):
                    
                    if(curr_node.cost > node.cost):
                        curr_node = node
                else :
                    curr_node = node
            
            # curr_node here is the best next node
            if(curr_node.board == final_board):
                self.solved = True
                self.solution = self.path_from_node(curr_node)
                return self.solution

            open_nodes.remove(curr_node)
            closed_nodes.append(curr_node)
            
            next_nodes = []
            for move in self._possible_moves(curr_node.board, self.config): 
                new_node = self.Node(parent=curr_node, board=self._simulate_move(move, curr_node.board), move=move)
                new_node.h = self.heuristic(new_node.board)
                # new_node.g is set automatically. And so shoud h and loss be... but yeah
                new_node.cost = new_node.h + new_node.g
                
                next_nodes.append(new_node)
            
            if(next_nodes == []):
                print("Error, next nodes is empty.")
                return
            for node in next_nodes :
                if  not (node.in_list(closed_nodes)):
                    if not node.in_list(open_nodes):
                        open_nodes.append(node)
                    else :
                        for node_from_open_nodes in open_nodes:
                            if node.equals(node_from_open_nodes):
                                if node_from_open_nodes.g > node.g :
                                    open_nodes.remove(node_from_open_nodes)
                                    open_nodes.append(node)

                                break
        if(max_depth == 0):
            print("Reached maximum depth without finding a solution.")
        else:
            print("No solution")
        self.solved = False
        
    def path_from_node(self, node):
        path = []
        while(node.parent != None):
            path.append(node.move)
            node = node.parent
        
        return path

    def move(self, board, config):
        if not self.searched_once :
            self.board = copy(board)
            self.board[self.board.index(' ')] = 0
            self.board = [ int(ele) for ele in self.board ]
            self.config = config
            
            start_time = time.time()
            self.searched_once = True   
            self.Astar(self.board)
            
            if self.solved :
                print("--- SOLVED in {}seconds ({} iterations) ---".format((time.time() - start_time), self.iterations ))
                try:
                    return str(self.solution.pop())
                except IndexError:
                    return str(None)
            else :
                return None
        else :
            if self.solved:
                return str(self.solution.pop() ) 
            else :
                return None

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
        self.name = "Limited depth player"
        self.max_depth = 25 # experiment with this here
        self.name = "Limited-depth search"
        self.solved = False
        self.searched_once = False
        self.solution = []

    def set_max_depth(self, depth):
        self.max_depth = depth

    def __search(self, board, trace, depth, previous_move):
        print(board)
        if (self._wins(board)):
            self.solution = trace
            self.solution.reverse()
            self.solved = True
            self.searched_once = True
            1/0
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
                print(self.solution)

                self.solved = True
                self.searched_once = True
                
        if self.solved:
            return str(self.solution.pop() )  # no i want the other extremity hon
        else :
            print("Failed to find a solution in reasonable time. Did {} iterations".format(self.iterations))
            input()
            return None

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
            return None        

if __name__ == "__main__":
                
    debug_board = ['1','2','6','3','4',' ','5','7','8']
    debug_config={
        'rows':3,
        'cols':3,
        'sir':'Undefined',}


    p = CLIPlayer()
    p.move(debug_board, debug_config)
        # _________________
        # |     |     |     |
        # |  1  |  2  |  6  |
        # |_____|_____|_____|
        # |     |     |     |
        # |  3  |  4  |     |
        # |_____|_____|_____|
        # |     |     |     |
        # |  5  |  7  |  8  |
        # |_____|_____|_____|