#simple python program for tic_tac_toe game

won = False
board = ["","","","","","","","",""]

#get input
def get_input(player):
    n = int(input("Enter a number (1-9) :"))
    mark_board(n,player)

def mark_board(n,player):
    board[n-1] = player
    display_board()

def check_board(player):
    #rules
    #horizontal
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player)):
        won = True
    #vertical
    elif ((board[0] == player and board[3] == player and board[6] == player) or
         (board[1] == player and board[4] == player and board[7] == player) or
         (board[2] == player and board[5] == player and board[8] == player)):
         won = True
    #cross
    elif ((board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):
        won = True
    else:
        won = False
    return won

def display_board():
    print(
        """
          {}  | {}  | {}
        ----------
          {}  | {}  | {}
        ----------
          {}  | {}  | {}
        """.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])
    )

def game():
    player = "X"
    while (won == False):
        print(player,"turn :")
        #get input
        get_input(player)
        #check board
        is_won = check_board(player=player)
        if is_won == True:
            print(player,"Won")
            break
        #change player
        if player == "X":
            player = "O"
        else:
            player = "X"
game()