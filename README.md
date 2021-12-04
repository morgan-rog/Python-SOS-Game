# python-sos-game
## Problem Description
```
Your customer asks you to develop the software that allows a blue player to play the SOS game 
against a red player or replay a recorded game. Either player can be human or computer. 
The game board is a grid of nxn (n>2) squares. The two players take turns to add either an "S" or 
an "O" to an unoccupied square, with no requirement to use the same letter each turn. Each 
player attempts to create the straight sequence S-O-S among connected squares (diagonally, 
horizontally, or vertically). To keep track of who made which SOSs, a line in the player’s color 
(i.e., blue or red) is drawn for each SOS sequence.
```
```
The game can be played in one of the following modes: 
(a) Simple game: The player who creates the first SOS is the winner. If no SOS is created
when the board has been filled up, then the game is a draw. Turns alternate between 
players after each move.
(b) General game: The game continues until the board has been filled up. The winner is the 
player who made the most SOSs. If both players made the same number of SOSs, then 
the game is a draw. When a player succeeds in creating an SOS, that player immediately 
takes another turn and continues to do so until no SOS is created on their turn. Otherwise,
turns alternate between players after each move.
```