import sqlite3

connection = sqlite3.connect('steam.db')
cursor = connection.cursor()

# Retorna todas as compras com promoções

cursor.execute("SELECT * FROM Compra C INNER JOIN Promocao P on C.promocao = P.promocao")

for i in cursor.fetchall():
    print(i)

connection.close()