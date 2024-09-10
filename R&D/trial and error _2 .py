import plyer
import time
import xlrd
from playsound import playsound

global sound_effect_location
sound_effect_location = input("Enter the ringtone location : ")
sound_effect_location ="/Users/yashlucky/Desktop/Ding-sound-effect.mp3"
playsound(sound_effect_location)

def current_time():
    #displays current time
    week = {0: "Monday", 1: 'Tuesday', 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Local time:", local_time)
    result = time.localtime(seconds)
    global year
    global tm_hour
    global tm_min
    global tm_sec
    global day_
    global tm_wday
    year = result.tm_year
    tm_hour = result.tm_hour
    tm_min = result.tm_min
    tm_sec = result.tm_sec
    tm_wday = result.tm_wday # displays week day in number format
    day_ = week[int(tm_wday)]
    playsound(sound_effect_location)

seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)
result = time.localtime(seconds)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_min:",result.tm_min)

# fixing errors in the timing process
stop_ = False
trial = 0
while stop_ == False:
    print("trial ",trial+1)
    current_time()
    if tm_sec == 0:
        sleep_ = 0
        break
    elif tm_sec > 0 and tm_sec < 30:
        sleep_ = 30 - tm_sec
    elif tm_sec == 30:
        sleep_ = 30
    elif tm_sec > 30 and tm_sec < 60:
        sleep_ = 60 - tm_sec
    elif tm_sec == 60:
        sleep_ = 0
        break
    current_time()
    sleep_ -= 4
    time.sleep(sleep_)
    current_time()
    print()
    trial += 1

print()
current_time()





