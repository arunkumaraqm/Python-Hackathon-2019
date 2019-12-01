## A8) Alarm Clock - A simple clock which beeps after X number of minutes and seconds.

## Please include "BeepSound.mp3" in pwd.
## Please install playsound.

import time as T

from playsound import playsound


minutes, seconds = map(int, input("Enter Duration: ").split(':'))
if minutes > 60 or seconds > 60: 
	print("Invalid")	
	quit()
seconds += minutes * 60
initial_time = T.time()

while True:
        T.sleep(1)
        passed_time = T.time() - initial_time
        if passed_time > seconds:
                print("Time's Up!")
                playsound('BeepSound.mp3')
                break
