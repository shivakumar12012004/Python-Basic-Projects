# Slot Machine Game

This is a simple text-based Slot Machine game built using Python. Players can deposit money, place bets on multiple lines, and spin the slot machine to win. The game uses a random selection of symbols for each spin, and winnings are calculated based on the combinations of symbols that appear.

## Features

- Deposit money into your account to play.
- Bet on 1-3 lines with custom bet amounts.
- Randomly generated slot machine symbols based on predefined symbol counts.
- Displays the results of the spin and any winnings.
- Tracks and updates the player's balance after each spin.

## How to Play

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the `slot_machine.py` file.
4. Run the script by executing:
   ```bash
   python slot_machine.py
5.The game will prompt you to:
6.Enter how much you'd like to deposit.
7.Select how many lines (1-3) you'd like to bet on.
   Enter how much you'd like to bet on each line.
The slot machine will then "spin," and the results will be shown. You'll win or lose based on the combination of symbols.
You can continue playing or quit at any time by typing q



What would you like to deposit? $100
Enter the number of lines to bet on (1-3)? 2
What would you like to bet on each line? $10
You are betting $10 on 2 lines. Total bet is equal to: $20

A | D | B
--------------
A | B | D
--------------
C | A | A


You won $10.
You won on lines: 1
Current balance is $90
Press enter to play (q to quit).


Slot Machine Rules
The slot machine consists of 3 rows and 3 columns.
Symbols available: A, B, C, and D.
Symbol "A" appears 2 times, "B" appears 4 times, "C" appears 6 times, and "D" appears 8 times.
The player can bet on 1-3 lines.
The player chooses how much to bet on each line (between $1 and $100).
After each spin, the game calculates winnings based on symbol combinations on each line.
The game continues until the player chooses to quit or their balance reaches zero.
Requirements
Python 3.x or later.
