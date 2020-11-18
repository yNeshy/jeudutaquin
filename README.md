### What is it ? 
A command line interface, Taquin game.
It has support for :
* Human player (command line input)
* Limited depth first search algorithm
* Unlimited depth first search algorithm
* Limited width first search algorithm
* Unlimited with first search algorithm
* A* algorithm with manhattan distance as heuristic.




### Run it 

##### Requirements:
* Python 2.7 or higher
* A screen.

Download all files and run the game.py file.

By default, it will generate its own board according to a the complexity you input, before solving it step by step.


### Run on custom board : 
Use the CLITaquin this way
with board being like ['1','2','6','3','4',' ','5','7','8']

`CLITaquin(player=A_PLAYER, board=YOU_BOARD).main()`


### Create a new player 
To create your own player, c/c the game.TemplateTaquinPlayer and implement your own move(board, config) function.

Import your new Player, then edit this life one game.py to your newly implemented player.
class YourPlayer(IPlayer):
  ...

and implement the "move(board, config)" function, which returns the move to made on the current board. 
A move is denoted by the number of the piece to move:

##### Example
        __________________
        |     |     |     |
        |  3  |  1  |  2  |
        |_____|_____|_____|
        |     |     |     |
        |     |  4  |  5  |
        |_____|_____|_____|
        |     |     |     |
        |  6  |  7  |  8  |
        |_____|_____|_____|
Acceptable returns of your move function should be either 3, 4 or 6.

PS: You can generate a solution the first time move is called and store it in a FIFO or whatever. Be smart with it.

