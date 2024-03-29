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
    np.random.seed(12345)
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
        n_trials = df_sub.shape[0]
        # fixation duration
        fixation = np.random.uniform(0.25,0.5,size = n_trials)
        fixation_blank = np.random.uniform(0.5,1,size = n_trials)
        
        # delay before responses -- where decoding focus
        delay = np.random.uniform(1,2,size = n_trials)
        
        # response choices
        resp_choices = np.random.choice(['V_nV','nV_V'],size = n_trials,)
        
        # delaye inbetween responses
        delay_in_between = np.random.uniform(0.5,1,size = n_trials)
        
        df_sub['fixation_duration'] = fixation
        df_sub['fixation_blank_duration'] = fixation_blank
        df_sub['delay_duration'] = delay
        df_sub['resp_choices'] = resp_choices
        df_sub['delay_in_between'] = delay_in_between
        df_sub['visb_choices'] = ['?'] * n_trials
        
        df_sub['convert'] = df_sub['resp_choices'].map({
                                            'V_nV':'Living_Things-Nonliving_Things',
                                            'nV_V':'Nonliving_Things-Living_Things'})
        corrAns = []
        key_options = ['1','2']
        for ii,row in df_sub.iterrows():
            key, = np.where(np.array(row['convert'].split('-')) == row['category'])
            corrAns.append(key_options[key[0]])
        df_sub['corrAns'] = corrAns
        
        df_sub = df_sub.sample(frac = 1,replace = False,random_state = 12345)
        df_f = df_sub[df_sub['category'] == "Living_Things"]
        df_h = df_sub[df_sub['category'] == 'Nonliving_Things']
        
        df_f1 = df_f.iloc[:50]
        df_f2 = df_f.iloc[50:]
        df_h1 = df_h.iloc[:50]
        df_h2 = df_h.iloc[50:]
        
        df_sub1 = pd.concat([df_f1,df_h1]).sample(frac = 1,replace = False,random_state=12345).reset_index(drop=True) # 前100个trial
        df_sub2 = pd.concat([df_f2,df_h2]).sample(frac = 1,replace = False,random_state=12345).reset_index(drop=True) # 后100个trial
        df_sub1.to_csv(f'dataframes/face-house-{idx}-1.csv',index = False)
        df_sub2.to_csv(f'dataframes/face-house-{idx}-2.csv',index = False)

    all_images = glob(os.path.join('materials','*','*'))
    df = pd.DataFrame(dict(image_name = all_images))
    df['category'] = df['image_name'].apply(lambda x:x.split('/')[1])
    df['category'] = df['category'].map(dict(face = 'Living_Things',
                                            house = 'Nonliving_Things'))
    df = df.sample(frac = 1,replace = False,random_state = 12345)
    df.to_csv(f'dataframes/localizer.csv',index = False)