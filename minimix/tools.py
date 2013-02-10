#
# Helper functions to create instruments and keyboard
# configurations for minimix
#
import os
import csv
import pygame as pg

def readkb(kb_file):
    """
    reads a .kb file and returns a list of keys
    """
    
    return [ key.strip('\n').split('|') for key in open(kb_file, 'rb')]

def keyboard_maker(outputfile):
    """ 
    Opens an interactive session that lets you hit the keys
    of your keyboard in the desired order. Press escape to finish.
    The resulting .kb file is written as outputfile.
    """
    
    kb_file = open(outputfile, 'w')
    
    pg.init()
    screen = pg.display.set_mode((640,480))
    while True:
        event =  pg.event.wait()
        if event.type is pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                break
            else:
                name = pg.key.name(event.key)
                print name
                kb_file.write(name + '\n')
    kb_file.close()
    pg.quit()

def key_names():
    """
    Opens an interactive session that lets you hit the keys
    of your keyboard and see how pygame named these. Press escape to exit.
    """
        
    pg.init()
    screen = pg.display.set_mode((640,480))
    
    while True:
        
        event =  pg.event.wait()
        
        if event.type is pg.KEYDOWN:
            
            if event.key == pg.K_ESCAPE:
                  
                break
                
            else:
                
                print pg.key.name(event.key)
    
    pg.quit()



def make_conf(folder, output,keyslist=None, startfile=0):
    """
    Makes a configuration file out of a folder.
    Uses the folder's name as a name for the .df output.
    Uses the piano.kb keyboard configuration as default.
    Args:
        folder (str): a folder containing wav or ogg files
        output (str): name of the output file, e.g. 'myconf.conf'
        keyslist (list): a list of list of keyboard keys. If the list is
        [['a'] ['z'] ['e','r','t']], then the first file in alphabetical
        order in the folder will be attributed to the key 'a', the second
        to 'z', and the thrid will be played on press of either 'e','r',
        or 't'. We recommend to provide this list as a .kb read : 
        keyslist = read_kb('piano.kb')
    """
    
    conf_file = csv.writer(open(output, 'wb'), delimiter=',')
    files = filter(lambda s : s.endswith(('.wav','.ogg')),
                   os.listdir(folder))
              
    files = sorted(files)[startfile:]
    
    if keyslist is None:
        
        keyslist = len(files) * [['#']]
        
    for name,keys in zip(files,keyslist):
        
        for k in keys:
            
            conf_file.writerow([k,' ' + '%s/%s'%(folder,name)])
