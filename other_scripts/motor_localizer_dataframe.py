#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 5 10:52:57 2023

@author: nmei
"""

import numpy as np
import pandas as pd
from sklearn.utils import shuffle
np.random.seed(12345)
n_trials = 60
color = 'red'

prepare_duration = np.random.uniform(1.0,1.5,size = n_trials)
target_duration = np.random.uniform(1.5,2.0,size = n_trials)
blank_duration = np.random.uniform(1.,1.5,size = n_trials)
target_location = shuffle(np.concatenate([[0]*int(n_trials/3),[1]*int(n_trials/3),[2]*int(n_trials/3)]))
color_matrix = np.array([['white','white','white'] * n_trials ]).reshape(-1,3)
for idx_row,idx_loc in enumerate(target_location):
    color_matrix[idx_row,idx_loc] = 'red'

df = dict(
    prepare_duration = prepare_duration,
    target_duration = target_duration,
    blank_duration = blank_duration,
    left_color = color_matrix[:,0],
    middle_color = color_matrix[:,1],
    right_color = color_matrix[:,2],
    corrAns = target_location + 1,
)
df = pd.DataFrame(df)
df.to_csv('../dataframes/motor_localizer.csv',index = False)