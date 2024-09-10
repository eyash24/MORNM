'''
Welcome to project MORNM
MORNM or machine oriented routine notifier and modifier, a python programme that helps keep the user within the routine that they choose to follow.
The user has full access to modifying the code and his routine when ever he sees fit.
This program uses excel sheet to read and modify time table and send's notification accordingly.
Depending on the user notification can come via speech or desktop notifier.
The program is user friendly and can be used by all sort of people without any worry of any sort.
'''

# import section
import plyer
import time
import xlrd
from playsound import playsound

# default details
list_instructions_excel = [
    "This is a list of instructions that the user must follow for getting the program to work : ",
    "1. Create an new microsoft excel sheet ",
    "2. Guidance to make a daily schedule sheet: ",
    "(1) The first 2 columns contain the start time and stop time in 12 hr clock , time format : hr/min/sec AM/PM",
    "(2) From third to seventh write the week days ",
    "(3) In the eighth column write time ( required for the time interval )(time interval = stop - start time)",
    "3. It is the user's wish whether they want to make a 24 hr schedule or 12 hour schedule (advisable is 24 hour schedule)",
    "4. The user has to keep in mind that even a difference in space can make a major difference in the programs ",
    "5. Save the file and trace the file location as it will be required for future use "
    "All the best in creating your excel sheet! "
]

list_project_details = [
    "MORNM or machine oriented routine notifier and modifier, a python programme that helps keep the user within the routine that they choose to follow.",
    "The user has full access to modifying the code and his routine when ever he sees fit.",
    "This program uses microsoft excel sheet to read and modify time table and send's notification accordingly.",
    "Depending on the user notification can come via speech or desktop notifier.",
    "The program is user friendly and can be used by all sort of people without any worry of any sort."
]

