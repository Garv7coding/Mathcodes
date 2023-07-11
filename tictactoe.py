currentplayer = "X"
# counter = 9

board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]


def instructions():
    print("Welcome to Noughts and Crosses!"
          "\nInstructions:"
          "\n1. Player one has noughts and player 2 has crosses"
          "\n2. You have to enter co-ordinates of your move for your symbol to be positioned")
    return " "


def win(board1, board):
    if board[0][0] == board[0][1] == board[0][2] == "X":
        print("Player1 Wins!")
        exit()
    elif board[0][0] == board[0][1] == board[0][2] == "0":
        print("Player2 Wins!")
        exit()
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("Player1 Wins!")
        exit()
    elif board[1][0] == "0" and board[1][1] == "0" and board[1][2] == "0":
        print("Player2 Wins!")
        exit()
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("Player1 Wins!")
        exit()
    elif board[2][0] == "0" and board[2][1] == "0" and board[2][2] == "0":
        print("Player2 Wins!")
        exit()
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player1 Wins!")
        exit()
    elif board[0][0] == "0" and board[1][1] == "0" and board[2][2] == "0":
        print("Player2 Wins!")
        exit()
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player1 Wins!")
        exit()
    elif board[0][2] == "0" and board[1][1] == "0" and board[2][0] == "0":
        print("Player2 Wins!")
        exit()
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("Player1 Wins!")
        exit()
    elif board[0][0] == "0" and board[0][1] == "0" and board[0][2] == "0":
        print("Player2 Wins!")
        exit()
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("Player1 Wins!")
        exit()
    elif board[0][1] == "0" and board[1][1] == "0" and board[2][1] == "0":
        print("Player2 Wins!")
        exit()
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("Player1 Wins!")
        exit()
    elif board[0][2] == "0" and board[1][2] == "0" and board[2][2] == "0":
        print("Player2 Wins!")
        exit()
    # elif all(board == "x" or "0" for item in board):
    # print("It's a draw")
    # exit()
    # else:
    # print(" Next turn")
    # print(player())


def player():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "0"
        print(move2(board, player))
    elif currentplayer == "0":
        currentplayer = "X"
        print(move1(board, player))


def board1(board):
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
    print(" ───┼───┼───")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
    print(" ───┼───┼───")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2])


def spaceleftcheck():
    global game
    spaces = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
                spaces = spaces + 1
                if spaces == 0:
                    print("Game is draw")
                    return " "
                    exit()


def move1(board, player):
    print("This is player X's turn'")
    p1inp = int(input("Where would you like to place your symbol, enter a number corresponding that on the board:"))
    if p1inp > 9:
        print("try again")
        print(move1(board, player))
    else:
        if p1inp == 1:
            board[0][0] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 2:
            board[0][1] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 3:
            board[0][2] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 4:
            board[1][0] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 5:
            board[1][1] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 6:
            board[1][2] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 7:
            board[2][0] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 8:
            board[2][1] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))
        if p1inp == 9:
            board[2][2] = "X"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move2(board, player))


def move2(board, player):
    print("This is player 0 's turn'")
    p1inp = int(input("Where would you like to place your symbol, enter a number corresponding that on the board:"))
    if p1inp > 9:
        print("try again")
        print(move2(board, player))
    else:
        if p1inp == 1:
            board[0][0] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 2:
            board[0][1] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 3:
            board[0][2] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 4:
            board[1][0] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 5:
            board[1][1] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 6:
            board[1][2] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 7:
            board[2][0] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 8:
            board[2][1] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))
        if p1inp == 9:
            board[2][2] = "0"
            print(board1(board))
            print(win(board1, board))
            print(spaceleftcheck())
            print(player())
            print(move1(board, player))


def main():
    print(instructions())
    print(board1(board))
    print(move1(board, player))


if __name__ == "__main__":
    main()

