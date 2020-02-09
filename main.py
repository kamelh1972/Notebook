
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


    user_choice = ": "
    while user_choice != "q":
        event = ViewEven()
        event1 = Hydrate()
        #event.action_event()
        user_choice = input("que voulez-vous faire:\n a : voir évènement\n b : supprimer évènement \n c : ajouter évènement \n d : modifier évènement \n q : quit \n")
        #print("action\n a : voir évènement\n b : supprimer évènement \n c : ajouter évènement \n d : modifier évènement \n q: quit \n")
        #action = input(": ")
        if user_choice == "a":
            #year = int(input("entree year"))
            #month = int(input("entrer month"))
            #day = int(input("entrer day"))
            date = input("quelle date voulez-vous voir")
            #date = datetime.date(date)
            print("votre agenda du {}".format(date))
            #event.display(date)
            event.display(date)

        elif user_choice == "b":
            date = input('Quel date voulez-vous supprimer')
            heure = input("quelle heure voulez-vous supprimer")
            event.delete(date,heure)

        elif user_choice == "c":
            print("Veuillez renseignez les champs suivants")
            titre = input(" titre:")
            date = input(" date:")
            heure = input(" heure:")
            description = input("description:")
            event.add(titre,date,heure,description)
            print("vos changement ont ete effectues")

        elif user_choice == "d":
            column = input("Quel évènement voulez-vous modifier(titre,date,heure,description) : ")
            date = input(" date :")
            heure = input(" heure :")
            nouvelles = input("nouvel evenement")
            event.update(column,date,heure,nouvelles)
        else:
            user_choice == "q"
            print("A bientot")