# function section
def current_time():
    #displays current time
    week = {0: "Monday", 1: 'Tuesday', 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Local time:", local_time)
    print()
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
    tm_wday = result.tm_wday
    # displays week day in number format
    day_ = week[int(tm_wday)]

def time_list(r,c):
    # code to print the time data in a list format [hr,min,sec,AM/PM]
    data_ = data_cell[int(r)][int(c)]
    global list_
    global timeinlist
    list_ = list()
    timeinlist = list()
    list_ = data_.split()
    str_ = list_[0]
    list_.remove(list_[0])
    list_2 = list()
    list_2 = str_.split('/')
    list_2.extend(list_)
    timeinlist=list_2


# input section
print("Welcome to our project MORNM")
for i in list_project_details:
    print(i)
    time.sleep(1.5)
print()
answer = input("Have you worked with the program before : ")
if answer == "No" or answer == "no":
    answer_ = input("Would you like to know the instructions for building an ideal excel sheet which the program can use : ")
    print()
    if answer_ == "yes" or answer_ == "Yes" or answer_ == "y":
        for i in list_instructions_excel:
            print(i)
            time.sleep(1.5)
        print()
    else:
        print()
else:
    print()
print()

answer__ = input("Have you followed the excel instructions given by the computer while making your excel routine sheet: ")
if answer__ == "No" or answer__ == "no" or answer__ == "n":
    answer___ = input("Would you like to know the instructions for building an ideal excel sheet which the program can use : ")
    if answer___ == "yes" or answer___ == "Yes" or answer___ == "y":
        for i in list_instructions_excel:
            print(i)
            time.sleep(1.5)
    else:
        raise TypeError("Please follow the instructions while working on your excel sheet")
else:
    print()
print()
print("For the computer to proceed with the program please enter the following details: ")
excel_sheet_location = input("Enter the excel sheet file location : ")
time_interval = int(input("Enter the time interval of your routine (input taken as minutes): "))
sound_effect_location = input("Enter the ringtone location for the notifier : ")
title_notification = input("Enter the title for each notification : ")
timeout_time = int(input("Enter the amount of time for which the notification will be displayed (input taken as seconds) : "))

# Necessary as the notifications are supposed to be sent a few minutes before the actual routine time for the user to get ready
if time_interval > 5:
    print("How many minutes before the routine time do you want the notification to be sent (it should be less then", time_interval, "), if you do not  want just type 0 ")
    time_before_routinetime = int(input("Input the minutes : "))
else:
    print("the notifications will be sent a minutes before the actual routine time due to lack of time difference in time intervals. ")
    time_before_routinetime = 1
print()

# for running and debugging we use this
# file location is required for the excel sheet location and access
excel_sheet_location = "/Users/yashlucky/Desktop/yash_Daily Schedule .xlsx"
sound_effect_location = '/Users/yashlucky/Downloads/ding-sound-effect/Ding-sound-effect.mp3'

# xlrd.open_workbook(location) gets the computer access to read the contains of the excel sheet
# xlwt is a module that can be used for modifying the elements of an excel sheet
workbook = xlrd.open_workbook(excel_sheet_location)

list_sheet_names = workbook.sheet_names()
sheet_no = 0
if len(list_sheet_names) > 1:
    print("Name of sheets in the excel provided by you : ", list_sheet_names)
    sheet_name = input("Enter the sheet name that you want to use : ")
    Error = False
    if sheet_name in list_sheet_names:
        sheet_no = int(list_sheet_names.index(sheet_name))
        Error = False
    else:
        print("Error in the program ")
        Error = True
        raise TypeError("Error in the program")
else:
    sheet_no = 0
print("sheet number : ", sheet_no)

sheet = workbook.sheet_by_index(sheet_no)
global data_cell
# essential to use keyword global as the variable is used in functions too
# for using data subtract 1 from both row and col value as python starts from 0 0 and not form 1 1
data_cell = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

n_rows = int(sheet.nrows)
n_cols = int(sheet.ncols)

# message and title sections; essential for the notification part
list_subject = list()
for i in range(1, n_rows, 1):
    for j in range(2, n_cols, 1):
        str_ = str(data_cell[i][j])
        if str_ not in list_subject:
            list_subject.append(str_)
        else:
            continue

# list of all routine subject with out any duplicates
print("List of subjects : ", list_subject)
print()
dic_message_subject = dict()
print("The default message for all routine subject is : subject name time ")
ans = input("Do you want to enter a message for each routine subject : ")
if ans == "Yes" or ans == "yes" or ans == "y" or ans == "True" and Error == False:
    for i in list_subject:
        print("For the subject: ", i)
        print("For inputs such as 'None' and 'default' ; the default will be carried out")
        ans_ = str(input("Enter the message for the routine subject : "))
        if ans_ == "None" or ans_ == "default":
            dic_message_subject[i] = i + " time"
        else:
            dic_message_subject[i] = ans_
    print(dic_message_subject)
else:
    print("The default message will be used")
    for i in list_subject:
        dic_message_subject[i] = i + " time"

print("Name of subject", ":", "Message ", sep=" ")
for i in dic_message_subject:
    print(i, ":", dic_message_subject[i], sep="\t\t\t")
print()
# Dictionary containing subject wise messages
# Prints the dictionary in the form that the user can understand

# Program to find the cell number(row and col)
time.sleep(.5)
current_time()
j = 1
row_hour = 0
time_found = False
hour_found = False
stop_ = False
print()
print("Trials for finding row number (1) ")
print("S.no", "Time in excel", "Present time", sep="\t")
while j < n_rows and stop_ == False:
    while hour_found == False and j < n_rows:
        time_list(j, 0)
        print(j, end="\t\t\t")
        tn_hour = tm_hour
        n_hour = timeinlist[0]
        if timeinlist[3] == "AM" and timeinlist[0] == '12':
            n_hour = 0
        elif timeinlist[3] == "PM" and timeinlist[0] == '12':
            n_hour = timeinlist[0]
        elif timeinlist[3] == "AM":
            n_hour = timeinlist[0]
        elif timeinlist[3] == "PM":
            n_hour = int(timeinlist[0]) + 12
        else:
            raise TypeError("Error in the system")

        print(n_hour, tn_hour, sep="\t\t\t",end="\n")
        if int(tn_hour) == int(n_hour):
            hour_found = True
            row_hour = j
            time_found = True
            continue
        else:
            hour_found = False
            j += 1
    if time_found == True :
        stop_ = True
    else:
        stop_ = False

time.sleep(.5)
# intervals
li_min_list = list()
for li_min_ in range(0, 61, time_interval):
    li_min_list.append(li_min_)
print()
print("Time intervals : ", li_min_list)

# Program to find the more defined version of the row number
time.sleep(.5)
stop_2 = False
j = row_hour
row_min = 0
time_row = 0
current_time()
time_sleep = 0
print()
print("Trials for finding row number (2) ")
print("Trial.no", "row", sep="\t")
while row_min != 5 and stop_2 == False:
    print(row_min, end="\t\t\t")
    if li_min_list[row_min] == tm_min:
        time_row = row_hour + row_min
        time_sleep = 0
        # time_sleep gives us the time amount that the computer should wait for giving the first notification
        stop_2 = True
    elif li_min_list[row_min] < tm_min and li_min_list[row_min + 1] > tm_min:
        time_row = row_hour + row_min
        stop_2 = True
        time_sleep = li_min_list[row_min + 1] - tm_min
    else:
        stop_2 = False
    row_min += 1

    print(time_row, end="\n")

    if stop_2 == False:
        continue
    else:
        break

print()
time.sleep(.5)

current_time()

print("Today is : ", day_)

i = 0
day_col = None
day_found = False
print()
print("Trials for finding column number ")
print("Trial.no", "Present day", "Day found ", sep="\t\t")
while day_found == False:
    # Program to find which day it is
    print(i, end="\t\t\t\t")
    print(day_, end="\t\t\t")
    print(data_cell[0][i], end="\n")

    if i > n_rows:
        print("Error in the system")
        Error = True
        raise TypeError("Error in the system")
    else:
        if day_ == data_cell[0][i]:
            day_found = True
            break
        else:
            i += 1
    day_col = i

print()

print("Present day col: ", day_col)
print("Present time row: ", time_row)

# program to decide what is the amount of time the computer has to sleep before it can notify the user according to how much time before the user has sent the notification to go
if time_sleep == 0:
    time_row += 1
    time_sleep = time_interval - time_before_routinetime
elif time_sleep < time_before_routinetime and time_sleep > 0:
    time_row += 1
    time_sleep_ = time_sleep
    time_sleep = time_interval - time_before_routinetime + time_sleep_
elif time_sleep > time_before_routinetime:
    time_sleep_ = time_sleep - time_before_routinetime
    time_sleep = time_sleep_
    print()

# Code to make the seconds = 0
current_time()
if tm_sec == 0:
    minus_sec = 0
else:
    minus_sec = 60 - tm_sec
    time_sleep = time_sleep - 1
time.sleep(minus_sec)

print("Time_sleep : ", time_sleep)
current_time()
print()

# time_sleep gives us the time amount in seconds that the computer should wait before giving the first notification
time.sleep(time_sleep*60)
# we are waiting for the coming notification time hence present time_row  + 1
time_row += 1

# Notification section
def notify_(title,message,timeout):
    global title_
    global message_
    global timeout_
    title_ = title
    message_ = message
    timeout_ = int(timeout)
    if title_ == None:
        title_ = "Alert!"
    else:
        title_ = title

    if timeout_ == None:
        timeout_ = 10
    else:
        timeout_ = timeout

    plyer.notification.notify(title=title_, message=message_, timeout=timeout_)
    playsound(sound_effect_location)

# list_title_2 contains info by which title_2 can be derived
list_title_2 = [title_notification, time_before_routinetime, "left to go"]

title_2 = ""
for i in list_title_2:
    title_2 = title_2 + str(i) + " "

print("Notification record :")
for i in range(0, n_rows - time_row):
    print("Notification sent for : ", time_row)
    cell_value = str(data_cell[time_row][day_col])
    message_ = dic_message_subject[cell_value]
    timeout_ = timeout_time
    time_interval_ = time_interval
    # 0 as a input means the user does not want the notification before the actual routine time
    if time_before_routinetime > 0:
        print("Notification sent_  for ", cell_value)
        current_time()
        notify_(title_2, message_, timeout_)
    else:
        continue

    time.sleep(time_before_routinetime*60)
    timeout_2 = timeout_time + time_before_routinetime
    current_time()
    print("Notification sent for ", cell_value)
    notify_(title_notification, message_, timeout_2)

    time.sleep(((time_interval_ - time_before_routinetime) * 60)-timeout_time)
    print()
    time_row += 1

print()
print("Thank you for using our program")



'''
This is the end of the program

A few suggestions that can be done to make the user's work easy 
1. Already assign file locations for excel and sound ringtone so that the user does not have to write the path everytime.
2. Have a short range of the length difference for the routine subjects (Makes the dictionary display better).
3. Please do not alter any time section related codes if done they will get messy and at every turn result in an error.
4. Do not touch the defined functions cause they are delicate 
5. Always save the excel file and then run the program 
6. Make a file where all the user's input data can be stored and can be called upon when the user does not want to waste time entering them.

Thank you for using our program 
Thank you 
'''