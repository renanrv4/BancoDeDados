import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

cursor.execute("""
INSERT INTO Jogo (jogo_ID, preco, nome)
VALUES ('182828', 35, 'AQW')
""")

connection.commit()

connection.close()