"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    else:
        count_x = 0
        count_o = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    count_x += 1
                elif board[i][j] == O:
                    count_o += 1
        if count_x > count_o:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
                
    return actions
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    copy = [row[:] for row in board]  # Create a deep copy of the board
    movement = player(board)
    copy[action[0]][action[1]] = movement
    return copy
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if verticalWin(board,X) or horizontalWin(board,X) or diagonalWin(board,X):
        return X
    elif verticalWin(board,O) or horizontalWin(board,O) or diagonalWin(board,O):
        return O
    else:
        return None

def verticalWin(board,symbol):
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    return False

def horizontalWin(board,symbol):
    for row in range(3):
        if all(cell == symbol for cell in board[row]):
            return True
    return False

def diagonalWin(board,symbol):
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return winner(board) is not None
    return True
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = -float('inf')
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v