import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

# Retorna jogos sem correspondência de usuários, ou seja, jogos que não foram comprados
cursor.execute("""
    SELECT j.jogo_ID, j.nome FROM Jogo j LEFT JOIN Compra c ON j.jogo_ID = c.jogo_ID WHERE c.jogo_ID IS NULL
""")

for jogo in cursor.fetchall():
    print(jogo)

connection.close()