#
# Helper functions to process sounds for minimix
#

import wave
import scipy.io.wavfile as wf
import os

def toWav(wavFileName, outputName=None):
	 
	 if outputName is None:
		 fileName, fileExtension = os.path.splitext(wavFileName)
		 outputName = fileName + '.wav'
		 
	 os.system('avconv -i %s %s'%(wavFileName,outputName))
	 
	 return outputName


def shift_wav(wavfile,output,shifts,verbose=False):
    """
    Makes new sounds by shifting the pitch of a sound.
    Requires soundstrech installed.
    
    Args:
        wavfile : Name of the file containing the original sound
        output: name to use as a prefix for the output files and for
                the output folder name
        shifts (list of int): specifies of how many half-tones the pitch
                shifts should be. For instance [-2,-1,1,2] will produce
                4 files containing the sound 2 half-tones lower, one
                halftone lower, one halftone higher and two halftones
                higher.
    """
    
    folder = os.path.dirname(output)
        
    if not os.path.exists(folder):
        
        os.makedirs(folder)
        
    for i,s in enumerate(shifts):
        
        outputfile = '%s%02d.wav'%(output,i)
        
        command = 'soundstretch %s %s -pitch=%d'%(wavfile,outputfile,s)
        if verbose:
            print command
        os.system(command)
    

def split_wav(wavfile,output,blanksSize = 2000):
    """
    Separates different sounds contained in a wav file.
    
    Args:
        wavfile (str): name of the file containing the original sound
        output (str): name to use as a prefix for the output file and for
                the output folder name
        blanksSize (int): number of empty frames between the sounds. You
        can tweak this parameter during the functions' run in order
        to get the expected number of sound samples.
    """
    
    rate, sound = wf.read(filename)
    L=len(sound)
    left = abs(sound[:,0])
    W = rate/100
    slidingMax = np.array( [left[i:(i+W)].max() for i in xrange(L-W)])
    samples = np.split(sound, np.where(slidingMax < 0.05*slidingMax.max())[0])
    
    ans = blanksSize
    while ans!='y':
        
        blanksSize = int(ans)
        nonEmptySamples = [s for s in samples if (len(s)>blanksSize)]
        print '%d samples found for bs=%d'%(len(nonEmptySamples),
                                             blanksSize)
        ans = raw_input('enter a blanksize or y: ')
        
    folder = os.path.dirname(outputname)
    if not os.path.exists(folder):
        
        os.makedirs(folder)

    for i,sample in enumerate(nonEmptySamples):
        
        fname =  '%s%03d.wav'%(outputname,i)
        wf.write(fname,rate,sample)
