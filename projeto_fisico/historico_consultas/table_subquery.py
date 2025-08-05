import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

# Listar todos os usuários que possuem itens que participam de eventos

cursor.execute("""

    SELECT username
    FROM Usuario U JOIN (SELECT * 
                        FROM Possui P JOIN Item I
                        ON I.item_ID = P.item_ID AND I.evento_ID IS NOT NULL) PI 
               
    ON U.user_ID = PI.user_ID

""")

for i in cursor.fetchall(): 
    print(i)

connection.close()