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

![Screenshot 2024-11-06 140447](https://github.com/user-attachments/assets/efe0ebca-742b-4477-829e-df25797d9423)

![Screenshot 2024-11-06 140501](https://github.com/user-attachments/assets/243d0d17-966a-4493-a4ec-2f46ccc6e866)


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