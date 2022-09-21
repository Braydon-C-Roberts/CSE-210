# Tic-Tac-Toe
# By Braydon Roberts


def main():
    playAgain = "y"
    while playAgain == "y":
        print("GLHF!")
        player = whosTurn("")
        board = createGameBoard()
        while not (gameOver(board)):
            displayGameBoard(board)
            playerMove(player, board)
            player = whosTurn(player)
        displayGameBoard(board)
        print("GG!")
        print()
        playAgain = input("play again [Y/N]: ")
        playAgain = playAgain.lower()

def createGameBoard():
    board = []
    for space in range(9):
        board.append(space + 1)
    return board

def displayGameBoard(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def whosTurn(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    print()

def playerMove(player, board):
    space = int(input(f"{player}'s turn. Choose a space (1-9): "))
    if space >= 1 and space <= 9:
        board[space - 1] = player
    else:
        print("Invalid input. Try again")
        playerMove(player, board)

def gameOver(board):
    for space in range(9):
        if (((board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])) or
            (board[space] == "x" and board[space] == "o")):
            return True
        return False
    
if __name__ == "__main__":
    main()