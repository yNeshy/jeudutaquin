from random import randrange

#class GeneticAlgorithm():





# implement move(board, config)
class RandomPlayer():
    def possible_moves_for_x(self, x):
        upper = x - config['cols']
        lower = x + config['cols']
        left = x - 1
        right = x + 1
        result = []
        if (empty(upper) ): result.append(upper)
        if (empty(lower) ): result.append(lower)
        if (empty(left) ): result.append(left)
        if (empty(right) ): result.append(right)
        return result 

    def move(self, board, config):
        move = allowed_moves[randrange(len(allowed_moves))]
        return (move)


class CLIPlayer():

    def move(self, board, config):
        piece = int(input("Piece to move: "))
        return str(piece)

