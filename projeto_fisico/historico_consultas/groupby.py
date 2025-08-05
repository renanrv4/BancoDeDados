import sqlite3

connection = sqlite3.connect('steam.db')
cursor = connection.cursor()

# Retorna todos os grupos que tem mais de um administrador

cursor.execute("""
    SELECT Nome
        FROM Grupo G JOIN (SELECT grupo_ID AS GID, COUNT(*)
                    FROM (SELECT *
                        FROM UCG
                        WHERE cargo_ID = '1')
                    GROUP BY grupo_ID
                    HAVING COUNT(*) > 1)
        ON G.grupo_ID = GID

""")

for i in cursor.fetchall():
    print(i)

connection.close()