/****************** 
 * Localizer *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'localizer';  // from the Builder filename that created this script
let expInfo = {
    'participant': '1',
    'image_size': '300',
    'debug': false,
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(setupTRIGetcRoutineBegin());
flowScheduler.add(setupTRIGetcRoutineEachFrame());
flowScheduler.add(setupTRIGetcRoutineEnd());
flowScheduler.add(introductionRoutineBegin());
flowScheduler.add(introductionRoutineEachFrame());
flowScheduler.add(introductionRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



flowScheduler.add(End_experimentRoutineBegin());
flowScheduler.add(End_experimentRoutineEachFrame());
flowScheduler.add(End_experimentRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });
  
psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "setupTRIGetc"
  setupTRIGetcClock = new util.Clock();
  // Run 'Begin Experiment' code from setup_vbles_trigger
  import * as time from 'time';
  image_size = Number.parseInt(expInfo["image_size"]);
  debug = bool(expInfo["debug"]);
  dict_answer = {"Living_Things": 1, "Nonliving_Things": 2};
  if ((! debug)) {
      import * as pyxid2 from 'pyxid2';
      import * as time from 'time';
      devices = pyxid2.get_xid_devices();
      dev = devices[0];
      console.log(dev);
      dev.reset_base_timer();
      dev.reset_rt_timer();
      dev.set_pulse_duration(30);
  }
  
  // Initialize components for Routine "introduction"
  introductionClock = new util.Clock();
  description_of_experiment = new visual.TextStim({
    win: psychoJS.window,
    name: 'description_of_experiment',
    text: '这个实验是一个定位任务。\n\n您的任务是识别接下来的图片里是人脸还是房子。\n\n请根据V（人脸）和nV（房子）的相对位置来按键。\n\n对应左边的按“1”，对应右边的按“2”。\n\n请实验员按“空格”键继续。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  start_experiment = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "probe_routine"
  probe_routineClock = new util.Clock();
  preblank = new visual.TextStim({
    win: psychoJS.window,
    name: 'preblank',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  probe = new visual.ImageStim({
    win : psychoJS.window,
    name : 'probe', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [image_size, image_size],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  postblank = new visual.TextStim({
    win: psychoJS.window,
    name: 'postblank',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "response_routine"
  response_routineClock = new util.Clock();
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  tell_response = new visual.TextStim({
    win: psychoJS.window,
    name: 'tell_response',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "End_experiment"
  End_experimentClock = new util.Clock();
  The_End = new visual.TextStim({
    win: psychoJS.window,
    name: 'The_End',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function setupTRIGetcRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'setupTRIGetc' ---
    t = 0;
    setupTRIGetcClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from setup_vbles_trigger
    psychoJS.window.flip();
    globalClock.reset();
    startTime = globalClock.getTime();
    
    // keep track of which components have finished
    setupTRIGetcComponents = [];
    
    for (const thisComponent of setupTRIGetcComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function setupTRIGetcRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'setupTRIGetc' ---
    // get current time
    t = setupTRIGetcClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setupTRIGetcComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function setupTRIGetcRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'setupTRIGetc' ---
    for (const thisComponent of setupTRIGetcComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "setupTRIGetc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function introductionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'introduction' ---
    t = 0;
    introductionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    start_experiment.keys = undefined;
    start_experiment.rt = undefined;
    _start_experiment_allKeys = [];
    // keep track of which components have finished
    introductionComponents = [];
    introductionComponents.push(description_of_experiment);
    introductionComponents.push(start_experiment);
    
    for (const thisComponent of introductionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function introductionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'introduction' ---
    // get current time
    t = introductionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *description_of_experiment* updates
    if (t >= 0.0 && description_of_experiment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      description_of_experiment.tStart = t;  // (not accounting for frame time here)
      description_of_experiment.frameNStart = frameN;  // exact frame index
      
      description_of_experiment.setAutoDraw(true);
    }
    
    
    // *start_experiment* updates
    if (t >= 0.0 && start_experiment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_experiment.tStart = t;  // (not accounting for frame time here)
      start_experiment.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      start_experiment.clock.reset();
      start_experiment.start();
    }
    
    if (start_experiment.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_experiment.getKeys({keyList: ['space'], waitRelease: false});
      _start_experiment_allKeys = _start_experiment_allKeys.concat(theseKeys);
      if (_start_experiment_allKeys.length > 0) {
        start_experiment.keys = _start_experiment_allKeys[_start_experiment_allKeys.length - 1].name;  // just the last key pressed
        start_experiment.rt = _start_experiment_allKeys[_start_experiment_allKeys.length - 1].rt;
        start_experiment.duration = _start_experiment_allKeys[_start_experiment_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of introductionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function introductionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'introduction' ---
    for (const thisComponent of introductionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(start_experiment.corr, level);
    }
    psychoJS.experiment.addData('start_experiment.keys', start_experiment.keys);
    if (typeof start_experiment.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_experiment.rt', start_experiment.rt);
        psychoJS.experiment.addData('start_experiment.duration', start_experiment.duration);
        routineTimer.reset();
        }
    
    start_experiment.stop();
    // the Routine "introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'dataframes/localizer.csv',
      seed: 12345, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(probe_routineRoutineBegin(snapshot));
      trialsLoopScheduler.add(probe_routineRoutineEachFrame());
      trialsLoopScheduler.add(probe_routineRoutineEnd(snapshot));
      trialsLoopScheduler.add(response_routineRoutineBegin(snapshot));
      trialsLoopScheduler.add(response_routineRoutineEachFrame());
      trialsLoopScheduler.add(response_routineRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function probe_routineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'probe_routine' ---
    t = 0;
    probe_routineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('probe_routine.started', globalClock.getTime());
    // Run 'Begin Routine' code from code
    trials.addData("image_onset_time", (globalClock.getTime() - startTime));
    stimulus_pulse_started = false;
    stimulus_pulse_ended = false;
    trigger_code = dict_answer[category];
    
    probe.setImage(image_name);
    // keep track of which components have finished
    probe_routineComponents = [];
    probe_routineComponents.push(preblank);
    probe_routineComponents.push(probe);
    probe_routineComponents.push(postblank);
    
    for (const thisComponent of probe_routineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function probe_routineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'probe_routine' ---
    // get current time
    t = probe_routineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code
    if ((! debug)) {
        if (((probe.status === PsychoJS.Status.STARTED) && (! stimulus_pulse_started))) {
            psychoJS.window.callOnFlip(dev.activate_line, trigger_code);
            stimulus_pulse_start_time = globalClock.getTime();
            stimulus_pulse_started = true;
        }
        if ((stimulus_pulse_started && (! stimulus_pulse_ended))) {
            if (((globalClock.getTime() - stimulus_pulse_start_time) >= 0.005)) {
                stimulus_pulse_ended = true;
            }
        }
    }
    
    
    // *preblank* updates
    if (t >= 0.0 && preblank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      preblank.tStart = t;  // (not accounting for frame time here)
      preblank.frameNStart = frameN;  // exact frame index
      
      preblank.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + np.random.choice([0.5, 1], size=1)[0] - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (preblank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      preblank.setAutoDraw(false);
    }
    
    // *probe* updates
    if (((preblank.status == FINISHED)) && probe.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe.tStart = t;  // (not accounting for frame time here)
      probe.frameNStart = frameN;  // exact frame index
      
      probe.setAutoDraw(true);
    }
    
    if (probe.status === PsychoJS.Status.STARTED && frameN >= (probe.frameNStart + 1)) {
      probe.setAutoDraw(false);
    }
    
    // *postblank* updates
    if (((probe.status == FINISHED)) && postblank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postblank.tStart = t;  // (not accounting for frame time here)
      postblank.frameNStart = frameN;  // exact frame index
      
      postblank.setAutoDraw(true);
    }
    
    if (postblank.status === PsychoJS.Status.STARTED && t >= (postblank.tStart + np.random.choice([0.5, 1], size=1)[0])) {
      postblank.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of probe_routineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function probe_routineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'probe_routine' ---
    for (const thisComponent of probe_routineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('probe_routine.stopped', globalClock.getTime());
    // the Routine "probe_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function response_routineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'response_routine' ---
    t = 0;
    response_routineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('response_routine.started', globalClock.getTime());
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    tell_response.setText(msg);
    // keep track of which components have finished
    response_routineComponents = [];
    response_routineComponents.push(response);
    response_routineComponents.push(tell_response);
    
    for (const thisComponent of response_routineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function response_routineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'response_routine' ---
    // get current time
    t = response_routineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *response* updates
    if (t >= 0.0 && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }
    
    if (response.status === PsychoJS.Status.STARTED) {
      let theseKeys = response.getKeys({keyList: ['1', '2'], waitRelease: false});
      _response_allKeys = _response_allKeys.concat(theseKeys);
      if (_response_allKeys.length > 0) {
        response.keys = _response_allKeys[_response_allKeys.length - 1].name;  // just the last key pressed
        response.rt = _response_allKeys[_response_allKeys.length - 1].rt;
        response.duration = _response_allKeys[_response_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *tell_response* updates
    if (frameN >= 0.0 && tell_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tell_response.tStart = t;  // (not accounting for frame time here)
      tell_response.frameNStart = frameN;  // exact frame index
      
      tell_response.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of response_routineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function response_routineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'response_routine' ---
    for (const thisComponent of response_routineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('response_routine.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(response.corr, level);
    }
    psychoJS.experiment.addData('response.keys', response.keys);
    if (typeof response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('response.rt', response.rt);
        psychoJS.experiment.addData('response.duration', response.duration);
        routineTimer.reset();
        }
    
    response.stop();
    // the Routine "response_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function End_experimentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End_experiment' ---
    t = 0;
    End_experimentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    End_experimentComponents = [];
    End_experimentComponents.push(The_End);
    
    for (const thisComponent of End_experimentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function End_experimentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End_experiment' ---
    // get current time
    t = End_experimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *The_End* updates
    if (t >= 0.0 && The_End.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      The_End.tStart = t;  // (not accounting for frame time here)
      The_End.frameNStart = frameN;  // exact frame index
      
      The_End.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (The_End.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      The_End.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of End_experimentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function End_experimentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End_experiment' ---
    for (const thisComponent of End_experimentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  // Run 'End Experiment' code from code_2
  console.log((globalClock.getTime() - startTime));
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
