#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:52:57 2023

@author: nmei
"""
import os
import numpy as np
import pandas as pd
from glob import glob

all_images = glob(os.path.join('greyscaled','*','*','*jpg'))
unique_class = ['Living_Things','Nonliving_Things']
unique_subclass = np.unique([item.split('/')[2] for item in all_images])

df_images = dict(category = [],
                 subtarget = [],
                 item = [],
                 image_name = [],
                 count = [],
                 )
for image in all_images:
    _,target,subclass,image_name = image.split('/')
    df_images['category'].append(target)
    df_images['subtarget'].append(subclass)
    df_images['item'].append(image_name.split('_')[0])
    df_images['count'].append(image_name.split('_')[-1].split('.')[0])
    df_images['image_name'].append(image)
df_images = pd.DataFrame(df_images)



for idx,df_sub in df_images.groupby('count'):
    df_sub.to_csv(f'living-nonliving-{idx}.csv',index = False)