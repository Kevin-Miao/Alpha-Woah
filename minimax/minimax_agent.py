import random

def is_winner(board, letter):
        # Given a board and a player's letter, this function returns True if that player has won.
        return ((board[0]==letter and board[1]==letter and board[2]==letter) or
                (board[3]==letter and board[4]==letter and board[5]==letter) or
                (board[6]==letter and board[7]==letter and board[8]==letter) or
                (board[0]==letter and board[3]==letter and board[6]==letter) or
                (board[1]==letter and board[4]==letter and board[7]==letter) or
                (board[2]==letter and board[5]==letter and board[8]==letter) or
                (board[0]==letter and board[4]==letter and board[8]==letter) or
                (board[2]==letter and board[4]==letter and board[6]==letter))


def is_space_free(board, move):
        return board[move] == 0

def minimax(board, depth, isMax, alpha, beta):
        computerLetter, playerLetter = 1, -1
        print(board)

        if is_winner(board, computerLetter):
                return 10
        if is_winner(board, playerLetter):
                return -10
        if is_board_full(board):
                return 0

        if isMax:
                best = -1000

                for i in range(9):
                        if is_space_free(board, i):
                                board[i] = computerLetter
                                best = max(best, minimax(board, depth+1, not isMax, alpha, beta) - depth)
                                alpha = max(alpha, best)
                                board[i] = 0

                                if alpha >= beta:
                                        break

                return best
        else:
                best = 1000

                for i in range(9):
                        if is_space_free(board, i):
                                board[i] = playerLetter
                                best = min(best, minimax(board, depth+1, not isMax, alpha, beta) + depth)
                                beta = min(beta, best)
                                board[i] = 0

                                if alpha >= beta:
                                        break

                return best


def minimax_select_move(board):
        computerLetter, playerLetter = 1, -1
        
        bestVal = -1000
        bestMove = -1

        for i in range(9):
                if is_space_free(board, i):
                        board[i] = computerLetter

                        moveVal = minimax(board, 0, False, -1000, 1000)

                        board[i] = 0

                        if moveVal > bestVal:
                                bestMove = i
                                bestVal = moveVal

        return bestMove


def is_board_full(board):
         return 0 not in board

