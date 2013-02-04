#
# A MINIMALISTIC MIXER ! BY ZULKO 2012
#


import pygame as pg
import csv
import time


SAMPLE_WIDTH = 16
FPS = 44100
N_CHANNELS = 2
BUFFER = 2**9
    
def minimix(config_file,mode = 'instrument',fadeout_time=50):
    """
    Opens an interface that lets you press the keys of your keyboard
    to plays the related soundfiles as sepcified in the provided
    configuration file.
    
    Args:
       config_file (str):  A file associating keyboard keys with
                           file names. Each line must be of the form
                           key , filename.
                       
       mode (str) :
            instrument -- causes autorepeat of samples as long
                            as the key is pressed.
            sustain -- causes autorepeat of the samples until its
                       key is pressed again.
            player -- striking the key causes the sound to play once. 
    
    Returns:
       a list of the (time,events).
    """
    
    repeat = 0 if (mode is 'player') else (-1)
    
    pg.mixer.pre_init(FPS,-SAMPLE_WIDTH,N_CHANNELS,BUFFER)
    pg.init()
    screen = pg.display.set_mode((640,480))
    
    
    
    
    ##### READ CONF FILE
    
    key2sound = {}
    key2file = {}
    config = csv.reader(open(config_file, 'rb'), delimiter=',')
    
    for key, soundfile in config:
        
        key,soundfile = key.strip(' '),soundfile.strip(' ')
        
        if key is not '#':
            
            key2file[key] = soundfile
            key2sound[key] = pg.mixer.Sound(soundfile)
    
    events_list = []
    currently_playing = {k : False for k in key2sound.iterkeys()}
    
    
    ##### MAIN LOOP
    
    while True:
        
        event =  pg.event.wait()
      
        if event.type in (pg.KEYDOWN,pg.KEYUP):
            key = pg.key.name(event.key)
              
            if key in key2sound:
                
                if event.type == pg.KEYDOWN:
                    
                    if (mode == 'sustain') and currently_playing[key]:
                        
                        key2sound[key].stop()
                        currently_playing[key] = False
                        
                    else:
                        
                        key2sound[key].play(repeat) 
                        currently_playing[key] = True
                    
                    events_list.append((time.time(),key2file[key]))
                    
                elif event.type == pg.KEYUP and (mode == 'instrument'):
                    
                    key2sound[key].fadeout(fadeout_time)
                    currently_playing[key] = False
                    
                    events_list.append((time.time(),key2file[key]))
            
            elif event.key == pg.K_ESCAPE:
                
                break
    
    pg.quit()
    
    return events_list   
