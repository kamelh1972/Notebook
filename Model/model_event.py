from connection import *

class Event():
    def __init__(self):
        self.titre = None
        self.date = None
        self.heure = None
        self.description = None
        self.db = connection()
        sel

    def display_event(self,date):
        sql="SELECT * FROM events WHERE date = %s;",(self.date,)
        self.date = input("taper date de l'evènement")
        self.db initialize_connection()
        self.db.cursor.execut()
