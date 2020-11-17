from copy import copy

class IPlayer :
    def __init__(self):
        self.name = "Unnamed algorithm"

    def set_max_depth(self, depth):
        pass

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
        if( ( (empty+1)  % int(config['cols']) != 0 )):
            left = empty - 1
            tmp.append(left)
        if( ((empty-1)%int(config['cols']) != 0 )):
            right = empty + 1
            tmp.append(right)
        
        valid_moves = [board[i] for i in tmp if i in range(int(config['cols']) * int(config['rows'])) ]
        print(valid_moves)
        return valid_moves

    def _simulate_move(self, move, board):
        zero = 0
        try :
            board.index(zero)
            move = int(move)
        except ValueError :
            zero = ' '
        new_board = copy(board)
        old_0 = new_board.index(zero)
        new_0 = new_board.index(move)
        new_board[old_0], new_board[new_0] = new_board[new_0], new_board[old_0]
        return new_board

    def move(self, board, config):
        """
        return, move my move, what this algorithm predicts should be done.
        It possible to make calculations only once, the first time this function
        is called and store the predictions in a list. Then pop() the move list and 
        return it move by move.
        """
        
        return self._possible_moves(board, config)[0]

debug_template = """
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
debug_template_list = ['(','é','"','@','&','ç','-','è',')']
debug_board = [' ', '1', '2', '3', '4', '5', '6', '7', '8']
debug_config = {
            'rows':3,
            'cols':3,
            'sir':'Undefined'}

if __name__ == "__main__":
    def draw(board):
        curr_BOARD = copy(debug_template)
        for i in range(len(board)):
            curr_BOARD = curr_BOARD.replace(debug_template_list[i], board[i])
        print(curr_BOARD)
        del curr_BOARD



    debug_player = IPlayer()
    board =['1','2','6','3','4',' ','5','7','8']
    next_moves = debug_player._possible_moves(board, debug_config )
    print("Initial board:")
    draw(board)
    print("Moves : "+str(next_moves))
    for move in next_moves:
        print("Moving "+str(move))
        tmp_board = debug_player._simulate_move(move, board)
        draw(tmp_board)
        input()
        