#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mne

filename = '' #把“...-raw.fif”的文件名复制到这
raw = mne.io.read_raw_fif(raw,preload = True)
events = mne.find_events(raw,)
event_id = {'face':1,'house':2}
epochs = mne.Epochs(raw,events = events,event_id = event_id,tmin = -0.1,tmax = 0.5,detred = 1,preload = True)
evoked = epochs.average()
evoked.plot_joint()