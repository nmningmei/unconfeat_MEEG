#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on 十月 31, 2023, at 16:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
import serial
port = serial.Serial('COM1')

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'post-mask-only-trigger'  # from the Builder filename that created this script
expInfo = {
    'n_square': '64',
    'probeFrames': '1',
    'participant': '1',
    'image_size': '300',
    'postmask_dur': '20',
    'session': '1',
    'block': '1',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Administrator\\Documents\\python_works\\unconfeat_MEEG\\post-mask-only-trigger.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color='black', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'black'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "setupTRIGetc" ---
    # Run 'Begin Experiment' code from setup_vbles_trigger
    curr=int(expInfo['probeFrames'])
    count=0
    
    #n_total = 32
    #premask_dur = float(expInfo['premask_dur'])
    postmask_dur = float(expInfo['postmask_dur'])
    session = int(expInfo['session'])
    block = int(expInfo['block'])
    n_square = int(expInfo['n_square'])
    image_size = int(expInfo['image_size'])
    
    dict_answer = {'Living_Things':1,
                   'Nonliving_Things':2,}
    
    dict_response = {'1':3,'2':4}
    
    dict_visible = {'1':5,'2':6,'3':7}
    
    import time
    #from psychopy import parallel 
    #parallel.setPortAddress(888)
    #wait_msg = "Waiting for Scanner..."
    #msg = visual.TextStim(win, color = 'DarkGray', text = wait_msg)
    
    
    
    # --- Initialize components for Routine "introduction" ---
    description_of_experiment = visual.TextStim(win=win, name='description_of_experiment',
        text='您的任务是识别接下来的图片里是人脸还是房子。\n\n请根据V（人脸）和nV（房子）的相对位置来按键。\n\n对应左边的按“1”，对应右边的按“2”。\n\n实验即将开始。',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    global_fixation = visual.TextStim(win=win, name='global_fixation',
        text='+',
        font='Arial',
        pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "probe_routine" ---
    blank = visual.TextStim(win=win, name='blank',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    probe = visual.ImageStim(
        win=win,
        name='probe', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(image_size, image_size),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "postmask" ---
    postmask_1 = visual.GratingStim(
        win=win, name='postmask_1',units='pix', 
        tex=np.random.rand(n_square,n_square) * 2 -1, mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(image_size, image_size), sf=None, phase=1.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=1, contrast=1.0, blendmode='avg',
        texRes=128, interpolate=False, depth=0.0)
    
    # --- Initialize components for Routine "jitter_delay" ---
    delay_post_mask = visual.TextStim(win=win, name='delay_post_mask',
        text='+',
        font='Arial',
        pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "response_routine" ---
    response = keyboard.Keyboard()
    tell_response = visual.TextStim(win=win, name='tell_response',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "visibility" ---
    visible = keyboard.Keyboard()
    tell_visible = visual.TextStim(win=win, name='tell_visible',
        text='?',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "post_trial_jitter" ---
    post_fixation = visual.TextStim(win=win, name='post_fixation',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from pick_post_fixation_duration
    
    
    
    # --- Initialize components for Routine "show_message" ---
    
    # --- Initialize components for Routine "End_experiment" ---
    The_End = visual.TextStim(win=win, name='The_End',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "setupTRIGetc" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setup_vbles_trigger
    #msg.draw()
    win.flip()
    
    #while True:
    #    if (parallel.readPin(10) == 1) or (event.getKeys() == ['q']):
    #        break
    #    else:
    #        time.sleep(0.0001) # give 1ms to other processes
    globalClock.reset()
    startTime = globalClock.getTime() 
    # keep track of which components have finished
    setupTRIGetcComponents = []
    for thisComponent in setupTRIGetcComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "setupTRIGetc" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setupTRIGetcComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "setupTRIGetc" ---
    for thisComponent in setupTRIGetcComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "setupTRIGetc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "introduction" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    introductionComponents = [description_of_experiment, global_fixation]
    for thisComponent in introductionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "introduction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *description_of_experiment* updates
        
        # if description_of_experiment is starting this frame...
        if description_of_experiment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            description_of_experiment.frameNStart = frameN  # exact frame index
            description_of_experiment.tStart = t  # local t and not account for scr refresh
            description_of_experiment.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(description_of_experiment, 'tStartRefresh')  # time at next scr refresh
            # update status
            description_of_experiment.status = STARTED
            description_of_experiment.setAutoDraw(True)
        
        # if description_of_experiment is active this frame...
        if description_of_experiment.status == STARTED:
            # update params
            pass
        
        # if description_of_experiment is stopping this frame...
        if description_of_experiment.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > description_of_experiment.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                description_of_experiment.tStop = t  # not accounting for scr refresh
                description_of_experiment.frameNStop = frameN  # exact frame index
                # update status
                description_of_experiment.status = FINISHED
                description_of_experiment.setAutoDraw(False)
        
        # *global_fixation* updates
        
        # if global_fixation is starting this frame...
        if global_fixation.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            global_fixation.frameNStart = frameN  # exact frame index
            global_fixation.tStart = t  # local t and not account for scr refresh
            global_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(global_fixation, 'tStartRefresh')  # time at next scr refresh
            # update status
            global_fixation.status = STARTED
            global_fixation.setAutoDraw(True)
        
        # if global_fixation is active this frame...
        if global_fixation.status == STARTED:
            # update params
            pass
        
        # if global_fixation is stopping this frame...
        if global_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > global_fixation.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                global_fixation.tStop = t  # not accounting for scr refresh
                global_fixation.frameNStop = frameN  # exact frame index
                # update status
                global_fixation.status = FINISHED
                global_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "introduction" ---
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(f"dataframes/face-house-{session}{block}.csv"),
        seed=12345, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "probe_routine" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('probe_routine.started', globalClock.getTime())
        # Run 'Begin Routine' code from code
        trials.addData("image_onset_time", globalClock.getTime() - startTime)
        trigger_code = dict_answer[category]
        probe.setImage(image_name)
        # keep track of which components have finished
        probe_routineComponents = [blank, probe]
        for thisComponent in probe_routineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "probe_routine" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank* updates
            
            # if blank is starting this frame...
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.started')
                # update status
                blank.status = STARTED
                blank.setAutoDraw(True)
            
            # if blank is active this frame...
            if blank.status == STARTED:
                # update params
                pass
            
            # if blank is stopping this frame...
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + np.random.choice([0.5,1],size = 1)[0]-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank.stopped')
                    # update status
                    blank.status = FINISHED
                    blank.setAutoDraw(False)
            
            # *probe* updates
            
            # if probe is starting this frame...
            if probe.status == NOT_STARTED and blank.status == FINISHED:
                win.callOnFlip(port.write, str.encode(chr(trigger_code)))
                # keep track of start time/frame for later
                probe.frameNStart = frameN  # exact frame index
                probe.tStart = t  # local t and not account for scr refresh
                probe.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe.started')
                thisExp.timestampOnFlip(win, 'trigger.started')
                # update status
                probe.status = STARTED
                probe.setAutoDraw(True)
            
            # if probe is active this frame...
            if probe.status == STARTED:
                # update params
                pass
            
            # if probe is stopping this frame...
            if probe.status == STARTED:
                if frameN >= (probe.frameNStart + curr):
                    win.callOnFlip(port.write,str.encode('0'))
                    # keep track of stop time/frame for later
                    probe.tStop = t  # not accounting for scr refresh
                    probe.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'probe.stopped')
                    thisExp.timestampOnFlip(win, 'trigger.stopped')
                    # update status
                    probe.status = FINISHED
                    probe.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in probe_routineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "probe_routine" ---
        for thisComponent in probe_routineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('probe_routine.stopped', globalClock.getTime())
        # the Routine "probe_routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "postmask" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('postmask.started', globalClock.getTime())
        postmask_1.setPhase(np.random.uniform(0,1,2).round(1))
        # keep track of which components have finished
        postmaskComponents = [postmask_1]
        for thisComponent in postmaskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "postmask" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *postmask_1* updates
            
            # if postmask_1 is starting this frame...
            if postmask_1.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                postmask_1.frameNStart = frameN  # exact frame index
                postmask_1.tStart = t  # local t and not account for scr refresh
                postmask_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(postmask_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'postmask_1.started')
                # update status
                postmask_1.status = STARTED
                postmask_1.setAutoDraw(True)
            
            # if postmask_1 is active this frame...
            if postmask_1.status == STARTED:
                # update params
                postmask_1.setTex(np.random.rand(n_square,n_square) * 2 -1, log=False)
            
            # if postmask_1 is stopping this frame...
            if postmask_1.status == STARTED:
                if frameN >= (postmask_1.frameNStart + postmask_dur):
                    # keep track of stop time/frame for later
                    postmask_1.tStop = t  # not accounting for scr refresh
                    postmask_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'postmask_1.stopped')
                    # update status
                    postmask_1.status = FINISHED
                    postmask_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in postmaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "postmask" ---
        for thisComponent in postmaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('postmask.stopped', globalClock.getTime())
        # the Routine "postmask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "jitter_delay" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('jitter_delay.started', globalClock.getTime())
        # Run 'Begin Routine' code from pick_jitter_delay_duration
        
        
        jitter_delay_dur=np.random.choice([1,1.5,2,2.5,3],size = 1,)[0]#first is jit1_count 0
        
        trials.addData("jitter1", jitter_delay_dur)
        # keep track of which components have finished
        jitter_delayComponents = [delay_post_mask]
        for thisComponent in jitter_delayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "jitter_delay" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delay_post_mask* updates
            
            # if delay_post_mask is starting this frame...
            if delay_post_mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delay_post_mask.frameNStart = frameN  # exact frame index
                delay_post_mask.tStart = t  # local t and not account for scr refresh
                delay_post_mask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delay_post_mask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'delay_post_mask.started')
                # update status
                delay_post_mask.status = STARTED
                delay_post_mask.setAutoDraw(True)
            
            # if delay_post_mask is active this frame...
            if delay_post_mask.status == STARTED:
                # update params
                pass
            
            # if delay_post_mask is stopping this frame...
            if delay_post_mask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delay_post_mask.tStartRefresh + jitter_delay_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    delay_post_mask.tStop = t  # not accounting for scr refresh
                    delay_post_mask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'delay_post_mask.stopped')
                    # update status
                    delay_post_mask.status = FINISHED
                    delay_post_mask.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in jitter_delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "jitter_delay" ---
        for thisComponent in jitter_delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('jitter_delay.stopped', globalClock.getTime())
        # the Routine "jitter_delay" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "response_routine" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response_routine.started', globalClock.getTime())
        # Run 'Begin Routine' code from reponse_trigger_code
        trials.addData("discrim_resptime", globalClock.getTime() - startTime)
        
        resp_options = [['nV_V',['Nonliving_Things','Living_Things']],
                        ['V_nV',['Living_Things','Nonliving_Things']]]
        
        idx = np.random.choice([0,1])
        msg = '{}'.format(resp_options[idx][0])
        
        trials.addData("response_window", resp_options[idx][0])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        tell_response.setText(msg
        
        )
        # keep track of which components have finished
        response_routineComponents = [response, tell_response]
        for thisComponent in response_routineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "response_routine" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response* updates
            waitOnFlip = False
            
            # if response is starting this frame...
            if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response.started')
                # update status
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if response is stopping this frame...
            if response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    response.tStop = t  # not accounting for scr refresh
                    response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response.stopped')
                    # update status
                    response.status = FINISHED
                    response.status = FINISHED
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['1','2'], ignoreKeys=["escape"], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    response.duration = _response_allKeys[-1].duration
            
            # *tell_response* updates
            
            # if tell_response is starting this frame...
            if tell_response.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                tell_response.frameNStart = frameN  # exact frame index
                tell_response.tStart = t  # local t and not account for scr refresh
                tell_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tell_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tell_response.started')
                # update status
                tell_response.status = STARTED
                tell_response.setAutoDraw(True)
            
            # if tell_response is active this frame...
            if tell_response.status == STARTED:
                # update params
                pass
            
            # if tell_response is stopping this frame...
            if tell_response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tell_response.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tell_response.tStop = t  # not accounting for scr refresh
                    tell_response.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tell_response.stopped')
                    # update status
                    tell_response.status = FINISHED
                    tell_response.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_routineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response_routine" ---
        for thisComponent in response_routineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response_routine.stopped', globalClock.getTime())
        # Run 'End Routine' code from reponse_trigger_code
        temp_correctAns = np.where(np.array(resp_options[idx][1]) == category)[0][0]+1
        
        trials.addData('correctAns',temp_correctAns)
        
        # objective accuracy
        
        if (response.keys == str(temp_correctAns)) or (response.keys == temp_correctAns):
           temp_corr = 1
        else:
            temp_corr = 0
        
        trials.addData('response.corr' , temp_corr)
        
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
        trials.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials.addData('response.rt', response.rt)
            trials.addData('response.duration', response.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "visibility" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('visibility.started', globalClock.getTime())
        visible.keys = []
        visible.rt = []
        _visible_allKeys = []
        # Run 'Begin Routine' code from trigger_visibility
        trials.addData("visible_resptime", globalClock.getTime() - startTime)
        
        # keep track of which components have finished
        visibilityComponents = [visible, tell_visible]
        for thisComponent in visibilityComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "visibility" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *visible* updates
            waitOnFlip = False
            
            # if visible is starting this frame...
            if visible.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                visible.frameNStart = frameN  # exact frame index
                visible.tStart = t  # local t and not account for scr refresh
                visible.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(visible, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'visible.started')
                # update status
                visible.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(visible.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(visible.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if visible is stopping this frame...
            if visible.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > visible.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    visible.tStop = t  # not accounting for scr refresh
                    visible.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'visible.stopped')
                    # update status
                    visible.status = FINISHED
                    visible.status = FINISHED
            if visible.status == STARTED and not waitOnFlip:
                theseKeys = visible.getKeys(keyList=['1','2','3'], ignoreKeys=["escape"], waitRelease=False)
                _visible_allKeys.extend(theseKeys)
                if len(_visible_allKeys):
                    visible.keys = _visible_allKeys[-1].name  # just the last key pressed
                    visible.rt = _visible_allKeys[-1].rt
                    visible.duration = _visible_allKeys[-1].duration
                    # was this correct?
                    if (visible.keys == str('1')) or (visible.keys == '1'):
                        visible.corr = 1
                    else:
                        visible.corr = 0
            
            # *tell_visible* updates
            
            # if tell_visible is starting this frame...
            if tell_visible.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tell_visible.frameNStart = frameN  # exact frame index
                tell_visible.tStart = t  # local t and not account for scr refresh
                tell_visible.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tell_visible, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tell_visible.started')
                # update status
                tell_visible.status = STARTED
                tell_visible.setAutoDraw(True)
            
            # if tell_visible is active this frame...
            if tell_visible.status == STARTED:
                # update params
                pass
            
            # if tell_visible is stopping this frame...
            if tell_visible.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tell_visible.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tell_visible.tStop = t  # not accounting for scr refresh
                    tell_visible.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tell_visible.stopped')
                    # update status
                    tell_visible.status = FINISHED
                    tell_visible.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in visibilityComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "visibility" ---
        for thisComponent in visibilityComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('visibility.stopped', globalClock.getTime())
        # check responses
        if visible.keys in ['', [], None]:  # No response was made
            visible.keys = None
            # was no response the correct answer?!
            if str('1').lower() == 'none':
               visible.corr = 1;  # correct non-response
            else:
               visible.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('visible.keys',visible.keys)
        trials.addData('visible.corr', visible.corr)
        if visible.keys != None:  # we had a response
            trials.addData('visible.rt', visible.rt)
            trials.addData('visible.duration', visible.duration)
        # Run 'End Routine' code from staircase
        count += 1
        trials.addData('probe_Frames',curr)
            
        count += 1
        if (visible.keys == str('1')) or (visible.keys == '1'):# invisible
                curr += np.random.choice([1,2,],size=1,p=[0.5,0.5])[0]
                if curr < 1:  curr = 1
        elif (visible.keys == str('2')) or (visible.keys == '2'):# partially aware
                curr -= 1
                if curr < 1:  curr = 1 
        elif (visible.keys == str('3')) or (visible.keys == '3'): # visible
                curr -= np.random.choice([2,3],size=1,p=[0.5,0.5])[0]
                if curr < 1: curr = 1
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "post_trial_jitter" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('post_trial_jitter.started', globalClock.getTime())
        # Run 'Begin Routine' code from pick_post_fixation_duration
        
        jitter2_delay_dur=np.random.choice([1,1.5,2,2.5],size = 1)[0]#first is jit1_count 0
        
        trials.addData("jitter2", jitter2_delay_dur)
        
        # keep track of which components have finished
        post_trial_jitterComponents = [post_fixation]
        for thisComponent in post_trial_jitterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "post_trial_jitter" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *post_fixation* updates
            
            # if post_fixation is starting this frame...
            if post_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                post_fixation.frameNStart = frameN  # exact frame index
                post_fixation.tStart = t  # local t and not account for scr refresh
                post_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(post_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'post_fixation.started')
                # update status
                post_fixation.status = STARTED
                post_fixation.setAutoDraw(True)
            
            # if post_fixation is active this frame...
            if post_fixation.status == STARTED:
                # update params
                pass
            
            # if post_fixation is stopping this frame...
            if post_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > post_fixation.tStartRefresh + jitter2_delay_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    post_fixation.tStop = t  # not accounting for scr refresh
                    post_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'post_fixation.stopped')
                    # update status
                    post_fixation.status = FINISHED
                    post_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in post_trial_jitterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "post_trial_jitter" ---
        for thisComponent in post_trial_jitterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('post_trial_jitter.stopped', globalClock.getTime())
        # the Routine "post_trial_jitter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "show_message" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('show_message.started', globalClock.getTime())
        # Run 'Begin Routine' code from print_
        
        meanacc = trials.data['response.corr'].mean()
        meanvis = trials.data['visible.corr'].mean()
        #msg="{} / {}\n\nmean correct {:.2f} \npresenting frames = {}\nmean unconscious response = {:.3f}" .format(
        #count,n_total,meanacc,curr,meanvis)
        
        #msg = msg + '\nkey={},cor={}'.format(response.keys,str(temp_correctAns))
        #msg WOULD BE TO DISPLAY IN A TXT OBJECT - THAT HAS BEEN DELETED
        # keep track of which components have finished
        show_messageComponents = []
        for thisComponent in show_messageComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "show_message" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in show_messageComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "show_message" ---
        for thisComponent in show_messageComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('show_message.stopped', globalClock.getTime())
        # Run 'End Routine' code from print_
        print("{}/{},mean unconscious = {:.2f}, frame = {}, p(correct) = {:.2f}".format(
            trials.thisN,trials.nTotal,
            meanvis,curr,meanacc))
        # the Routine "show_message" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsText(filename + 'trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "End_experiment" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    End_experimentComponents = [The_End]
    for thisComponent in End_experimentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "End_experiment" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *The_End* updates
        
        # if The_End is starting this frame...
        if The_End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            The_End.frameNStart = frameN  # exact frame index
            The_End.tStart = t  # local t and not account for scr refresh
            The_End.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(The_End, 'tStartRefresh')  # time at next scr refresh
            # update status
            The_End.status = STARTED
            The_End.setAutoDraw(True)
        
        # if The_End is active this frame...
        if The_End.status == STARTED:
            # update params
            pass
        
        # if The_End is stopping this frame...
        if The_End.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > The_End.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                The_End.tStop = t  # not accounting for scr refresh
                The_End.frameNStop = frameN  # exact frame index
                # update status
                The_End.status = FINISHED
                The_End.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_experimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_experiment" ---
    for thisComponent in End_experimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    # Run 'End Experiment' code from code_2
    print(globalClock.getTime() - startTime)
    #print("mean unconscious = {:.2f}, frame = {}, p(correct) = {:.2f}".format(
    #    meanvis,curr,meanacc))
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
