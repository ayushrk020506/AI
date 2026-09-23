board = [
    "O", " ", "X",
    "X", " ", " ",
    "X", "O", "O"
]

cost = 0

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False

def board_full():
    return " " not in board

def robot_move():
    global cost

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            cost += 1
            print("Robot placed X at position", i + 1)
            print("Path Cost:", cost)
            return

display_board()

while True:

    robot_move()
    display_board()

    if check_winner("X"):
        print("Robot Wins!")
        print("Final Path Cost:", cost)
        break

    if board_full():
        print("Draw!")
        print("Final Path Cost:", cost)
        break

    position = int(input("Enter your position for O (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid position")
        continue
    
    board[position] = "O"
    cost += 1

    display_board()

    if check_winner("O"):
        print("User Wins!")
        print("Final Path Cost:", cost)
        break

    if board_full():
        print("Draw!")
        print("Final Path Cost:", cost)
        break