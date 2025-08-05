import sqlite3

connection = sqlite3.connect("steam.db")
cursor = connection.cursor()

# projeta os nomes e os preços dos jogos com o preço abaixo da média

cursor.execute("""
    SELECT J.nome, J.preco
    FROM Jogo J
    WHERE J.preco < (SELECT AVG(preco) FROM Jogo)
 """)

for i in cursor.fetchall():
    print(i)

connection.close()
