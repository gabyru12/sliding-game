import copy
from levels import *

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
        for j in range(len(board)):
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
        for j in range(len(board)):
            if board[i][j][0] == "2":
                pos_finishes[board[i][j]] = (i,j)
    if len(pos_finishes) != 0:
        return pos_finishes
    return 0

#Verifica se o estado currente é solução
def solution_check(pieces,winning_points,pos_pieces,pos_finish):
    for i in range(len(pieces)):
        key = pieces[i]
        key1 = winning_points[i]
        if pieces[i][1] != winning_points[i][1]:
            return False
        elif pos_pieces[key] != pos_finish[key1]:
            return False
    return True

#No caso de uma peça estiver em cima do winning point, o winning point vai desaparecer da matriz do tabuleiro e para que no caso de a peça sair do local winning point, esta função irá garantir que ele apareça de novo
def update_finish(new_board,board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col][0] == "2" and new_board[row][col] == "0":
                    new_board[row][col] = board[row][col]

# Dá os movimentos possíveis num estado
def check_move(pos_pieces,pieces,new_board,board):
    moves_bool = {"move_up": False, "move_down": False, "move_left": False, "move_right": False}
    piece_positions = pos_pieces(new_board) #posição das peças usadas
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


# Faz o movimento e retorna novos estados para memo1 
def do_move(boards_analized,used_pieces,list_finish,pos_finish, check_move, pos_pieces,board,solution_check,memo,memo1,visited,history,solution,solution_not_found):
    flag = False
    pieces = used_pieces(board)
    finish = list_finish(board)
    finish_position = pos_finish(board)
    if len(memo1) != 0:    
        memo = copy.deepcopy(memo1)
        memo1 = []
    for i in range(len(memo)):
        if flag:
            break
        moves = check_move(pos_pieces,pieces,memo[i],board)
        for j in range(len(moves)):
            new_board = copy.deepcopy(memo[i])
            if moves[j] == "move_up":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if row-1 > -1 and new_board[row-1][col] != "3" and new_board[row-1][col][0] != "1": 
                                    new_board[row-1][col] = new_board[row][col]
                                    new_board[row][col] = "0"
                    update_finish(new_board,board)    
            elif moves[j] == "move_down":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if row+1 < len(board) and new_board[row+1][col] != "3" and new_board[row+1][col][0] != "1": 
                                    new_board[row+1][col] = new_board[row][col]
                                    new_board[row][col] = "0" 
                    update_finish(new_board,board)   
            elif moves[j] == "move_left":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if col-1 > -1 and new_board[row][col-1] != "3" and new_board[row][col-1][0] != "1":
                                    new_board[row][col-1] = new_board[row][col]
                                    new_board[row][col] = "0"
                    update_finish(new_board,board)    
            elif moves[j] == "move_right":
                for k in range(len(new_board)):
                    for row in range(len(new_board)):
                        for col in range(len(new_board)):
                            if new_board[row][col][0] == "1":
                                if col+1 < len(board) and new_board[row][col+1] != "3" and new_board[row][col+1][0] != "1": 
                                    new_board[row][col+1] = new_board[row][col]
                                    new_board[row][col] = "0"    
                    update_finish(new_board,board)
            boards_analized += 1
            if new_board in visited:
                    continue
            else:
                visited.append(new_board)
                memo1.append(new_board)
                pieces = used_pieces(new_board)
                piece_postition = pos_pieces(new_board)
                history[tuple(tuple(row) for row in new_board)] = (memo[i],moves[j]) 
            if solution_check(pieces,finish,piece_postition,finish_position):
                flag = True
                solution = True
                print("\nSolução encontrada\n")
                break
    if memo1 == []:
        print("\nSolução não encontrada\n")
        solution_not_found = True
    return memo,memo1,visited,history,solution,solution_not_found,boards_analized

#dá a lista de movimentos realizados e a sequência de estados até encontrar a solução
def retrace_steps(history, visited, memo1):
    solution_path = [memo1[-1]]
    moves = []
    for i in range(len(visited)-1, -1, -1):
        tupled_board = tuple(tuple(row) for row in visited[i])
        tupled_solution_path = tuple(tuple(row) for row in solution_path[-1])
        if tupled_board in history:
            if tupled_board == tupled_solution_path:
                solution_path.append(history[tupled_board][0])
                moves.append(history[tupled_board][1])
    solution_path.reverse()
    moves.reverse()
    return solution_path, moves

#onde a magia acontece
def breath_first_search(do_move,used_pieces,list_finish,pos_finish,check_move, pos_pieces,solution_check,board):
    memo = [board]
    memo1 = []
    visited = [board] 
    history = {}
    counter = 0
    boards_analized = 0
    solution = False
    solution_not_found = False
    while solution == False and solution_not_found == False:
        memo,memo1,visited,history,solution,solution_not_found,boards_analized = do_move(boards_analized,used_pieces,list_finish,pos_finish,check_move, pos_pieces, board,solution_check,memo,memo1,visited,history,solution,solution_not_found)
        counter +=1
    if memo1 != []:
        solution_path,moves = retrace_steps(history, visited, memo1) 
    else:
        moves = None
        solution_path = None
    return counter,moves,solution_path,boards_analized