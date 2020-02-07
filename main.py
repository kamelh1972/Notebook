
# Python program to display calendar of
# given month of the year

# import module
import os
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


    #event = ViewEven()
    #user_choice = ""
    #while user_choice != "q":
        #user_choice = input("action\n a : voir évènement\n b : supprimer évènement \n c : ajouter évènement \n d : modifier évènement \n q : quit")


    event = ViewEven()
    event.action_event()
