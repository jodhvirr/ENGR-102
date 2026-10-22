# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 8Bonus
# Date:         17 October 2026

# Storing a chess board in a list of lists.
chess_board = [
              ["R", "N", "B", "Q", "K", "B", "N", "R"], 
              ["P", "P", "P", "P", "P", "P" , "P", "P"],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."],
              ["p", "p", "p", "p", "p", "p" , "p", "p"],
              ["r", "n", "b", "q", "k", "b", "n", "r"],
              ]


running = True

while(running):
    
# Chess board displayed before every move.
    for i in range(8):
        for j in range(8):
            print(chess_board[i][j], end = " ")
        print()
         
    r_piece = int(input("What row is the piece currently in?: "))
    c_piece = int(input("What column is the piece currently in?: "))
    
    r_move = int(input("What row do you want to move that piece to?: "))
    c_move = int(input("What column do you want to move that piece to?: "))
    
    if r_piece not in range(8) or c_piece not in range(8) or r_move not in range(8) or c_move not in range(8):
        print("Invalid move! One of the rows/columns doesn't exist. ")
        break
    
    if not chess_board[r_piece][c_piece] == ".":
        # Valid moves update board correctly.
        chess_board[r_move][c_move] = chess_board[r_piece][c_piece]
        chess_board[r_piece][c_piece] = "."
    else:
        # Invalid moves (empty starting square) recognized, and error reported.
        print("Invalid move! There wasn't a piece at that specific row and column. ")
        break


