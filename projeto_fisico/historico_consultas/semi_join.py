import sqlite3

connection = sqlite3.connect("steam.db")
cursor = connection.cursor()

# projeta o username de todos os usuários que fazem parte de um grupo

cursor.execute("""
    SELECT U.username
    FROM Usuario U
    WHERE U.user_ID IN (SELECT user_ID
                        FROM UCG)
""")

for i in cursor.fetchall():
    print(i)

connection.close()