# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:45:28 2023

@author: Administrator
"""

import os,re,warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from glob import glob
from sklearn.metrics import roc_auc_score
from joblib import Parallel,delayed

from matplotlib import pyplot as plt
import seaborn as sns

def str2int(x):
    if type(x) is str:
        return float(re.findall(r'\d+',x)[0])

if __name__ == "__main__":
    np.random.seed(12345) # non-parametric会用到重抽样，这有随机性，要控制
    n_permutation = int(1e4) # 为non-parametric t test用
    
    working_data = glob('*.csv')

    df = []
    for f in working_data:
        temp = pd.read_csv(f)
        temp_data = temp.iloc[:-13]
        temp_info = temp.iloc[-13:,:2]
        for _,row in temp_info.iterrows():
            temp_data[row['category']] = row['image_name']
        df.append(temp_data)
    df = pd.concat(df)
    for col in ['mask_frames_raw',
                'visible.keys_raw',
                'response.keys_raw']:
        df[col] = df[col].apply(str2int)
    
    df_plot = dict(visible = [],
                   behavioral = [],
                   chance = [],
                   )
    df_res = dict(visible = [],
                  behavioral = [],
                  pval = [],
                  N = [],
                  frames = [],
                  )
    for visible,df_sub in df.groupby('visible.keys_raw'):
        df_sub = df_sub.dropna(subset = ['response.keys_raw'])
        if visible != np.nan:
            correct_answer = df_sub['correctAns_raw'].values - 1
            response = df_sub['response.keys_raw'].values - 1
            
            idxs = np.random.choice(correct_answer.shape[0],
                                   size = (n_permutation,correct_answer.shape[0]),
                                   replace = True,
                                   )
            y_true = np.random.choice(correct_answer,
                                      size = (10000,correct_answer.shape[0]),
                                      replace = True)
            y_pred = np.random.choice(response,
                                      size = (10000,correct_answer.shape[0]),
                                      replace = True)
            # 重抽样得到的行为正确率分布
            experiment = np.array(Parallel(n_jobs = -1,verbose = 1)(delayed(roc_auc_score)(*[
                                    correct_answer[idx],
                                    response[idx]
                                    ]) for idx in idxs))
            # 重抽样得到的随机行为正确率分布
            null = np.array(Parallel(n_jobs = -1,verbose = 1)(delayed(roc_auc_score)(*[
                                    a,b
                                    ])for a,b in zip(y_true,y_pred)))
            # p值为null比真实正确率高的概率
            pval = (np.sum(null > experiment.mean()) + 1) / (n_permutation + 1)
            # save
            [df_plot['behavioral'].append(item) for item in experiment]
            [df_plot['chance'].append(item) for item in null]
            [df_plot['visible'].append(visible) for _ in experiment]
            
            df_res['visible'].append(visible)
            df_res['behavioral'].append(experiment.mean())
            df_res['pval'].append(pval)
            df_res['N'].append(df_sub.shape[0])
            df_res['frames'].append(df_sub['mask_frames_raw'].values.mean())
    df_plot = pd.DataFrame(df_plot)
    df_res = pd.DataFrame(df_res)
            
    # plot
    df_plot = pd.melt(df_plot,id_vars = ['visible',],
                      value_vars = ['behavioral','chance'],)
    df_plot['visible'] = df_plot['visible'].map({1:'unconscious',
                                                 2: 'glimpse',
                                                 3:'conscious',
                                                     })
    
    g = sns.catplot(x = 'visible',
                    y = 'value',
                    hue = 'variable',
                    hue_order = ['behavioral','chance',],
                    data = df_plot,
                    kind = 'violin',
                    **{"cut":0,
                       "split":True,
                       "inner":'quartile',
                       }
                    )
    [ax.axhline(0.5,linestyle = '--',color = 'black',alpha = .7) for ax in g.axes.flatten()]
    g.set(xlabel = 'awareness',
          ylabel = 'ROC AUC')
    g.savefig('results.jpg',
              dpi = 300,
              bbox_inches = 'tight',
              )
    df_res.to_csv('results.csv',index = False)