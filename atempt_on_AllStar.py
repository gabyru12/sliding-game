import copy
from levels import *

board = [["0","1b1","0","0","2r1","3"],
           ["0","0","0","0","0","2g1"],
           ["0","3","0","3","0","1g1"],
           ["0","0","1r1","0","3","3"],
           ["3","0","0","0","0","3"],
           ["2b1","0","0","0","3","0"]]

#lista das peças usadas
def used_pieces(board):
    pieces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == "1":
                pieces.append(board[i][j])
    return pieces

#lista das winning points
def list_finish(board):
    pieces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == "2":
                pieces.append(board[i][j])
    return pieces

# Dá a posição de uma peça
def pos_pieces(boardstate):
    pos_pieces = {}
    for i in range(len(boardstate)):
        for j in range(len(boardstate)):
            if boardstate[i][j][0] == "1":
                pos_pieces[boardstate[i][j]] = (i,j)
    return pos_pieces

# Dá a posição das posições finais
def pos_finish(board):
    pos_finishes = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == "2":
                pos_finishes[board[i][j]] = (i,j)
    if len(pos_finishes) != 0:
        return pos_finishes
        
def solution_check(pieces,winning_points,pos_pieces,pos_finish):
    for i in range(len(pieces)):
        key = pieces[i]
        key1 = winning_points[i]
        if key[1] != key1[1]:
            return False
        elif pos_pieces[key] != pos_finish[key1]:
            return False
    return True

def update_finish(new_board,board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col][0] == "2" and new_board[row][col] == "0":
                    new_board[row][col] = board[row][col]

def check_moves(pos_pieces,pieces,board):
    moves_bool = {"move_up": False, "move_down": False, "move_left": False, "move_right": False}
    piece_positions = pos_pieces(board) #posição das peças usadas
    moves = [] #movimentos possíveis
    for i in range(len(pieces)):
        row,col = piece_positions[pieces[i]]
        if col-1 > -1 and board[row][col-1] != "3":
                moves_bool["move_left"] = True
        if col+1 < len(board) and board[row][col+1] != "3":
                moves_bool["move_right"] = True
        if row-1 > -1 and board[row-1][col] != "3":
                moves_bool["move_up"] = True
        if row+1 < len(board) and board[row+1][col] != "3":
                moves_bool["move_down"] = True
    for key,value in moves_bool.items():
        if value:
            moves.append(key)
    return moves

def pair_pieces_winning_point(used_pieces,list_finish,board):
    paired = []
    pieces = used_pieces(board)
    winning_points = list_finish(board)
    for piece in pieces:
        for finish in winning_points:
            if piece[1] == finish[1]:
                paired.append((piece,finish))
    return paired

def put_in_openBoardMoves(open_board_moves,check_moves,pieces,pos_pieces,newly_created_boardstate):
    if tuple(tuple(row) for row in newly_created_boardstate[0]) not in open_board_moves.keys():
        moves = check_moves(pos_pieces,pieces,newly_created_boardstate[0])
        open_board_moves[tuple(tuple(row) for row in newly_created_boardstate[0])] = (moves,newly_created_boardstate[1])
    newly_created_boardstate = None
    return open_board_moves,newly_created_boardstate

