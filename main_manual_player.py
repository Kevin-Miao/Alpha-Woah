from minimax import minimax_select_move, is_winner, is_board_full

def draw_board(board):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print("|".join(["O" if i == 1 else "X" if i == -1 else " " for i in board[0]]))
        print('-+-+-')
        print("|".join(["O" if i == 1 else "X" if i == -1 else " " for i in board[1]]))
        print('-+-+-')
        print("|".join(["O" if i == 1 else "X" if i == -1 else " " for i in board[2]]))

def get_player_move(board):
    # Let the player type in their move.
    move = '' 
    while move not in range(9) or board[int(move)//3][int(move)%3] != 0:
        print('What is your next move? (0-8)')
        move = int(input())
    return move

if __name__ == "__main__":
    # Reset the board
    theBoard = [[0 for _ in range(3)] for _ in range(3)]
    playerLetter, computerLetter = -1, 1
    # Player always goes first
    turn = "player"
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            draw_board(theBoard)
            move = get_player_move(theBoard)
            theBoard[move//3][move%3] = playerLetter

            if is_winner(theBoard, playerLetter):
                draw_board(theBoard)
                print('You won the game')
                gameIsPlaying = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'computer'
        else:
            move, _ = minimax_select_move(theBoard)
            theBoard[move//3][move%3] = computerLetter

            if is_winner(theBoard, computerLetter):
                draw_board(theBoard)
                print('You lose the game')
                gameIsPlaying = False
            else:
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player'
                    
