
from Model.model_event import *

class ViewEven():

    def __init__(self):
        self.titre = None
        self.date = None
        self.heure =None
        self.description = None

    def action_event(self):
        model = Event()
        print("action\n a : voir évènement\n b : supprimer évènement \n c : ajouter évènement \n d : modifier évènement")
        print("que voulez-vous faire")
        action = input(": ")
        if action == "a":
            model.display_event()

        elif action == "b":
            model.delete_event()

        elif action == "c":
            model.add_event()

        elif action == "d":
            column = input("Que voulez-vous modifier ? (name, firstname, email, age, password, pseudo) : ")
            value = input("Nouvelle valeur : ")
            user[column] = value
            model.update_event()
