from copy import copy

class IPlayer :
    def __init__(self):
        self.name = "Unnamed algorithm"

    def _wins(self, board):
        won = True
        i = 0
        while (won &(i< (len(board) -1))):
            i = i+1
            won = (int(board[i-1]) <= int(board[i]))
        return won

    def _possible_moves(self, board, config):   
        
        zero = 0
        try :
            board.index(zero)
        except ValueError :
            zero = ' '
        tmp = []
        empty = board.index(zero)
        upper = empty - int(config['cols'])
        lower = empty + int(config['cols'])
        tmp.append(upper)
        tmp.append(lower)
        if( ( empty  % int(config['cols']) != zero )):
            left = empty - 1
            tmp.append(left)
        if( ((empty-1)%int(config['cols']) != zero )):
            right = empty + 1
            tmp.append(right)
        valid_moves = [board[i] for i in tmp if i in range(int(config['cols']) * int(config['rows'])) ]
        return valid_moves

    def _simulate_move(self, move, board):
        new_board = copy(board)
        old_0 = new_board.index(0)
        new_0 = new_board.index(int(move))
        new_board[old_0], new_board[new_0] = new_board[new_0], new_board[old_0]
        return new_board

    def move(self, board, config):
        """
        return, move my move, what this algorithm predicts should be done.
        It possible to make calculations only once, the first time this function
        is called and store the predictions in a list. Then pop() the move list and 
        return it move by move.
        """
        
        return board[0]
