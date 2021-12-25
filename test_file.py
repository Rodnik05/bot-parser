import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('''CREATE TABLE olimpiads
            (name text, level text, link text, text text)''')
cur.execute("INSERT INTO olimpiads VALUES ('text', 'TEST', 'TEST')")

con.commit()

con.close