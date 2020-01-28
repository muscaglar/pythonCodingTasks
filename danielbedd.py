#program to play daniel every hour.

import time
import VLC

while True:
    danny = vlc.MediaPlayer("/Users/vito/Desktop/gotta/m4p")
    danny.play()
    time.sleep(180)
    danny.stop()
    time.sleep(3600)
