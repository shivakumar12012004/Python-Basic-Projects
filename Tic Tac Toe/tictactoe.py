board=["1","2","3","4","5","6","7","8","9"]
currplayer = None
winner=None
gameRunning=True

#print the board
def printb(board):
    print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
    print("--------------")
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
    print("--------------")
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")

#input from player
def playerInput(board):
    global currplayer
    i=int(input("Enter a number between 1-9 : "))
    if i>=1 and i<=9 and board[i-1] not in ['X', 'O']:
        board[i-1]=currplayer
        swapplayer()
    elif(i>9 or i<1):
        print("Enter a proper number")
    else:
        print("Oops player is already in that spot! ")

#check for winner
def checkwinner(board):
    global winner
    if board[0]==board[1]==board[2] and board[0] in ['X', 'O']:
        winner=board[0]
        return True
    if board[3]==board[4]==board[5] and board[3] in ['X', 'O']:
        winner=board[3]
        return True
    if board[6]==board[7]==board[8] and board[6] in ['X', 'O']:
        winner=board[6]
        return True
    if board[0]==board[4]==board[8] and board[0] in ['X', 'O']:
        winner=board[0]
        return True
    if board[2]==board[4]==board[6] and board[2] in ['X', 'O']:
        winner=board[2]
        return True
    if board[0]==board[3]==board[6] and board[0] in ['X', 'O']:
        winner=board[0]
        return True
    if board[1]==board[4]==board[7] and board[1] in ['X', 'O']:
        winner=board[1]
        return True
    if board[2]==board[5]==board[8] and board[2] in ['X', 'O']:
        winner=board[2]
        return True
    return False

#check for win
def checkwin():
    global gameRunning
    if all(cell in ['X', 'O'] for cell in board):
        if checkwinner(board):
            gameRunning=False
            printb(board)
            print(f"The winner is {winner}")
        else:
            gameRunning=False
            printb(board)
            print(f'It\'s a tie...')
        return
    if checkwinner(board):
        gameRunning=False
        printb(board)
        print(f"The winner is {winner}")

#swap the players
def swapplayer():
    global currplayer
    if currplayer=='X':
        currplayer='O'
    else:
        currplayer='X'

#choose the first player
def choose_first_player():
    global currplayer
    while True:
        choice = input("Choose the first player (X/O): ").upper()
        if choice in ['X', 'O']:
            currplayer = choice
            break
        else:
            print("Invalid choice. Please choose either 'X' or 'O'.")

#function calls until the game is running
choose_first_player()
while gameRunning:
    printb(board)
    playerInput(board)
    checkwin()


"""board=["1","2","3","4","5","6","7","8","9"]
currplayer = 'X'
winner=None
gameRunning=True

#print the board
def printb(board):
    print("| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
    print("--------------")
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
    print("--------------")
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |")

#input from player
def playerInput(board):
    global currplayer
    i=int(input("Enter a number between 1-9 : "))
    if i>=1 and i<=9 and board[i-1] not in ['X', 'O']:
        board[i-1]=currplayer
        swapplayer()
    elif(i>9 or i<1):
        print("Enter a proper number")
    else:
        print("Oops player is already in that spot! ")

#check for winner
def checkwinner(board):
    global winner
    if board[0]==board[1]==board[2] and board[0] in ['X', 'O']:
        winner=board[0]
        return True
    if board[3]==board[4]==board[5] and board[3] in ['X', 'O']:
        winner=board[3]
        return True
    if board[6]==board[7]==board[8] and board[6] in ['X', 'O']:
        winner=board[6]
        return True
    if board[0]==board[4]==board[8] and board[0] in ['X', 'O']:
        winner=board[0]
        return True
    if board[2]==board[4]==board[6] and board[2] in ['X', 'O']:
        winner=board[2]
        return True
    if board[0]==board[3]==board[6] and board[0] in ['X', 'O']:
        winner=board[0]
        return True
    if board[1]==board[4]==board[7] and board[1] in ['X', 'O']:
        winner=board[1]
        return True
    if board[2]==board[5]==board[8] and board[2] in ['X', 'O']:
        winner=board[2]
        return True
    return False

#check for win
def checkwin():
    global gameRunning
    if all(cell in ['X', 'O'] for cell in board):
        if checkwinner(board):
            gameRunning=False
            printb(board)
            print(f"The winner is {winner}")
        else:
            gameRunning=False
            printb(board)
            print(f'It\'s a tie...')
        return
    if checkwinner(board):
        gameRunning=False
        printb(board)
        print(f"The winner is {winner}")

#swap the players
def swapplayer():
    global currplayer
    if currplayer=='X':
        currplayer='O'
    else:
        currplayer='X'

#function calls until the game is running
while gameRunning:
    printb(board)
    playerInput(board)
    checkwin()


"""