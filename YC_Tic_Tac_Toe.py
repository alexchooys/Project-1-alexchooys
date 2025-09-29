"""
Author: Yuanseng Choo
Date: 2025-09-28
Program: Tic-Tac-Toe (console)

Overview:
- Starts a new Tic-Tac-Toe game with X going first.
- Prompts players for row and column input (0-2).
- Validates input and occupied cells.
- Updates and prints the board after each valid move.
- Detects wins (rows, columns, diagonals) and draws.
- Offers replay at the end.
"""

import re

# Display the current game board
def printBoard(board):
    # Column
    print("------------------")
    print("|R\\C| 0 | 1 | 2 |")
    print("------------------")

    # Row
    for r in range(3):
        print(f"| {r} | {board[r][0]} | {board[r][1]} | {board[r][2]} |")
        print("------------------")
    print()

# Create a new empty board
def resetBoard(board):
    for r in range(3):
        for c in range(3):
            board[r][c] = " "

# Validate if the move is within bounds and cell is empty
def validateEntry(row, col, board):
    # range first
    if not (0 <= row <= 2 and 0 <= col <= 2):
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1, or 2.")
        return False 
    if board[row][col] != " ":
        print("That cell is already taken.")
        print("Please make another selection.")
        return False
    return True


# Check if the board is completely filled
def checkFull(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True

# Check if the current player has won
def checkWin(board, turn):
    # rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == turn:
            return True
    # cols
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == turn:
            return True
    # diags
    if board[0][0] == board[1][1] == board[2][2] == turn:
        return True
    if board[0][2] == board[1][1] == board[2][0] == turn:
        return True
    return False

# Check if the game has ended (win or draw)
def checkEnd(board, turn):
    if checkWin(board, turn):
        print(f"{turn} IS THE WINNER!!!")
        return True
    if checkFull(board):
        print("DRAW! NOBODY WINS!")
        return True
    return False
     
# Main game loop
def main():
    again = 'y'
    while again.lower() == 'y':

        # New game setup
        board = [[" " for _ in range(3)] for _ in range(3)]
        print()
        print("New Game: X goes first.")
        print()
        printBoard(board)

        turn = "X"

        # In-game loop
        while True:
            print(f"{turn}'s turn.")
            print(f"Where do you want your {turn} placed?")
            print("Please enter row number and column number separated by a comma.")

            while True:
                raw = input().strip()   # get player input

                # If the user entered nothing or only spaces, re-prompt
                if not raw:
                    print("Invalid entry: try again.")
                    print("Row & column numbers must be either 0, 1, or 2.")
                    print()
                    print(f"{turn}'s turn.")
                    print(f"Where do you want your {turn} placed?")
                    print("Please enter row number and column number separated by a comma.")
                    continue

                # Split on either a comma or any whitespace (one or more)
                parts = [t for t in re.split(r"[,\s]+", raw) if t]

                # Handle one-taken inputs cleanly
                if len(parts) == 1:
                    only = parts[0]
                    if only.isdigit():
                        print(f"You entered only one number: {only}")
                        print("Please enter two numbers 0, 1, or 2, for example: 1,2")
                    else:
                            print(f"You entered only one alphabet: {only}")
                            print("Use numbers 0, 1, or 2, for example: 1,2")
                    print()
                    print(f"{turn}'s turn.")
                    print(f"Where do you want your {turn} placed?")
                    print("Please enter row number and column number separated by a comma or space.")
                    continue

                # Validate we got exactly two numeric tokens
                row1 = str(parts[0])
                col1 = str(parts[1])
                if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                    print(f"You have entered row #{row1}")
                    print(f"{'and column':>20} #{col1}")
                    print("Invalid entry: try again.")
                    print("Row & column numbers must be either 0, 1, or 2.")
                    print()
                    print(f"{turn}'s turn.")
                    print(f"Where do you want your {turn} placed?")
                    print("Please enter row number and column number separated by a comma.")
                    continue
                
                row = int(parts[0])
                col = int(parts[1])
                print(f"You have entered row #{row}")
                print(f"{'and column':>20} #{col}")

                # Validate coordinates and occupancy
                if not validateEntry(row, col, board):
                    print()
                    print(f"{turn}'s turn.")
                    print(f"Where do you want your {turn} placed?")
                    print("Please enter row number and column number separated by a comma.")
                    continue

                print("Thank you for your selection.")
                print()
                board[row][col] = turn
                break # exit input loop; proceed to end checks and next turn

            # End-of-game check and board print
            if checkEnd(board, turn):
                print()
                printBoard(board)
                break

            printBoard(board)
            # Switch turns
            # turn = "O" if turn == "X" else "X"
            if turn == "X":
                turn = "O"             
            else:
                turn = "X"

        # Replay 
        print()
        again = input("Another game? Enter Y or y for yes.\n").strip()
        print()

    print("Thank you for playing!")

if __name__ == "__main__":
    main()