import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

# Retorna os usuários que pertencem ao mesmo grupo e tem o mesmo cargo que 'Joab'
cursor.execute("""
    SELECT user_ID, grupo_ID, cargo_ID FROM UCG WHERE (grupo_ID, cargo_ID) = (
        SELECT grupo_ID, cargo_ID FROM UCG WHERE user_ID = 'Joab')
""")

for jogo in cursor.fetchall():
    print(jogo)

connection.close()