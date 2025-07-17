board = ["1","2","3","4","5","6","7","8","9"]
m = True
def create():
    for i in range(3):
        for j in range(3):
            a = i * 3 + j

            print("|",board[a],"|",end=" ")
        print()
    
def adding_x():
    while True:
        
        X = int(input("Player 1 enter your move: "))-1
        if board[X] not in ["X","O"]:
            board[X]="X"
            create()
            if board[0]== board[1]==board[2] or board[0]==board[3]==board[6] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]or board[2]==board[5]==board[8] or board[1]==board[4]==board[7] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]:
                print("You won")
                exit()
            break
    else:
        print("Invalid move, try again")

def adding_o():
    while True:
        O = int(input("Player 2 enter your move: "))-1
        if board[O] not in ["X","O"]:
            board[O]="O"
            create()
            if board[0]== board[1]==board[2] or board[0]==board[3]==board[6] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]or board[2]==board[5]==board[8] or board[1]==board[4]==board[7] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8]:
                print("Second player won!")
                exit()
            break
                
        else:
            print("Invalid move, try again")
def draw():
    draw_check = True
    for i in board:
        if i not in ["X","O"]:
            draw_check=False
            break
    if draw_check:
        print("It's a draw")
        create()
        exit()

def combine():
    adding_x()
    draw()
    adding_o()
    draw()

while m:
    combine()
    
    


    
