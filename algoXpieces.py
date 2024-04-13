import copy
# Cria tabuleiro
board = [
    ["0","3","0","0","2g1"],
    ["3","0","0","3","1r1"],
    ["1g2","0","0","0","0"],
    ["0","3","0","0","0"],
    ["0","2r2","3","0","0"]
    ]

# lista das peças usadas                
def used_pieces(board):
    pieces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == "1":
                pieces.append(board[i][j])
    return pieces

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

def pos_finish(board):
    pos_finishes = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == "2":
                pos_finishes[board[i][j]] = (i,j)
    if len(pos_finishes) != 0:
        return pos_finishes
    return 0

# Dá a posição das posições finais
def pos_finish(board):
    pos_finishes = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == "2":
                pos_finishes[board[i][j]] = (i,j)
    if len(pos_finishes) != 0:
        return pos_finishes
    return 0

# Verifica se soução já foi encontrada
def solution_check(pieces,winning_points,pos_pieces,pos_finish):
    for i in range(len(pieces)):
        key = pieces[i]
        key1 = winning_points[i]
        if pieces[i][1] != winning_points[i][1]:
            return False
        elif pos_pieces[key] != pos_finish[key1]:
            return False
    return True

def update_finish(new_board,board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col][0] == "2" and new_board[row][col] == "0":
                    new_board[row][col] = board[row][col]

# Dá os movimentos possíveis
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

memo = [board]
memo1 = [] #memoriza estados do tabuleiro para dar print
visited = [board] 
history = {}
#counter = 0

#daqui pa cima deve tar fixe
#<---------------------------------------------------------------------------------->
#daqui pa baixo preciso acrescentar cenas

# Faz o movimento e retorna novos estados para memo1 
def do_move(used_pieces,list_finish,pos_finish,check_move, pos_piece,board,solution_check):
    global memo,memo1,counter
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
                print("Solução encontrada\n")
                break
    if memo1 == []:
        print("Solução não encontrada")
    counter += 1

def retrace_steps(history, visited, memo1):
    solution_path = [memo1[-1]]
    moves = []
    for i in range(len(visited)-1, -1, -1):
        tupled_board = tuple(tuple(row) for row in visited[i])
        tupled_solution_path = tuple(tuple(row) for row in solution_path[-1])
        if tupled_board in history:
            if tupled_board == tupled_solution_path:
                print(i)
                solution_path.append(history[tupled_board][0])
                moves.append(history[tupled_board][1])
    solution_path.reverse()
    moves.reverse()
    return solution_path, moves

#print do tabuleiro para análise
def print_board(memo):
        for row in memo:
            print("  ".join(row))
        print("\n")

print("Initial Board:")
#print_board(memo)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)
do_move(used_pieces,list_finish,pos_finish,check_move,pos_pieces,board,solution_check)

solution_path,moves = retrace_steps(history, visited, memo1)
print(len(visited))
print(len(history))
for i in range(len(solution_path)):
    print_board(solution_path[i])
print(moves)
