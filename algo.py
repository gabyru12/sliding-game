import copy
# Cria tabuleiro
board = [["0" for _ in range(4)] for _ in range(4)]
board[2][3] = "1"

# Dá a posição de uma peça
def pos_piece(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "1":
                return i, j

# Dá os movimentos possíveis
def check_move(pos_piece,board):
    moves_bool = {"move_up": False, "move_down": False, "move_left": False, "move_right": False}
    row, col = pos_piece(board)
    moves = []
    if col != 0:
        moves_bool["move_left"] = True
    if col != 3:
        moves_bool["move_right"] = True
    if row != 0:
        moves_bool["move_up"] = True
    if row != 3:
        moves_bool["move_down"] = True
    for key,value in moves_bool.items():
        if value:
            moves.append(key)
    return moves

memo = [board]
memo1 = [] #memoriza estados do tabuleiro para dar print

# Faz o movimento e retorna novos estados para memo1 
def do_move(check_move, pos_piece):
    global memo,memo1
    if len(memo1) != 0:    
        memo = copy.deepcopy(memo1)
        memo1 = []
    for i in range(len(memo)):
        row, col = pos_piece(memo[i])
        moves = check_move(pos_piece,memo[i])
        for j in range(len(moves)):
            board1 = copy.deepcopy(memo[i])
            if moves[j] == "move_up":
                board1[row][col], board1[0][col] = "0", "1"
                memo1.append(board1)
            elif moves[j] == "move_down":
                board1[row][col], board1[3][col] = "0", "1"
                memo1.append(board1)
            elif moves[j] == "move_left":
                board1[row][col], board1[row][0] = "0", "1"
                memo1.append(board1)
            elif moves[j] == "move_right":
                board1[row][col], board1[row][3] = "0", "1"
                memo1.append(board1)

#print do tabuleiro para análise
def print_board(memo):
    for i in range(len(memo)):
        print(f"{i+1}\n")
        for row in memo[i]:
            print(" ".join(row))
        print("\n")

print("Initial Board:")
print_board(memo)

print("\nPossible Moves:")
print(check_move(pos_piece,board))

print("\nBoard after move:")
do_move(check_move, pos_piece) #primeira transformação
do_move(check_move, pos_piece) #segunda transformação
print_board(memo1)
