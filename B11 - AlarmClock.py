## B11) Alarm Clock - which displays day, month, and time and accepts the alarm time to beep

## Will not work if you don't have "BeepSound.mp3" in pwd.

def beep():
	from playsound import playsound
	playsound("BeepSound.mp3")

from datetime import datetime
import calendar
now_ = datetime.now()
print(calendar.day_name[datetime.today().weekday()], now_.day, now_.month, now_.strftime("%H:%M:%S"), sep = ' ')

limit = str(input('Enter date: '))
try:
    given_time = datetime.strptime(limit, '%H:%M:%S')
except ValueError:
    print ("Incorrect format")
    quit()
    
import time
while True:
	time.sleep(1)
	if datetime.now().strftime("%H:%M:%S") == limit:
		print("Done.")
		beep()
		break

