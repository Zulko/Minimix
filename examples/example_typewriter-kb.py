#!/usr/bin/env python

from minimix import minimix
raw_input('')
from minimix.quick import *

"""
In this example we start in a working directory containing 4 subfolders
'configs','keyboards','soundfonts','sounds' 
We already have a keyboard file piano.kb in the 'kb' folder
and a soundfile of me saying 'aaa' in the 'sounds' folder.

We first first create a whole soundfont from aaa.ogg
by shifting the pitch of the sound (requires Soundstrech), then
we create a configuration file from our new soundfont. Use piano.kb as
the keyboard layout. Then we launch minimix. Have fun !
"""

# transforms the .ogg file into a .wav file in '/sounds'
wav_file = toWav('./sounds/bowl.ogg')

# creates a folder in '/soundfonts' with all the shifts of the pitches
sf_folder = shifts(wav_file,range(-25,25))

# creates a configuration file bowl.cf in '/configs'
cf_file = cf(sf_folder,'keyboards/typewriter.kb')

# launches minimix.
minimix(cf_file)

# Note that these steps only have to be takn once. In the future you
# can call minimix drectly by calling minimix('./configs/aaa.cf')
