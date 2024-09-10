import plyer
import time
import xlrd
from playsound import playsound

'''
inputs to take 
time interval (required for interval list)
location of excel file 
title,message,timeout for notification 
sound effect of notification location 
'''

#file location is required for the excel sheet location and access
file_location = "/Users/yashlucky/Desktop/yash_Daily Schedule .xlsx"
workbook = xlrd.open_workbook(file_location)
#sheet_by_index(a), a displays the sheet number
sheet = workbook.sheet_by_index(1)
data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
# for using data subtract 1 from both row and col value as python starts from 0 0 and not form 1 1
n_rows = int(sheet.nrows)
n_cols = int(sheet.ncols)

def time_list(r,c):
    #code to print the time data in a list format [hr,min,sec,AM/PM]
    data_ = data[int(r)][int(c)]
    global list_ # in order to use the variable outside of the function we use global as a keyword
    global timeinlist
    list_ = list()
    timeinlist=list()
    list_ = data_.split()
    str_ = list_[0]
    list_.remove(list_[0])
    list_2 = str_.split('/')
    list_2.extend(list_)
    timeinlist=list2

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

def datatime_24hours(r,c):
    #converts 12 hour digital clock into 24 hours digital clock
    time_list(r,c)
    if timeinlist[3] == "AM":
        current_hour = timeinlist[0]
    elif timeinlist[3] == "PM" and timeinlist[0]>12:
        current_hour = timeinlist[0]+12
        timeinlist[0] = current_hour

li_min_list = list()
time_interval_=15 # convert this to variable as given in the input section
for li_min_ in range(0, 61, time_interval_):
    li_min_list.append(li_min_)

current_time()
i = 2
day_col=None
day_found = False
while day_found == False:
    # to find which day it is, there after we proceed
    if i > n_rows:
        print("error in the system")
        error = True
    else:
        if day_ == data[0][i]:
            day_found = True
            break
        else:
            i += 1
    day_col = i

    # code to find the row and the col
    error = False
    stop_ = False
    time_row = 0
    time_row_found = False
    while stop_ == False:
        current_time()
        j = 1
        time_hour_row = 0
        time_hour_found = False
        while time_hour_found == False:
            # code to find the hour row
            r = j
            c = 0
            data_ = data[int(r)][int(c)]
            global list_  # in order to use the variable outside of the function we use global as a keyword
            global timeinlist
            global list_2
            list_ = list()
            timeinlist = list()
            list_2 = list()
            list_ = data_.split()
            len_ = len(list_)
            if len_ == 2:
                str_ = list_[0]
                list_.remove(list_[0])
                list_2 = str_.split('/')
                list_2.extend(list_)
                timeinlist = list_2
            else:
                print()

        if int(timeinlist[0]) < int(tm_hour):
            j += 1
        elif int(timeinlist[0]) == int(tm_hour):
            time_hour_found = True
            time_hour_row = j

        j = time_hour_row
        row_min = 0
        while time_min_found == False:
            if li_min_list[row_min] == tm_min:
                time_row = j
                time_min_found = True
            elif li_min_list[row_min] < tm_min and li_min_list[row_min + 1] > tm_min:
                time_row = j
                time_min_found = True
            else:
                j += 1
            time_row = j
        print(time_row)
    # code to find the row and the col
    error = False
    stop_ = False
    time_row = 0
    time_row_found = False
    while stop_ == False:
        current_time()
        j = 1
        time_hour_row = 0
        time_hour_found = False
        while time_hour_found == False:
            # code to find the hour row
            r = j
            c = 0
            data_ = data[int(r)][int(c)]
            global list_  # in order to use the variable outside of the function we use global as a keyword
            global timeinlist
            global list_2
            list_ = list()
            timeinlist = list()
            list_2 = list()
            list_ = data_.split()
            len_ = len(list_)
            if len_ == 2:
                str_ = list_[0]
                list_.remove(list_[0])
                list_2 = str_.split('/')
                list_2.extend(list_)
                timeinlist = list_2
            else:
                print()

        if int(timeinlist[0]) < int(tm_hour):
            j += 1
        elif int(timeinlist[0]) == int(tm_hour):
            time_hour_found = True
            time_hour_row = j

        j = time_hour_row
        row_min = 0
        while time_min_found == False:
            if li_min_list[row_min] == tm_min:
                time_row = j
                time_min_found = True
            elif li_min_list[row_min] < tm_min and li_min_list[row_min + 1] > tm_min:
                time_row = j
                time_min_found = True
            else:
                j += 1
            time_row = j
        print(time_row)

    #time_row gives us the row no for utilisation
    #day_col gies us the col number for utilisation

# after finding the row and col number, proceeding to the notification part


'''
list of routine and time intervals 
use of time intervals for time.sleep module 
use of routine subs for notification module 
'''


time_col=0
time_col_found = False
i=0
while time_col_found == False:
    # to find which day it is, there after we proceed
    if i > n_rows:
        print("error in the system")
        error = True
    else:
        if "Time" == data[0][i]:
            time_col_found = True
            time_col = i
            break
        else:
            i += 1

i=time_row
list_routine_sub=list()
list_time_intervals=list()

while i<=n_rows:
    sub=(sheet.cell_value(i, day_col))
    list_routine_sub.append(sub)
    time_=(sheet.cell_value(i,time_col))
    list_time_intervals.append(time_)
    i+=1


#notification
def notify_(title,message,timeout):
    global title_
    global message_
    global timeout_
    title_=title
    message_=message
    timeout_=int(timeout)
    if title == None :
        title_="Alert"
    else:
        title_=title

    if timeout == None:
        timeout_ = 5
    else:
        timeout_ = timeout

    plyer.notification.notify(title=title_, message=message_, timeout=timeout_)
    playsound('/Users/yashlucky/Downloads/ding-sound-effect/Ding-sound-effect.mp3')




