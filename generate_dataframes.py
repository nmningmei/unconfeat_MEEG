#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:52:57 2023

@author: nmei
"""
import os,re
import numpy as np
import pandas as pd
from glob import glob

if __name__ == "__main__":
    all_images = glob(os.path.join('processed','*','*png'))

    dict_name = dict(face = 'Living_Things',
                    house = 'Nonliving_Things')
    
    df_images = dict(category = [],
                    image_name = [],
                    image_number = [],
                    image_iter = [],
                    )
    for image in all_images:
        temp = image.replace('\\','/').split('/')
        df_images['category'].append(dict_name[temp[1]])
        df_images['image_name'].append(image)
        numbers = re.findall(r'\d+',temp[-1])
        df_images['image_number'].append(int(numbers[0]))
        df_images['image_iter'].append(int(numbers[1]))
    df_images = pd.DataFrame(df_images)
    
    for idx,df_sub in df_images.groupby('image_iter'):
        df_sub = df_sub.sample(frac = 1,replace = False,random_state = 12345)
        df_sub1 = df_sub.iloc[:100] # 前100个trial
        df_sub2 = df_sub.iloc[100:] # 后100个trial
        df_sub1.to_csv(f'dataframes/face-house-{idx}1.csv',index = False)
        df_sub2.to_csv(f'dataframes/face-house-{idx}2.csv',index = False)

    all_images = glob(os.path.join('materials','*','*'))
    df = pd.DataFrame(dict(image_name = all_images))
    df['category'] = df['image_name'].apply(lambda x:x.split('/')[1])
    df['category'] = df['category'].map(dict(face = 'Living_Things',
                                            house = 'Nonliving_Things'))
    df = df.sample(frac = 1,replace = False,random_state = 12345)
    df.to_csv(f'dataframes/locolizer.csv',index = False)