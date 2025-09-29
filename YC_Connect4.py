"""
Author: Yuanseng Choo
Date: 2025-09-28
Program: Connect Four (console)

Overview:
- 6x7 Connect Four with gravity.
- Shows available landing cells (e.g., a1 means column a, bottom row).
- Validates input, enforces gravity, detects wins (4-in-a-row) and draw, and offers replay.
"""

import re

# Displays the game board, rows shown 6 down to 1

def printBoard(board):
    horiz = " " + "-" * 33
    print(horiz)
    for r in range(6, 0, -1):
        # r-1 maps visual row (6..1) to board index (5..0)
        cells = " | ".join(board[r-1][c] for c in range(7))
        print(f"| {r} | {cells} |")
        print(horiz)
    print("|R\\C| a | b | c | d | e | f | g |")
    print(horiz)
    print()

# Create a new empty 6x7 board
def resetBoard(board):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            board[r][c] = " "

# Validate if the move is within bounds and cell is empty
def validateEntry(board, col, row):
    if not board[row][col] == " ":
        print("Invalid entry: try again.\n")  
        return False
    if row > 0:
        if board[row-1][col] == " ":
            print("Invalid entry: try again.\n")  
            return False        
    return True

# Check if the board is completely full
def checkFull(board):
    """Return True if there are no empty cells on the board."""
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == " ":
                return False
    return True

def availablePosition(board):
    """
    Returns a list like ['a1','b1','c2', ...] showing the next landing
    cell for each non-full column (lowest empty slot).
    """
    rows, cols = len(board), len(board[0])
    letters = "abcdefg"
    out = []
    for c_idx in range(cols):
        landing_r = None
        for rr in range(0, rows):
            if board[rr][c_idx] == " ":
                landing_r = rr
                break
        if landing_r is not None:
            out.append(f"{letters[c_idx]}{landing_r+1}")
    return out

# Check 4-in-a-row in four directions: right, down, diag down-right, diag down-left
def checkWin(board, turn):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] != turn:
                continue
            # right (0, +1)
            if c + 3 < cols and all(board[r][c + k] == turn for k in range(4)):
                return True
            # down (+1, 0)
            if r + 3 < rows and all(board[r + k][c] == turn for k in range(4)):
                return True
            # diag down-right (+1, +1)
            if r + 3 < rows and c + 3 < cols and all(board[r + k][c + k] == turn for k in range(4)):
                return True
            # diag down-left (+1, -1)
            if r + 3 < rows and c - 3 >= 0 and all(board[r + k][c - k] == turn for k in range(4)):
                return True
    return False

# Check if game has ended and print appropriate message
def checkEnd(board, turn):
    if checkWin(board, turn):
        print(f"{turn} IS THE WINNER!!!\n")
        return True
    if checkFull(board):
        print("DRAW! NOBODY WINS!\n")
        return True
    return False

# Main game loop
def main():
    again = "y"
    while again.lower() == "y":
        # fixed 6x7 board for Connect Four
        board = [[" " for _ in range(7)] for _ in range(6)]
        resetBoard(board)

        turn = "X"  

        print()
        print("New Game: X goes first")
        print()
        printBoard(board)

        while True:
            print(f"{turn}'s turn.")
            print(f"Where do you want your {turn} placed?")
            avail = availablePosition(board)
            print(f"Available positions are: {avail}")
            print()

            # parse inputs like "a1"
            raw = input("Please enter column-letter and row-number (e.g., a1): ").strip()

            m = re.fullmatch(r"\s*([a-gA-G])\s*([1-6])\s*", raw)
            if not m:
                print("Invalid entry: try again.\n")
                continue

            col = m.group(1).lower()
            row = int(m.group(2))

            letters = "abcdefg"
            c_idx = letters.index(col)
            # validate (function prints its own error if invalid)
            if not validateEntry(board, c_idx, row-1):
                continue

            # place token at the landing row of that column (no ord())

            board[row-1][c_idx] = turn

            print("Thank you for your selection.\n")
            printBoard(board)

            # end-of-game check (function prints winner/draw)
            if checkEnd(board, turn):
                break

            turn = "X" if turn == "O" else "O"

        again = input("Another game? Enter Y or y for yes: ").strip()
        print()

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
