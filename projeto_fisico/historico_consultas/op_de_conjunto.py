import sqlite3

connection = sqlite3.connect('steam.db')
cursor = connection.cursor()

cursor.execute("""
    SELECT user_ID FROM Desenvolvedor
    INTERSECT
    SELECT user_ID FROM Distribuidor;
""")

for i in cursor.fetchall():
    print(i)

connection.close()