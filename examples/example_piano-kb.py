#!/usr/bin/env python

from minimix import minimix
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

# transforms the .ogg file into a .wav file
wav_file = toWav('./sounds/aaa.ogg')

# creates a folder 'soundfonts' with all the shifts of the pitches
sf_folder = shifts(wav_file,range(-19,18))

# creates a configuration file aaa.cf in the configs folder
cf_file = cf(sf_folder,'keyboards/piano.kb')

# launches minimix.
minimix(cf_file)

# Note that these steps only have to be takn once. In the future you
# can call minimix drectly by calling minimix('./configs/aaa.cf')
