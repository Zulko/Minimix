#
# My personal collection of quick methods. They rely on a rational
# organisation of the working directory with folders 'configs',
# 'keyboards', 'soundfonts','sounds'
#

from sound import *
from tools import *

def cf(folder_name, keys = 'piano.kb',startfile=0):
	"""
	Makes a configuration file from of a folder.
	Uses the folder's name as a name for the .df output.
	Uses the piano.kb file as default.
	Reads the soundfiles in alphabetical order.
	"""
	  
	name = folder_name.split('/')[-1]
	cf_filename = './configs/%s.cf'%name
	make_conf(folder_name, cf_filename,keyslist=readkb(keys),
			  startfile=startfile)
	return cf_filename


def shifts(filename,shifts = range(-12,13)):
	"""
	Makes a soundfont out of a wav file by shifting	its tone.
	Stores the soundfont in /soundfonts/filename/
	Default range is +- one octave.
	"""
	filepath, fileext = os.path.splitext(filename)
	name = filepath.split('/')[-1]
	folder = '%s/../soundfonts/%s'%(os.path.dirname(filename),name)
	output = '%s/%s'%(folder,name)
	shift_wav(filename, output, shifts)
	return folder    
    

def split(wavfile):
	"""
	Makes a soundfont out of a wav file containing several sounds.
	Stores the soundfont in /soundfonts/filename/
	"""
	name = folder.split('/')[-1]
	filePath, fileExt = os.path.splitext(wavfile)
	fileName = filePath.split('/')[-1]
	foldername = '%s/../%s/'%(filePath,fileName)
	splitWav(wavToSplit, foldername)

