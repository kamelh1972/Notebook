from Model.connexion import *

class Event():
    def __init__(self):
        self.db = connection()


    def display_event(self):
        sql="SELECT * FROM events WHERE date = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, date)
        result=self.db.connect.cursor.fetchall()
        self.conn.close_connection()
        return result

    def delete_event(self,titre):
        sql="DELETE FROM events WHERE titre = %s;",(titre,)
        self.titre = input('Quel evènement voulez-vous supprimer')
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(titre))
        self.db.connect.cursor.fetchall()
        self.conn.close_connection()

    def add_event(self,arg):
        self.titre = input("entrer titre")
        self.date = input("entrer date")
        self.heure = input("entrer heure")
        self.description = input("entrer description")
        sql="INSERT INTO events(titre,description) VALUES (%s,%s,%s,%s);"
        argment = (arg.titre, arg.date,arg.heure,arg.description)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(argument))
        self.db.connect.commit()
        self.conn.close_connection()

    def update_event(self):
        column = input("Que voulez-vous modifier ? (titre, date, heure, description) : ")
        value = input("Nouvelle valeur : ")
        sql="UPDATE events SET + column + = %,WHERE date = %s AND heure = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(titre,date,heure,description))
        self.db.connect.commit()
        self.conn.close_connection()
