import sys
sys.path.append('..')
from .utils import *

import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
import torchvision.models

class ResNet(nn.Module):
    def __init__(self, game, args):
        # game params
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()
        self.args = args
        self.name = 'ResNet'

        super().__init__()
        network = torchvision.models.resnet18(pretrained=False, progress=True)
        network.conv1 = nn.Conv2d(1, 64, kernel_size=(3,3), padding=(1,1), bias=False)
        network.fc = nn.Identity()
        self.network = network
        self.fc1 = nn.Linear(512, self.action_size)
        self.fc2 = nn.Linear(512, 1)

    def forward(self, s):
        s = s.view(-1, 1, self.board_x, self.board_y)  
        pi = self.fc1(self.network(s))
        v =  self.fc2(self.network(s))                                                            # batch_size x 1

        return F.log_softmax(pi, dim=1), torch.tanh(v)
