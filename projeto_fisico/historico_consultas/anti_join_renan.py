import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

# Retorna jogos sem correspondência de usuários, ou seja, jogos que não foram comprados
cursor.execute("""
    SELECT e.evento_ID, e.nome FROM Evento e WHERE NOT EXISTS (SELECT 1 FROM Item i WHERE e.evento_ID = i.evento_ID)
""")

for jogo in cursor.fetchall():
    print(jogo)

connection.close()