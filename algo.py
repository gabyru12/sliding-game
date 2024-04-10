import copy
# Cria tabuleiro
board = [["0" for _ in range(4)] for _ in range(4)]
board[2][2] = "1" #start
#board[0][0] = "2" #finish
#board[2][0], board[3][3] = "3","3" #obstacles

# Dá a posição de uma peça
def pos_piece(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "1":
                return i, j

def pos_finish(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "2":
                return i, j

def solution_check(pos_piece,pos_finish,board1,board): 
    if pos_piece(board1) == pos_finish(board):
        return True
    return False

# Dá os movimentos possíveis
def check_move(pos_piece,board):
    moves_bool = {"move_up": False, "move_down": False, "move_left": False, "move_right": False}
    row, col = pos_piece(board)
    moves = []
    if col != 0: 
        if board[row][col-1] != "3":
            moves_bool["move_left"] = True
    if col != len(board)-1: 
        if board[row][col+1] != "3":
            moves_bool["move_right"] = True
    if row != 0: 
        if board[row-1][col] != "3":
            moves_bool["move_up"] = True
    if row != len(board)-1: 
        if board[row+1][col] != "3":
            moves_bool["move_down"] = True
    for key,value in moves_bool.items():
        if value:
            moves.append(key)
    return moves

memo = [board]
memo1 = [] #memoriza estados do tabuleiro para dar print
visited = [] 
counter = 0

# Faz o movimento e retorna novos estados para memo1 
def do_move(check_move, pos_piece):
    global memo,memo1,counter
    flag = False
    if len(memo1) != 0:    
        memo = copy.deepcopy(memo1)
        memo1 = []
    for i in range(len(memo)):
        if flag:
            break
        row_piece, col_piece = pos_piece(memo[i])
        moves = check_move(pos_piece,memo[i])
        for j in range(len(moves)):
            board1 = copy.deepcopy(memo[i])
            if moves[j] == "move_up":
                board1[row_piece][col_piece] = "0"
                for row in range(row_piece, -1,-1):
                    if row == 0:
                        board1[row][col_piece] = "1"
                        break
                    if board1[row-1][col_piece] == "3":
                        board1[row][col_piece] = "1"
                        break
                if board1 in visited:
                    continue
                else:
                    visited.append(board1)
                memo1.append(board1)
            elif moves[j] == "move_down":
                board1[row_piece][col_piece] = "0"
                for row in range(row_piece, len(board1),1):
                    if row == len(board1)-1:
                        board1[row][col_piece] = "1"
                        break
                    if board1[row+1][col_piece] == "3":
                        board1[row][col_piece] = "1"
                        break
                if board1 in visited:
                    continue
                else:
                    visited.append(board1)
                memo1.append(board1)
            elif moves[j] == "move_left":
                board1[row_piece][col_piece] = "0"
                for col in range(col_piece, -1,-1):
                    if col == 0:
                        board1[row_piece][col] = "1"
                        break
                    if board1[row_piece][col-1] == "3":
                        board1[row_piece][col] = "1"
                        break
                if board1 in visited:
                    continue
                else:
                    visited.append(board1)                    
                memo1.append(board1)
            elif moves[j] == "move_right":
                board1[row_piece][col_piece] = "0"
                for col in range(col_piece, len(board1),1):
                    if col == len(board1)-1:
                        board1[row_piece][col] = "1"
                        break
                    if board1[row_piece][col+1] == "3":
                        board1[row_piece][col] = "1"
                        break
                if board1 in visited: 
                    continue
                else: 
                    visited.append(board1)
                memo1.append(board1)
            if solution_check(pos_piece,pos_finish,board1,board): 
                flag = True
                print("Solução encontrada\n")
                break
    counter += 1
                
#print do tabuleiro para análise
def print_board(memo):
    for i in range(len(memo)):
        print(f"{i+1}\n")
        for row in memo[i]:
            print(" ".join(row))
        print("\n")

print("Initial Board:")
print_board(memo)
do_move(check_move, pos_piece) #primeira transformação
#do_move(check_move, pos_piece) #segunda transformação
#do_move(check_move, pos_piece) #segunda transformação
print(f"counter: {counter}\n")
print_board(memo1)

