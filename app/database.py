import sqlite3

connection=sqlite3.connect("sql.db")

cur=connection.cursor()

#cur.execute("""
#CREATE TABLE IF NOT EXISTS shipment (
 #   id TEXT PRIMARY KEY,
  #  content TEXT
##)
#"")
#cur.execute("""
##INSERT INTO shipment
##values(1270,12.5,"CPU","placed")
#""")

#cur.execute(""" SELECT * FROM shipment    """)
#update
content ="xyzcd"
id=1270
cur.execute("""UPDATE shipment
SET content = ?
WHERE id=?""",(content,id))
#cur.execute("SELECT*FROM shipment")
#print(cur.fetchall())

connection.commit()

connection.close()