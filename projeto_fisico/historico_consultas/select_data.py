import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

cursor.execute("""SELECT * FROM Jogo""")

for i in cursor.fetchall(): 
    print(i)

connection.close()