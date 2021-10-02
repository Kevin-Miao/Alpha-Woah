import random

def is_winner(board, letter):
        # Given a board and a player's letter, this function returns True if that player has won.
        return ((board[0][0]==letter and board[0][1]==letter and board[0][2]==letter) or
                (board[1][0]==letter and board[1][1]==letter and board[1][2]==letter) or
                (board[2][0]==letter and board[2][1]==letter and board[2][2]==letter) or
                (board[0][0]==letter and board[1][0]==letter and board[2][0]==letter) or
                (board[0][1]==letter and board[1][1]==letter and board[2][1]==letter) or
                (board[0][2]==letter and board[1][2]==letter and board[2][2]==letter) or
                (board[0][0]==letter and board[1][1]==letter and board[2][2]==letter) or
                (board[0][2]==letter and board[1][1]==letter and board[2][0]==letter))


def is_space_free(board, move):
        return board[move//3][move%3] == 0

def minimax(board, depth, isMax, alpha, beta):
        computerLetter, playerLetter = 1, -1

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
                                board[i//3][i%3] = computerLetter
                                best = max(best, minimax(board, depth+1, not isMax, alpha, beta) - depth)
                                alpha = max(alpha, best)
                                board[i//3][i%3] = 0

                                if alpha >= beta:
                                        break

                return best
        else:
                best = 1000

                for i in range(9):
                        if is_space_free(board, i):
                                board[i//3][i%3] = playerLetter
                                best = min(best, minimax(board, depth+1, not isMax, alpha, beta) + depth)
                                beta = min(beta, best)
                                board[i//3][i%3] = 0

                                if alpha >= beta:
                                        break

                return best


def minimax_select_move(board):
        computerLetter, playerLetter = 1, -1
        
        bestVal = -1000
        bestMove = -1

        for i in range(9):
                if is_space_free(board, i):
                        board[i//3][i%3] = computerLetter

                        moveVal = minimax(board, 0, False, -1000, 1000)

                        board[i//3][i%3] = 0

                        if moveVal > bestVal:
                                bestMove = i
                                bestVal = moveVal

        moveProbs = [0 for _ in range(9)]
        moveProbs[bestMove] = 1
        return bestMove, moveProbs


def is_board_full(board):
         return 0 not in board[0] and 0 not in board[1] and 0 not in board[2]