def simulate_move(counter,open_board_value,pair_pieces_winning_point,list_finish,used_pieces,open_board_moves,check_moves,pieces,winning_points,pos_pieces,pos_finish,newly_created_boardstate,put_in_openBoardMoves,board,solution):
    open_board_moves,newly_created_boardstate = put_in_openBoardMoves(open_board_moves,check_moves,pieces,pos_pieces,newly_created_boardstate)
    pos_of_winning_points = pos_finish(board)
    for tupled_parent_board, value in open_board_moves.items():
        moves = value[0]
        parent_board = list(list(row) for row in tupled_parent_board)
        for i in range(len(moves)):
            new_board = copy.deepcopy(parent_board)
            if moves[i] == "move_left":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if col-1 > -1 and new_board[row][col-1] != "3" and new_board[row][col-1][0] != "1":
                                    new_board[row][col-1] = new_board[row][col]
                                    new_board[row][col] = "0"
                    update_finish(new_board,board)  
            elif moves[i] == "move_right":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if col+1 < len(new_board) and new_board[row][col+1] != "3" and new_board[row][col+1][0] != "1":
                                    new_board[row][col+1] = new_board[row][col]
                                    new_board[row][col] = "0"
                    update_finish(new_board,board)  
            elif moves[i] == "move_up":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if row-1 > -1 and new_board[row-1][col] != "3" and new_board[row-1][col][0] != "1":
                                    new_board[row-1][col] = new_board[row][col]
                                    new_board[row][col] = "0"
                    update_finish(new_board,board)  
            elif moves[i] == "move_down":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if row+1 < len(new_board) and new_board[row+1][col] != "3" and new_board[row+1][col][0] != "1":
                                    new_board[row+1][col] = new_board[row][col]
                                    new_board[row][col] = "0"
                    update_finish(new_board,board)
            pieces_v2 = used_pieces(new_board)
            pos_of_pieces = pos_pieces(new_board)
            counter += 1
            if new_board not in visited_board_value:
                open_board_value = heuristic_calc(open_board_value,pair_pieces_winning_point,used_pieces,list_finish,pos_pieces,pos_finish,open_board_moves,moves[i],new_board,parent_board,board)
            if solution_check(pieces_v2,winning_points,pos_of_pieces,pos_of_winning_points):
                solution = True
                return open_board_value,open_board_moves,solution,counter
    open_board_moves.clear()
    return open_board_value,open_board_moves,solution,counter

def heuristic_calc(open_board_value,pair_pieces_winning_point,used_pieces,list_finish,pos_pieces,pos_finish,open_board_moves,move,new_board,parent_board,board):
    pairs = pair_pieces_winning_point(used_pieces,list_finish,board)
    pos_of_pieces = pos_pieces(new_board)
    pos_of_winning_points = pos_finish(board)
    tupled_board = tuple(tuple(row) for row in new_board)
    value = 0
    depth = open_board_moves[tuple(tuple(row) for row in parent_board)][1] + 1 
    for i in range(len(pairs)):
        x_piece,y_piece = pos_of_pieces[pairs[i][0]][0],pos_of_pieces[pairs[i][0]][1]
        x_winning_point,y_winning_point = pos_of_winning_points[pairs[i][1]][0],pos_of_winning_points[pairs[i][1]][1]
        value += abs(x_piece-x_winning_point)+abs(y_piece-y_winning_point)+depth
    if tupled_board not in open_board_value:
        open_board_value[tupled_board] = (parent_board,move,value,depth)
    elif tupled_board in open_board_value and value < open_board_value[tupled_board][2]:
        open_board_value[tupled_board] = (parent_board,move,value,depth)
    return open_board_value
                
def after_move(newly_created_boardstate,open_board_value,visited_board_value):
    list_of_different_values = []
    for i in open_board_value.values():
        list_of_different_values.append(i[2])
    lowest_value = min(list_of_different_values)
    for new_board in open_board_value.keys():
        if open_board_value[new_board][2] == lowest_value:
            parent_board = open_board_value[new_board][0]
            move = open_board_value[new_board][1]
            depth = open_board_value[new_board][3]
            newly_created_boardstate = ((list(list(row) for row in new_board), depth))
            visited_board_value.append(list(list(row) for row in new_board))
            history[(new_board,depth)] = (parent_board,move)
            del open_board_value[new_board]
            return newly_created_boardstate,visited_board_value,history


newly_created_boardstate = (board,0)
open_board_moves = {} 
open_board_value = {} 
visited_board_value = []
history = {}
pieces = used_pieces(board)
winning_points = list_finish(board)
solution = False
counter = 0


while not solution:
    open_board_value,open_board_moves,solution,counter = simulate_move(counter,open_board_value,pair_pieces_winning_point,list_finish,used_pieces,open_board_moves,check_moves,pieces,winning_points,pos_pieces,pos_finish,newly_created_boardstate,put_in_openBoardMoves,board,solution)
    newly_created_boardstate,visited_board_value,history = after_move(newly_created_boardstate,open_board_value,visited_board_value)
    print(counter)
    for row in newly_created_boardstate[0]:
        print(" ".join(row))
    print("\n")

for row in newly_created_boardstate[0]:
    print(" ".join(row))
print(f"Depth: {newly_created_boardstate[1]}")
print(f"Boards analized: {counter}")
