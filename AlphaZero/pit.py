import Arena
from MCTS import MCTS
# from othello.OthelloGame import OthelloGame
# from othello.OthelloPlayers import *
# from othello.pytorch.NNet import NNetWrapper as NNet


import os
import logging

import coloredlogs
from tictactoe.TicTacToeGame import TicTacToeGame
from tictactoe.TicTacToePlayers import *
from tictactoe.pytorch.NNet import NNetWrapper as NNet
from tictactoe.TicTacToeLogic import Board
from utils import *
import wandb
import torch.cuda


import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

args = dotdict({
    'numIters': 15,
    'numEps': 30,              # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 15,        #
    'updateThreshold': 0.6,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 25,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 60,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,
    'architecture':'mlpnet',
    'lr': 0.005,
    'dropout': 0.3,
    'epochs': 10,
    'batch_size': 64,
    'cuda': torch.cuda.is_available(),
    'num_channels': 512,

})

mini_othello = False  # Play in 6x6 instead of the normal 8x8.
human_vs_cpu = True

# if mini_othello:
#     g = OthelloGame(6)
# else:
#     g = OthelloGame(8)

g = TicTacToeGame()

# all players
rp = RandomPlayer(g).play
hp = HumanTicTacToePlayer(g).play



# nnet players
n1 = NNet(g, args=args, architecture='lenet')
n1.load_checkpoint('./temp/','best.pth.tar')
args1 = dotdict({'numMCTSSims': 25, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

if human_vs_cpu:
    player2 = rp
else:
    n2 = NNet(g)
    n2.load_checkpoint('./pretrained_models/othello/pytorch/', '8x8_100checkpoints_best.pth.tar')
    args2 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
    mcts2 = MCTS(g, n2, args2)
    n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

    player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

arena = Arena.Arena(n1p, player2, g, display=TicTacToeGame.display)

print(arena.playGames(2, verbose=True))
