import sqlite3

connection = sqlite3.connect('steam.db')
cursor = connection.cursor()

# Retorna todos os usuários que nunca fizeram uma compra

cursor.execute("SELECT U.username FROM Usuario U LEFT JOIN COMPRA C ON U.user_ID = C.user_ID WHERE C.user_ID IS NULL")

for i in cursor.fetchall():
    print(i)

connection.close()