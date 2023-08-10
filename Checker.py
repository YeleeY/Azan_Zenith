import os
import time
import subprocess
from API import *

subprocess.run(["python", "media player.py"])


while True:
    current_time = time.strftime("%H:%M")

    if str(current_time) == str(fajr) or str(current_time) == str(zuhr) or str(current_time) == str(asr) or str(current_time) == str(magrib) or str(current_time) == str(isha):
         
       subprocess.run(["python", "media player.py"])
