import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import wandb
from tqdm import tqdm
import subprocess

runs = {
    'cs294-190-hw1/hw1/ar28myh4':500,
    'cs294-190-hw1/hw1/8xc2i42u':100,
    'cs294-190-hw1/hw1/ewu24fvr':25,
    'cs294-190-hw1/hw1/cjrkrsam':10,
    'cs294-190-hw1/hw1/xzdxx6bs':3}

agent1 = {k:np.array([]) for k in [500, 100, 25, 10, 3]}
agent2 = {k:np.array([]) for k in [500, 100, 25, 10, 3]}
draws = {k:np.array([]) for k in [500, 100, 25, 10, 3]}

for mode in ['', '-r']:
    for run in tqdm(runs):
        for it in tqdm([1,2,3,4,5,6,7,8,9,10,15]):
            path = 'LeNetLeNet_{}.pth.tar'.format(it)
            script = ['python', 'main.py', '-n', '100', '-p', path, '-a', 'lenet', '-m', str(runs[run])]
            if script[-1] == '500':
                script[-1] = '200'
            api = wandb.Api()
            r = api.run(run)
            r.file(path).download(replace=True)
            if mode == '-r':
                script.append(mode)
            s=subprocess.check_output(script)
            a1, a2, dr = [x for x in s.decode('utf-8').split(' ')[-1].split('\n') if x]
            agent1[runs[run]] = np.append(agent1[runs[run]], a1)
            agent2[runs[run]] = np.append(agent2[runs[run]], a2)
            draws[runs[run]] = np.append(draws[runs[run]], dr)

import pickle

f1 = open('a1-v2.pkl','wb')
pickle.dump(agent1, f1)

f2 = open('a2-v2.pkl','wb')
pickle.dump(agent2, f2)

f3 = open('dr-v2.pkl','wb')
pickle.dump(draws, f3)
