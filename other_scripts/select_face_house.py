# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from glob import glob
from shutil import rmtree,copyfile
import numpy as np
import pandas as pd

if __name__ == "__main__":
    np.random.seed(12345)
    neutral_face = glob(os.path.join('../materials/face/neutral/*/*gif'))
    female = np.array([item for item in neutral_face if ('female' in item)])
    male = np.array([item for item in neutral_face if ('female' not in item)])
    
    # select
    female = np.random.choice(female,size = 50,replace = False)
    male = np.random.choice(male,size = 50,replace = False)
    house = np.random.choice(glob(os.path.join('../materials/house/*jpg')),100,replace = False)
    
    # create a folder
    folder_name = 'materials'
    if os.path.exists(folder_name):
        rmtree(folder_name)
    os.mkdir(folder_name)
    os.mkdir(os.path.join(folder_name,'face'))
    os.mkdir(os.path.join(folder_name,'house'))
    
    # copy and paste
    for item in female:
        temp = item.replace('\\','/').split('/')
        new_name = os.path.join(folder_name,'face',f'{temp[-2]}_{temp[-1]}')
        copyfile(item,new_name)
    for item in male:
        temp = item.replace('\\','/').split('/')
        new_name = os.path.join(folder_name,'face',f'{temp[-2]}_{temp[-1]}')
        copyfile(item,new_name)
    for item in house:
        temp = item.replace('\\','/').split('/')
        new_name = os.path.join(folder_name,'house',f'{temp[-1]}')
        copyfile(item,new_name)
    
    