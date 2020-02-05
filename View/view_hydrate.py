from Model.model_event import *

class Hydrate:
    def __init__(self,database):
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        self.hydrate = database

    def hydrate(self,database):
        """function to set a value to each attribut based on a dictionnary"""
        for key, value in data.items():
            # Prevent he creation of unwanted attributs
            if hasattr(self, keys):
                setattr(self, keys, values)

    def show_event(self):
        text = "-------------\n \
        titre: {}\n \
        date: {}\n \
        heure: {}\n \
        description: {}\n \
        print(text.format(self.titre, self.date, self.heure, self.description))
