import sqlite3

connection = sqlite3.connect('steam.db')
cursor = connection.cursor()


#Retorna todos os usuarios que fizeram pelo menos uma compra

cursor.execute("""
    SELECT user_ID, username
    FROM Usuario
    WHERE user_ID IN (
        SELECT user_ID
        FROM Compra
    );
""")

for i in cursor.fetchall():
    print(i)

connection.close()