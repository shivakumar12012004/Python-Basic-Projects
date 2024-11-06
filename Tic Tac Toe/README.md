# Tic-Tac-Toe Game

This is a simple text-based Tic-Tac-Toe game built using Python. 
The game allows two players to take turns and play Tic-Tac-Toe on a 3x3 grid. 
The game will check for a winner after every move and display the winner or a tie when the game ends.

## Features

- Two players can play on the same system.
- Simple, text-based user interface.
- Input validation to ensure the moves are valid.
- The game ends when a player wins or when there's a tie.
- The winner is displayed after the game ends.

## How to Play

1. Clone the repository or download the game script file.
2. Open a terminal/command prompt.
3. Navigate to the directory containing the `tictactoe.py` file.
4. Run the script by executing:
5. The game will display a 3x3 grid and ask each player to input a number (between 1-9) corresponding to an empty spot on the grid.
6. Players take turns entering their moves. Player X always goes first.
7. The game will announce the winner or indicate a tie when the game ends.

## Gameplay Example

| - | - | - |
--------------
| - | - | - |
--------------
| - | - | - |
--------------

Enter a number between 1-9 : 1

| X | - | - |
--------------
| - | - | - |
--------------
| - | - | - |
--------------

Enter a number between 1-9 : 2

| X | O | - |
--------------
| - | - | - |
--------------
| - | - | - |
--------------

Enter a number between 1-9 : 3

| X | O | X |
--------------
| - | - | - |
--------------
| - | - | - |
--------------

Enter a number between 1-9 : 4

| X | O | X |
--------------
| O | - | - |
--------------
| - | - | - |
--------------

Enter a number between 1-9 : 5

| X | O | X |
--------------
| O | X | - |
--------------
| - | - | - |
--------------

Enter a number between 1-9 : 6

| X | O | X |
--------------
| O | X | O |
--------------
| - | - | - |
--------------

Enter a number between 1-9 : 7

| X | O | X |
--------------
| O | X | O |
--------------
| X | - | - |
--------------

The winner is X

## Game Logic

- The game board is represented by a list of 9 elements, initialized as `"-"` to represent empty spots.
- Players alternate between 'X' and 'O'. 
- After each move, the board is printed, and a winner is checked.
- The game ends if there is a winner or if there are no empty spots left (a tie).

## Requirements

- Python 3.x or later.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, make changes, and submit a pull request. Contributions are welcome!

## Acknowledgements

- The game logic and structure were created by [Your Name].
