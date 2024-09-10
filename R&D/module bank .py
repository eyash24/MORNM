# python program for understanding the working plyer module
print("hello world")

import plyer

#notification
plyer.notification.notify(title="notification",message="my first notification",timeout=3)
print("bye")
print()

#battery
print(plyer.battery.status)


# text to speech
plyer.tts.speak(message="my first notification ")

import time
seconds = time.time()
local_time = time.ctime(seconds)
print("Local time:", local_time)
result = time.localtime(seconds)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_min:",result.tm_min)
print(type(result.tm_hour))

import xlrd
# trial
file_location="/Users/yashlucky/Desktop/yash_Daily Schedule .xlsx"
workbook = xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(1)
print (workbook.sheet_names())
data=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
# for using data subtract 1 from both row and col value as python starts from 0 0 and not form 1 1

#for the program

def time_list(r,c):
    #to primt the time data in a list format
    data_ = data[int(r)][int(c)]
    list_ = list()
    list_ = data_.split()
    str_ = list_[0]
    list_.remove(list_[0])
    list_2 = str_.split('/')
    list_2.extend(list_)
    print(list_2)

time_list(1,0)
print(data[0][2])

