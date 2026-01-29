from tkinter import*
from tkinter import messagebox
top = Tk()

top.title("Tic-Tac-Toe")
top.geometry('700x600')
top.configure(bg="mistyrose")

l1=Label(top,text='Play With:', bg="mistyrose" , fg="gray25")
l1.grid(row=1,column=1)
l2=Label(top,text='Select:', bg="mistyrose" , fg="gray25")
l2.grid(row=2,column=1)
l3=Label(top,text='Start the game:', bg="mistyrose" , fg="gray25")
l3.grid(row=3,column=1)

v1=IntVar(value=-1)
v2=IntVar(value=-1)
v3=IntVar(value=-1)

r1=Radiobutton(top, text='Computer', variable=v1, value=1,bg="mistyrose", fg="gray25" )
r1.grid(row=1,column=2)
r2=Radiobutton(top, text='Player2', variable=v1, value=0 ,bg="mistyrose", fg="gray25")
r2.grid(row=1,column=3)

r3=Radiobutton(top, text='X', variable=v2, value=1, bg="mistyrose", fg="gray25")
r3.grid(row=2,column=2)
r4=Radiobutton(top, text='O', variable=v2, value=0, bg="mistyrose", fg="gray25")
r4.grid(row=2,column=3)

r5=Radiobutton(top, text='Yes', variable=v3, value=1, bg="mistyrose", fg="gray25")
r5.grid(row=3,column=2)
r6=Radiobutton(top, text='No', variable=v3, value=0,bg="mistyrose", fg="gray25")
r6.grid(row=3,column=3)


button={}
board = {i: ' ' for i in range(1, 10)}
turn = ['X']
play_with = 0  # 1=computer, 0=player2
player_symbol = 'X'
computer_symbol = 'O'
game_active = False

turn = ['X']

def press(num):
    global turn, game_active

    if not game_active:
        return

    if not is_space_free(num):
        messagebox.showwarning("Invalid", "This position is already taken!")
        return

    board[num] = turn[0]
    button[num]['text'] = turn[0]

    
    if check_win(turn[0]):
        messagebox.showinfo("Game Over", f"Player '{turn[0]}' wins!")
        ask_play_again()
        return
    elif check_draw():
        messagebox.showinfo("Game Over", "It's a Draw!")
        ask_play_again()
        return

    turn[0] = 'O' if turn[0] == 'X' else 'X'

    if play_with == 1 and turn[0] == computer_symbol:
        top.after(500, computer_turn)
        
def computer_turn():
    move = computer_move()
    if move is not None:
        press(move)

def start_game():
    global play_with, player_symbol, computer_symbol, turn, game_active

    play_with = v1.get()
    symbol = v2.get()
    start = v3.get()

    if play_with == -1 or symbol == -1 or start == -1:
        messagebox.showwarning('Missing Selection', 'Please select all options.')
        return

    if start == 0:
        messagebox.showinfo('Game', 'You chose not to start the game.')
        top.destroy()
        return

    
    if symbol == 1:
        player_symbol = 'X'
        computer_symbol = 'O'
    else:
        player_symbol = 'O'
        computer_symbol = 'X'

    turn[0] = player_symbol
    game_active = True

    
    for i in range(1, 10):
        button[i]['state'] = NORMAL
        button[i]['text'] = str(i)
        board[i] = ' '

    messagebox.showinfo('Game Started', 'Game Started!')


def ask_play_again():
    global game_active
    game_active = False
    again = messagebox.askyesno("Play Again", "Do you want to play again?")
    if again:
        reset_board()
    else:
        top.destroy()


def is_space_free(pos):
    return board[pos] == ' '

def check_win(letter):
    win_combos = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    return any(board[a] == board[b] == board[c] == letter for a, b, c in win_combos)

def check_draw():
    return all(board[i] != ' ' for i in board)  

def reset_board():
    global board, game_active
    board = {i: ' ' for i in range(1, 10)}
    for i in range(1, 10):
        button[i]['text'] = str(i)
        button[i]['state'] = DISABLED
    game_active = False

def computer_move():
    
    for i in range(1, 10):
        if is_space_free(i):
            copy = board.copy()
            copy[i] = computer_symbol
            if check_win_in_copy(copy, computer_symbol):
                return i
        for i in range(1, 10):
         if is_space_free(i):
            copy = board.copy()
            copy[i] = player_symbol
            if check_win_in_copy(copy, player_symbol):
                return i

    
    if is_space_free(5):
        return 5

    
    for i in [1, 3, 7, 9]:
        if is_space_free(i):
            return i

    
    for i in [2, 4, 6, 8]:
        if is_space_free(i):
            return i
    return None

def check_win_in_copy(copy_board, letter):
    combos = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    return any(copy_board[a] == copy_board[b] == copy_board[c] == letter for a, b, c in combos)

b1=Button(top, text="start",width=5 ,height=2, bg="gainsboro", fg="black",font=("Arial",14,"bold"),relief="raised",bd=5 ,command= start_game)
b1.grid(row=8,column=50 ,padx=30 ,pady=15)

for num in range(1,10):
     button[num]=Button(top,text=str(num),width=12,height=5 , state=DISABLED,command=lambda n=num: press(n), bg="gainsboro")
     
button[1].grid(row=19,column=19)
button[2].grid(row=19,column=20)
button[3].grid(row=19,column=21)
button[4].grid(row=20,column=19)
button[5].grid(row=20,column=20)
button[6].grid(row=20,column=21)
button[7].grid(row=21,column=19)
button[8].grid(row=21,column=20)
button[9].grid(row=21,column=21)

top.mainloop()