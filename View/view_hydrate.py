from Model.model_event import *

class Hydrate:
    def __init__(self,database=False):
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        if database:
            self.hydrate(database)

    def hydrate(self):
        """function to set a value to each attribut based on a dictionnary"""
        for key, value in data.items():
            # Prevent he creation of unwanted attributs
            if hasattr(self, key):
                setattr(self, key, value)

    def show_event(self):
        text = "-------------\n \
        titre: {}\n \
        date: {}\n \
        heure: {}\n \
        description: {}\n"
        print(text.format(self.titre, self.date, self.heure, self.description))
