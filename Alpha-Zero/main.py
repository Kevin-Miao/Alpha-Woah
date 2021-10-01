import os

os.environ['CUDA_VISIBLE_DEVICES'] = "4"  # Making sure it's only using one GPU

import logging

import coloredlogs

from Coach import Coach
from tictactoe.TicTacToeGame import TicTacToeGame
from tictactoe.pytorch.NNet import NNetWrapper as nn
from utils import *
import wandb
import torch.cuda

log = logging.getLogger(__name__)

coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.

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
    'architecture':'resnet',
    'lr': 0.005,
    'dropout': 0.3,
    'epochs': 10,
    'batch_size': 64,
    'cuda': torch.cuda.is_available(),
    'num_channels': 512,

})

wandb.init(project='cs294-190-hw1', entity='kevin-miao', config=args)


def main():
    log.info('Loading %s...', TicTacToeGame.__name__)
    g = TicTacToeGame()

    log.info('Loading %s...', nn.__name__)
    nnet = nn(g, args= wandb.config, architecture=wandb.config.architecture)

    if wandb.config.load_model:
        log.info('Loading checkpoint "%s/%s"...', wandb.config.load_folder_file)
        nnet.load_checkpoint(wandb.config.load_folder_file[0], wandb.config.load_folder_file[1])
    else:
        log.warning('Not loading a checkpoint!')

    log.info('Loading the Coach...')
    c = Coach(g, nnet, wandb.config)

    if wandb.config.load_model:
        log.info("Loading 'trainExamples' from file...")
        c.loadTrainExamples()

    log.info('Starting the learning process 🎉')
    c.learn()


if __name__ == "__main__":
    main()
