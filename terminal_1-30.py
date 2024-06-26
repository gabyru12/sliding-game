from bfs import *
from levels import *
import copy

while True:
    level = input("What level would you like to play (1-30): ")
    if level == "exit":
        break
    level = int(level)
    while level < 0 or level > 30:
        print("This level doesn't exist.")
        level = int(input("Choose another: "))
    if level == 1:
        level = level1
    elif level == 2:
        level = level2
    elif level == 3:
        level = level3
    elif level == 4:
        level = level4
    elif level == 5:
        level = level5
    elif level == 6:
        level = level6
    elif level == 7:
        level = level7
    elif level == 8:
        level = level8
    elif level == 9:
        level = level9
    elif level == 10:
        level = level10
    elif level == 11:
        level = level11
    elif level == 12:
        level = level12
    elif level == 13:
        level = level13
    elif level == 14:
        level = level14
    elif level == 15:
        level = level15
    elif level == 16:
        level = level16
    elif level == 17:
        level = level17
    elif level == 18:
        level = level18
    elif level == 19:
        level = level19
    elif level == 20:
        level = level20
    elif level == 21:
        level = level21
    elif level == 22:
        level = level22
    elif level == 23:
        level = level23
    elif level == 24:
        level = level24
    elif level == 25:
        level = level25
    elif level == 26:
        level = level26
    elif level == 27:
        level = level27
    elif level == 28:
        level = level28
    elif level == 29:
        level = level29
    elif level == 30:
        level = level30

    winning_points = list_finish(level)
    pos_of_finish = pos_finish(level)
    pieces = used_pieces(level)
    new_board = copy.deepcopy(level)
    
    while True:
        solution_of_board = False
        pos_of_pieces = pos_pieces(new_board)
        for row in new_board:
            print(" ".join(row))
        print("\n")
        if solution_check(pieces,winning_points,pos_of_pieces,pos_of_finish):
            print ("GANHOU!")
            break
        move = input("Choose move (right, left, up, down): ")
        if move == "left":
            for k in range(len(new_board)):
                for row in range(len(new_board)):
                    for col in range(len(new_board)):
                        if new_board[row][col][0] == "1":
                            if col-1 > -1 and new_board[row][col-1] != "3" and new_board[row][col-1][0] != "1": 
                                new_board[row][col-1] = new_board[row][col]
                                new_board[row][col] = "0"
            update_finish(new_board,level) 
        elif move == "right":
            for k in range(len(new_board)):
                for row in range(len(new_board)):
                    for col in range(len(new_board)):
                        if new_board[row][col][0] == "1":
                            if col+1 < len(new_board) and new_board[row][col+1] != "3" and new_board[row][col+1][0] != "1": 
                                new_board[row][col+1] = new_board[row][col]
                                new_board[row][col] = "0"
            update_finish(new_board,level) 
        elif move == "up":
            for k in range(len(new_board)):
                for row in range(len(new_board)):
                    for col in range(len(new_board)):
                        if new_board[row][col][0] == "1":
                            if row-1 > -1 and new_board[row-1][col] != "3" and new_board[row-1][col][0] != "1": 
                                new_board[row-1][col] = new_board[row][col]
                                new_board[row][col] = "0"
            update_finish(new_board,level) 
        elif move == "down":
            for k in range(len(new_board)):
                for row in range(len(new_board)):
                    for col in range(len(new_board)):
                        if new_board[row][col][0] == "1":
                            if row+1 < len(new_board) and new_board[row+1][col] != "3" and new_board[row+1][col][0] != "1": 
                                new_board[row+1][col] = new_board[row][col]
                                new_board[row][col] = "0"
            update_finish(new_board,level)
        elif move == "back":
            break
        else:
            continue