import sqlite3

connection = sqlite3.connect('steam.db')
cursor = connection.cursor()

# Retorna todos os usuários que nunca fizeram uma compra

cursor.execute("SELECT U.username FROM Usuario U LEFT JOIN COMPRA C ON U.user_ID = C.user_ID WHERE C.user_ID IS NULL AND U.user_ID NOT IN (SELECT user_ID FROM Distribuidor) AND U.user_ID NOT IN (SELECT user_ID FROM Desenvolvedor)")

for i in cursor.fetchall():
    print(i)

connection.close()