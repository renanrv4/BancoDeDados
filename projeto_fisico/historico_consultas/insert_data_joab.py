import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

cursor.execute("""
INSERT INTO Jogo (jogo_ID, preco, nome)
VALUES ('182828', 35, 'AQW')
""")

# Inserações por Joab para Row SubQuery:

cursor.execute("INSERT INTO UCG (grupo_ID, user_ID, cargo_ID) VALUES ('001', 'Joab', '01')")

cursor.execute("INSERT INTO UCG (grupo_ID, user_ID, cargo_ID) VALUES ('001', 'Renan', '01')")

cursor.execute("INSERT INTO UCG (grupo_ID, user_ID, cargo_ID) VALUES ('001', 'Luis', '02')")

cursor.execute("INSERT INTO UCG (grupo_ID, user_ID, cargo_ID) VALUES ('002', 'Hugo', '01')")

cursor.execute("INSERT INTO UCG (grupo_ID, user_ID, cargo_ID) VALUES ('002', 'Gabriel', '02')")

cursor.execute("INSERT INTO UCG (grupo_ID, user_ID, cargo_ID) VALUES ('002', 'Diego', '02')")

connection.commit()

connection.close()