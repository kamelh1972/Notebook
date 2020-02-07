from Model.connexion import *

class Event():
    def __init__(self):
        self.db = connection()


    def display_event(self,date):
        sql="SELECT * FROM events WHERE date = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,date)
        result=self.db.cursor.fetchall()
        self.db.close_connection()
        return result


    def delete_event(self,date, heure):
        sql="DELETE FROM events WHERE date = %s AND heure = %s;"
        self.db.initialize_connection()
        argument= (date,heure)
        self.db.cursor.execute(sql, argument)
        self.db.connection.commit()
        self.db.close_connection()

    def add_event(self,title,date,heure,description):
        sql="INSERT INTO events(titre,date,heure,description) VALUES (%s,%s,%s,%s);"
        argument = (titre, date,heure,description)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        self.db.connection.commit()
        self.db.close_connection()

    def update_event(self,column,date,heure,nouvelles):
        sql="UPDATE events SET "+ column+" =%s WHERE date=%s and heure =%s; "
        argument= (nouvelles,date,heure)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        self.db.connection.commit()
        self.db.close_connection()

    #def next_month(self,current_month):
        #self.current_month =
