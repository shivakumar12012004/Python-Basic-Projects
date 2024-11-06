board=["-","-","-","-","-","-","-","-","-"]
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
    if i>=1 and i<=9 and board[i-1]=="-":
        global currplayer
        board[i-1]=currplayer
        swapplayer()
    elif(i>9 or i<1):
        print("Enter an proper number")
    else:
        print("Oops player is already in that spot! ")

#check for winner
def checkwinner(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!='-':
        winner=board[0]
        return True
    if board[3]==board[4]==board[5] and board[3]!='-':
        winner=board[3]
        return True
    if board[6]==board[7]==board[8] and board[6]!='-':
        winner=board[6]
        return True
    if board[0]==board[4]==board[8] and board[0]!='-':
        winner=board[0]
        return True
    if board[2]==board[4]==board[6] and board[2]!='-':
        winner=board[2]
        return True
    if board[0]==board[3]==board[6] and board[0]!='-':
        winner=board[0]
        return True
    if board[1]==board[4]==board[7] and board[1]!='-':
        winner=board[1]
        return True
    if board[2]==board[5]==board[8] and board[2]!='-':
        winner=board[2]
        return True
    return False


#check for win
def checkwin():
    global gameRunning
    if '-' not in board:
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


#funtion calls until the game is running
while gameRunning:
    printb(board)
    playerInput(board)
    checkwin()