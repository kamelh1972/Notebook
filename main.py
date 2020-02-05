
# Python program to display calendar of
# given month of the year

# import module
import calendar
import datetime
from View.view_event import *
#import local

if __name__ == '__main__':
    date= datetime.date.today()
    str= date

    yy = 2020
    mm = 2

# display the calendar
    print(str)
    print(calendar.month(yy, mm))


    event = Event()
    user_choice = ""


event = ViewEven()
event.action_event()
