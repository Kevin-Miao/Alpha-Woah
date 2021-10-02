import random

def random_agent_select_move(board):
    all_moves = []
    for i in range(9):
        if board[i//3][i%3] == 0:
            all_moves.append(i)

    move = random.choice(all_moves)
    assert board[move//3][move%3] == 0
    
    move_probs = [0 for _ in range(9)]
    move_probs[move] = 1
    return move, move_probs
