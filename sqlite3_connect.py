import sqlite3
conn = sqlite3.connect(':memory:')
curs = conn.cursor()
#curs.execute('CREATE TABLE colors(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING) ')
conn.commit()
curs.execute('INSERT INTO colors(name) values("Red")')
conn.commit()
curs.execute('SELECT * FROM colors')
conn.commit()
conn.close()