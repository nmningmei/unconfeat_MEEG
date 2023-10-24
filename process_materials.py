# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:59:29 2023

@author: Administrator
"""

import os
import numpy as np
from glob import glob
from tqdm import tqdm
from shutil import rmtree
from PIL import Image,ImageFilter
from joblib import Parallel,delayed

def scramble(image):
    # convert to numpy array
    image_array = np.asarray(image)
    ImSize = image_array.shape
    # the same random phase for all layers
    RandomPhase = np.angle(np.fft.fft2(np.random.normal(size=(ImSize[0],ImSize[1]))))
    # preallocation
    ImFourier = np.zeros((ImSize[0],ImSize[1],ImSize[2]),dtype=np.complex128)
    Amp = np.zeros((ImSize[0],ImSize[1],ImSize[2]))
    Phase = np.zeros((ImSize[0],ImSize[1],ImSize[2]))
    ImScrambled = np.zeros((ImSize[0],ImSize[1],ImSize[2]),dtype=np.complex128)
    
    # for each color channel/layer
    for layer in range(image_array.shape[-1]):
        # get the fourier space of the layer
        ImFourier[:,:,layer] = np.fft.fft2(image_array[:,:,layer])
        # get the magnitude
        Amp[:,:,layer] = np.abs(ImFourier[:,:,layer])
        # get the phase
        Phase[:,:,layer] = np.angle(ImFourier[:,:,layer])
        # add gaussian noise to the phase
        Phase[:,:,layer] = Phase[:,:,layer] + RandomPhase
        # covert fourier space back to image space
        ImScrambled[:,:,layer] = np.fft.ifft2(Amp[:,:,layer] * np.exp(1j*(Phase[:,:,layer])))
    # take only the real part
    ImScrambled = np.real(ImScrambled)
    return ImScrambled.astype('uint8') # make sure to be in RGB format

def proc(image,idx,reference_im):
    scramble_im = Image.fromarray(scramble(reference_im.resize((512,512))))
    im = Image.open(image).convert("L").convert("RGB").resize((512,512))
    if np.random.randn() > 0:
        im = im.transpose(method = Image.Transpose.FLIP_LEFT_RIGHT)
    im = im.rotate(np.random.randint(-45,45,size = 1),fillcolor = (0,0,0),)
    imarray = np.asarray(im).copy()
    imarray[np.where(imarray > 245)]  = 0
    im = Image.fromarray(imarray)
    im = im.filter(ImageFilter.GaussianBlur(4))
    scramble_im = scramble_im.filter(ImageFilter.GaussianBlur(4))
    blended = Image.blend(im,scramble_im,alpha = .5)
    
    temp = image.replace('\\','/').split('/')
    
    blended.save(os.path.join(new_folder,temp[1],temp[2].split('.')[0] + f'_{idx}.png'))
    return im,blended

if __name__ == "__main__":
    np.random.seed(12345)
    images = glob('materials/*/*')
    
    new_folder = 'processed'
    if os.path.exists(new_folder):
        rmtree(new_folder)
    os.mkdir(new_folder)
    
    os.mkdir(os.path.join(new_folder,'face'))
    os.mkdir(os.path.join(new_folder,'house'))
    
    reference_im = Image.open(np.random.choice(images,size = 1)[0]).convert("L").convert("RGB")
    
    
    for image in images:
        _ = Parallel(n_jobs = -1,verbose = 1)(delayed(proc)(**{'image':image,'idx':idx,
                                                               'reference_im':reference_im}) for idx in range(26))
