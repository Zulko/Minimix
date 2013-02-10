SOUNDS FOR MINIMIX
by Zulko

aaa.ogg - me trying to sing "aaaaaah". I kept the best of 15 attempts.
bowl.ogg - made with... guess what.

The pitch of these sounds cannot be directly shifted by Soundstretch as
the files are '.ogg', an extension that Soundstretch does not recognize.
To use the files inside minimix, you will need to convert them into wav files first.
thiw can be done with toWav(oggfile) (see sound.py) of directly with ffmpeg or avconv
(which are the same program):

avconv -i bowl.ogg bowl.wav


Both sounds are featured in my youtube demonstration video
http://www.youtube.com/watch?v=XM0obSYPjnM&feature=share&list=UUeACpJ3-DIqjtBQFxVaABYA


