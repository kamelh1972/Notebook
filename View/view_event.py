
from Model.model_event import *
from View.view_hydrate import *
import datetime
class ViewEven():

    def __init__(self):
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None

    def action_event(self):
        model = Event()
        #model1 = Hydrate()
        print("action\n a : voir évènement\n b : supprimer évènement \n c : ajouter évènement \n d : modifier évènement \n q: quit \n")
        print("que voulez-vous faire")
        action = input(": ")

        if action == "a":
            #date = input("tapez date évènement:")
            year = int(input("entree year"))
            month = int(input("entrer month"))
            day = int(input("entrer day"))
            date = datetime.date(year,month,day)
            print("votre agenda du {}".format(date))
            for row in model.display_event(date):
                print(row)

        elif action == "b":
            date = input('Quel date voulez-vous supprimer')
            heure = input("quelle heure voulez-vous supprimer")
            model.delete_event(date,heure)

        elif action == "c":
            print("Veuillez renseignez les champs suivants")
            titre = input(" titre:")
            date = input(" date:")
            heure = input(" heure:")
            description = input("description:")
            model.add_event(titre,date,heure,description)

        elif action == "d":
            column = input("Quel évènement voulez-vous modifier : ")

            date = input(" date :")
            heure = input(" heure :")
            nouvelles = input("nouvel evenement")

            model.update_event(column,date,heure,nouvelles)

        else:
            action == "q"
            print("A bientot")
