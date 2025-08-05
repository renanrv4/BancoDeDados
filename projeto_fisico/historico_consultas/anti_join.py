import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

# Retorna jogos sem correspondência de usuários, ou seja, jogos que não foram comprados
cursor.execute("""
    SELECT j.jogo_ID, j.nome FROM Jogo j WHERE NOT EXISTS (SELECT * FROM Compra c WHERE c.jogo_ID = j.jogo_ID)
""")

for jogo in cursor.fetchall():
    print(jogo)

connection.close()