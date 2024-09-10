import plyer
import time
import xlrd
from playsound import playsound

#input section
'''
print("Welcome to our porject MORNM")
print("for the computer to proceed with the program please enter the following details ")
excel_sheet_location = input("enter the excel sheet file location : ")
time_interval = input("enter the time interval of your routine: ")
sound_effect_location = input("enter the ringtone location for the notifier : ")
title_notificatio = input("enter the title for each notification : ")
timeout_time = input("Amount of time for which the notification will be displayed : ")
'''

#for now
title_notification="Alert!"
excel_sheet_location = "/Users/yashlucky/Desktop/yash_Daily Schedule .xlsx"
sound_effect_location = '/Users/yashlucky/Downloads/ding-sound-effect/Ding-sound-effect.mp3'
timeout_time = 3

#file location is required for the excel sheet location and access
file_location = "/Users/yashlucky/Desktop/yash_Daily Schedule .xlsx"
workbook = xlrd.open_workbook(file_location)
#sheet_by_index(a), a displays the sheet number
sheet = workbook.sheet_by_index(1)
global data_cell
data_cell = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
# for using data subtract 1 from both row and col value as python starts from 0 0 and not form 1 1
n_rows = int(sheet.nrows)
n_cols = int(sheet.ncols)
str_=str(input())
if str_ == "123":
    print("okay")
else:
    raise TypeError("Please follow the instructions while working on your excel sheet")