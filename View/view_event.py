
from Model.model_event import *



class ViewEven():

    def __init__(self):
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        self.model = None


    def display(self,date):
        model = Event()
        #model1 = Event()
        model.show_event_all(date)

    def delete(self,date,heure):
        model = Event()
        self.date = date
        self.heure = heure
        model.delete_event(date,heure)

    def add(self,titre,date,heure,description):
        model = Event()
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        model.add_event(titre,date,heure,description)

    def update(self,column,date,heure,nouvelles):
        model = Event()
        self.column = column
        self.date = None
        self.heure = None
        self.nouvelles = None
        model.update_event(column,date,heure,nouvelles)
