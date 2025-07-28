import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

# Ordenar os jogos do desenvolvedor1 do mais caro pro mais barato

cursor.execute("""

    SELECT J.nome, J.preco
    FROM Jogo J, (SELECT *
                FROM Desenvolve
                WHERE developer_ID = 'desenvolvedor1') G
    WHERE J.jogo_ID = G.game_ID
    ORDER BY J.preco DESC

""")

for i in cursor.fetchall(): 
    print(i)

connection.close()