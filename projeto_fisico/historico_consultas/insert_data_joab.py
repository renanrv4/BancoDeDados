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

# Inserações por Joab para Anti-Join:

# Jogos
cursor.execute("INSERT INTO Jogo (jogo_ID, preco, nome) VALUES ('001', 50.00, 'SQL Surfers')")
cursor.execute("INSERT INTO Jogo (jogo_ID, preco, nome) VALUES ('002', 35.00, 'Nathan Racing')")
cursor.execute("INSERT INTO Jogo (jogo_ID, preco, nome) VALUES ('003', 40.00, 'Tabira Wars')")
cursor.execute("INSERT INTO Jogo (jogo_ID, preco, nome) VALUES ('004', 20.00, 'Piaui World')")

# Usuários
cursor.execute("INSERT INTO Usuario (user_ID, username, First_name, Last_name) VALUES ('00001', 'robinho', 'Robson', 'Fidalgo')")
cursor.execute("INSERT INTO Usuario (user_ID, username, First_name, Last_name) VALUES ('00002', 'nathanzinho', 'Nathan', 'AlgumaCoisa')")

# Compras
cursor.execute("INSERT INTO Compra (user_ID, jogo_ID, promocao, data_compra, nota_fiscal) VALUES ('00001', '001', NULL, '2006-04-29', 'NF12345')")
cursor.execute("INSERT INTO Compra (user_ID, jogo_ID, promocao, data_compra, nota_fiscal) VALUES ('00002', '002', NULL, '2003-02-24', 'NF67890')")


connection.commit()

connection.close()