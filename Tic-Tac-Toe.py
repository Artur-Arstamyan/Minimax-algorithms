import numpy as np
player, opponent = 'x', 'o'

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'x':
                return 10  
            elif board[i][0] == 'o':
                return -10
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'x':
                return 10  
            elif board[0][i] == 'o':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'x':
                return 10  
            elif board[0][0] == 'o':
                return -10
    if board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] == 'x':
                return 10  
            elif board[1][1] == 'o':
                return -10
    return 0

def isfull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

def minimax(board, depth, ismax):
    score = evaluate(board)
    if score == 10:
        return score-depth
    elif score == -10:
        return score+depth
    elif isfull(board):
        return 0
    if ismax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = player
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = '-'
        return best
    if not ismax:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = '-'
        return best

def minimax_alpha_beta(board, depth, ismax, a, b):
    score = evaluate(board)
    if score == 10:
        return score-depth
    elif score == -10:
        return score+depth
    elif isfull(board):
        return 0
    if ismax:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = player
                    a = max(a, minimax_alpha_beta(board, depth+1, False, a, b))
                    board[i][j] = '-'
                    if b <= a:
                        return a
        return a
    if not ismax:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = opponent
                    b = min(b, minimax_alpha_beta(board, depth+1, True, a, b))
                    board[i][j] = '-'
                    if b <= a:
                        return b
        return b

def findbestmove(board, ismax):
    best_move = (0, 0)
    if ismax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'x'
                    curr = minimax_alpha_beta(board, 1, False, -10000, 10000)
                    if best < curr:
                        best = curr
                        best_move = (i, j)
                    board[i][j] = '-'
        return best_move, best
    else: 
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'o'
                    curr = minimax_alpha_beta(board, 1, True, -10000, 10000)
                    if best > curr:
                        best = curr
                        best_move = (i, j)
                    board[i][j] = '-'
        return best_move, best

board = np.array([['-', '-', '-'],
                  ['x', 'o', 'x'],
                  ['-', '-', '-']])
steps = 10-abs(findbestmove(board, False)[1])
for k in range(steps):
    i, j = findbestmove(board, k%2)[0]
    board[i][j] = 'x' if k%2 else 'o'
    print(f'Best move is to put {board[i][j]} in board[{i}][{j}] cell')
    print(board)
    print()

##  Output
'''
Best move is to put o in board[0][0] cell
[['o' '-' '-']
 ['x' 'o' 'x']
 ['-' '-' '-']]

Best move is to put x in board[2][2] cell
[['o' '-' '-']
 ['x' 'o' 'x']
 ['-' '-' 'x']]

Best move is to put o in board[0][2] cell
[['o' '-' 'o']
 ['x' 'o' 'x']
 ['-' '-' 'x']]

Best move is to put x in board[0][1] cell
[['o' 'x' 'o']
 ['x' 'o' 'x']
 ['-' '-' 'x']]

Best move is to put o in board[2][0] cell
[['o' 'x' 'o']
 ['x' 'o' 'x']
 ['o' '-' 'x']]
 '''
