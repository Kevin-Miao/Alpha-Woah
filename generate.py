import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import wandb
from tqdm import tqdm
import subprocess

runs = {
    'cs294-190-hw1/hw1/kap4ytaf':500,
    'cs294-190-hw1/hw1/az93cnr1':100,
    'cs294-190-hw1/hw1/egrhegxj':25,
    'cs294-190-hw1/hw1/vjqagow1':10,
    'cs294-190-hw1/hw1/rhq1iysc':3}

agent1 = {k:np.array([]) for k in [500, 100, 25, 10, 3]}
agent2 = {k:np.array([]) for k in [500, 100, 25, 10, 3]}
draws = {k:np.array([]) for k in [500, 100, 25, 10, 3]}

for mode in ['', '-r']:
    for run in tqdm(runs):
        for it in tqdm(range(1, 11)):
            path = 'LeNetLeNet_{}.pth.tar'.format(it)
            script = ['python', 'main.py', '-n', '100', '-p', path, '-a', 'lenet', '-m', str(runs[run])]
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

f1 = open('a1.pkl','wb')
pickle.dump(agent1, f1)

f2 = open('a2.pkl','wb')
pickle.dump(agent2, f2)

f3 = open('dr.pkl','wb')
pickle.dump(draws, f3)
