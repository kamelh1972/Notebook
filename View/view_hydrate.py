from Model.model_event import *

class Hydrate:

    def hydrate(self,database):
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
        description: {}\n \
        print(text.format(self.titre, self.date, self.heure, self.description))
