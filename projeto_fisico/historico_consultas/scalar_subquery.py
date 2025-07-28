import sqlite3

connection = sqlite3.connect("steam.db")
cursor = connection.cursor()

# projeta os nomes dos jogos com o preço abaixo da média

cursor.execute("""
    SELECT J.nome
    FROM Jogo J
    WHERE J.preco < (SELECT AVG(preco) FROM Jogo)
 """)
