import random
board=['-','-','-','-','-','-','-','-','-']
currentplayer="x"
winner=None
gamerunning=True
def printboard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("------")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("------")
    print(board[6]+"|"+board[7]+"|"+board[8])
def playerinput(board):
    inp=int(input("select a spot between 1-9:"))
    if board[inp-1]=="-":
        board[inp-1]=currentplayer
    else:
        print("oops player is already at that spot")
        playerinput(board)
def checkhorizantal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[5]!="-":
        winner=board[5]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True
def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[4]
        return True
    elif board[2]==board[5]==board[8] and board[8]!="-":
        winner=board[8]
        return True
def checkdiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[6]!="-":
        winner=board[4]
        return True
def checkifwin(board):
    global gamerunning
    if checkhorizantal(board):
        printboard(board)
        print(f"the winner is {winner}")
        gamerunning=False
    elif checkrow(board):
        printboard(board)
        print(f"the winner is {winner}")
        gamerunning=False
    elif checkdiag(board):
        printboard(board)
        print(f"the winner is {winner}")
        gamerunning=False
def checkiftie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("it is a tie")
        gamerunning=False
def switchplayer():
    global currentplayer
    if currentplayer=="x":
        currentplayer="o"
    else:
        currentplayer="x"
def computer(board):
    while currentplayer=="o":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="o"
            switchplayer()
while gamerunning:
    printboard(board)
    playerinput(board)
    checkifwin(board)
    checkiftie(board)
    if gamerunning==True:
        switchplayer()
        computer(board)
        checkifwin(board)
        checkiftie(board)