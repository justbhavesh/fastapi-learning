import sqlite3
from app.schema import Ship
class Database:
    def __init__(self,db_name):
      self.con=sqlite3.connect(db_name,check_same_thread=False)
      self.cur=self.con.cursor()
    def create_table(self,name):
       self.cur.execute(f"""
    CREATE TABLE IF NOT EXIST{name} shipments
    (id integer PRIMARY KEY AUTOINCREMENT,
      content TEXT,
        weight REAL,
        status TEXT)
       """)
       
       self.con.commit()

    def create_shipment(self,shipments:Ship):
       self.cur.execute("""
            INSERT INTO shipment (weight,content,status)VALUE(:weight,:content,:status)
        

""",{**shipments.model_dump(),"status":"Placed"})
       self.con.commit.cur.lastrowid
      
    def get_shipment(self,sid:int):
       self.cur.execute("""SELECT * FROM shipment WHERE id = :sid""",{"id":sid})


db = Database("supply.db")