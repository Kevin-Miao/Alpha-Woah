from agents import minimax_select_move, random_agent_select_move, is_winner, is_board_full

import random
import tqdm

def draw_board(board):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print("|".join(["O" if i == 1 else "X" if i == -1 else " " for i in board[0]]))
        print('-+-+-')
        print("|".join(["O" if i == 1 else "X" if i == -1 else " " for i in board[1]]))
        print('-+-+-')
        print("|".join(["O" if i == 1 else "X" if i == -1 else " " for i in board[2]]))
        
if __name__ == "__main__":
    agent1_select_move = random_agent_select_move
    agent2_select_move = minimax_select_move

    n_games = 200
    agent1_games_won = 0
    agent2_games_won = 0
    agent1_symbol, agent2_symbol = 1, -1

    for _ in tqdm.tqdm(range(n_games)):
        board = [[0 for _ in range(3)] for _ in range(3)]
        curr_player = 0 if random.random() < 0.5 else 1
        #print(f"current player is {'minimax' if curr_player == 0 else 'random'}")
    
        while any(0 in board[i] for i in range(3)) and not is_winner(board, agent1_symbol) and not is_winner(board, agent2_symbol):
            #draw_board(board)
            if curr_player == 0:
                move, _ = agent1_select_move(board)
                board[move//3][move%3] = agent1_symbol
            else:
                # we want to flip the board so the current player is 1 and the enemy is -1
                tmp = [[-j for j in i] for i in board]
                move, _ = agent2_select_move(tmp)
                board[move//3][move%3] = agent2_symbol

            curr_player = (curr_player+1)%2

        #draw_board(board)
        if is_winner(board, agent1_symbol):
            #print("MINIMAX WINS")
            agent1_games_won += 1
        
        if is_winner(board, agent2_symbol):
            #print("RANDOM WINS")
            agent2_games_won += 1

    print("Agent 1 games won: ", agent1_games_won)
    print("Agent 2 games won: ", agent2_games_won)
    print("Games drawn: ", n_games-agent1_games_won-agent2_games_won)
