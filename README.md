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
To create a new player, inherit from IPlayer interface (on iplayer.py file) and implement your own `move(board, config)` function.

A move is denoted by the number of the piece to move and is only acceptable, obviously, if the move returned is possible on the board.

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


Import your new Player, then edit the game.py to use your newly implemented player.

Player class:
class YourPlayer(IPlayer):
  ...

Line to edit in main :
CLITaquin(player=YOUR_PLAYER).main()

