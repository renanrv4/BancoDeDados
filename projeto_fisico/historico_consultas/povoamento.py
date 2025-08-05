import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

cursor.execute("""
INSERT INTO Usuario (user_ID, username, First_name, Last_name)
VALUES
('1', 'Francisco Oceano', 'Diego', 'Lyra'),
('2', 'niceas', 'Hugo', 'Nicéas'),
('3', 'Moraes', 'Gabriel', 'Moraes'),
('4', 'luis_erf', 'Luís Eduardo', 'Ribeiro'),
('5', 'joab', 'Joab', 'Silva'),
('6', 'rsc8', 'Renan', 'Santana'),
('7', 'dist_games', 'Distri', 'Games'),
('8', 'mega_pub', 'Mega', 'Publisher'),
('9', 'dev_studio', 'Dev', 'Studio'),
('10', 'indie_maker', 'Indie', 'Maker'),
('11', 'valve', 'Valve', 'Corporation'),
('12', 'eletronic_arts', 'Eletronic', 'Arts');

""")

cursor.execute("""
INSERT INTO Cargo (cargo_ID, nivel_de_hierarquia, Nome)
VALUES
('1', '1', 'Administrador'),
('2', '2', 'Membro');
""")

cursor.execute("""
INSERT INTO Grupo (grupo_ID, Nome)
VALUES
('1', 'IDK Servidores'),
('2', 'Gamers BR');
""")

cursor.execute("""
INSERT INTO UCG (grupo_ID, user_ID, cargo_ID)
VALUES
('1', '2', '1'),
('1', '1', '2'),
('1', '3', '2'),
('1', '4', '2'),
('2', '1', '1'),
('2', '3', '1'),
('2', '5', '2'),
('2', '6', '2');
""")

cursor.execute("""
INSERT INTO Segue (seguidor_ID, seguido_ID, data_inicio, valido)
VALUES
('1', '2', '2025-01-10', 1),
('1', '2', '2025-02-01', 0),
('1', '2', '2025-03-01', 1),
('3', '4', '2025-01-15', 1),
('5', '2', '2025-01-20', 1),
('6', '1', '2025-01-25', 1);
""")

cursor.execute("""
INSERT INTO Cartao_credito (cartao_ID, user_ID)
VALUES
('1', '1'),
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('6', '6');
""")

cursor.execute("""
INSERT INTO Distribuidor (user_ID, distribuidor)
VALUES
('7', 'Distrib1'),
('8', 'Distrib2'),
('11', 'Valve'),
('12', 'Eletronic Arts');
""")

cursor.execute("""
INSERT INTO Desenvolvedor (user_ID, desenvolvedor)
VALUES
('9', 'Dev1'),
('10', 'Dev2'),
('11', 'Valve'),
('12', 'Eletronic Arts');
""")

cursor.execute("""
INSERT INTO Jogo (jogo_ID, preco, nome, distribuidor_ID, desenvolvedor_ID)
VALUES
('1', 0.00, 'Counter-Strike 2', '11', '11'),
('2', 0.00, 'Dota 2', '11', '11'),
('3', 79.90, 'Dead by Daylight', '8', '10'),
('4', 29.90, 'Balatro', '8', '10'),
('5', 300.00, 'EA SPORTS FC 25', '12', '12');
""")

cursor.execute("""
INSERT INTO Evento (evento_ID, nome, data_inicio)
VALUES
('1', 'Halloween', '2025-10-31'),
('2', 'Natal', '2025-12-25');
""")

cursor.execute("""
INSERT INTO Item (item_ID, nome, float, evento_ID)
VALUES
('1', 'Adagas Sombrias | Teia-Rubra', 0.00025, '1'),
('2', 'AWP | Sabedoria do Dragão', 0.00015, '2'),
('3', 'Atrocidade Obsidiana', 0.00050, '1');
""")

cursor.execute("""
INSERT INTO Inventario (user_ID, publico)
VALUES
('1', 1),
('2', 1),
('3', 0),
('4', 1),
('5', 0),
('6', 1);
""")

cursor.execute("""
INSERT INTO Possui (item_ID, user_ID)
VALUES
('1', '1'),
('2', '2'),
('3', '3');
""")

cursor.execute("""
INSERT INTO Promocao (promocao_ID, promocao, data_inicio, data_final, nome)
VALUES
('1', 0.50, '2025-11-25', '2025-11-30', 'Black Friday'),
('2', 0.30, '2025-06-20', '2025-06-27', 'Summer Sale');
""")

cursor.execute("""
INSERT INTO Compra (user_ID, jogo_ID, promocao_ID, data_compra, nota_fiscal)
VALUES
('1', '3', '1', '2025-11-26', 'NF12345'),
('2', '1', '2', '2025-06-21', 'NF12346'),
('3', '4', NULL, '2025-07-01', 'NF12347'),
('4', '2', '2', '2025-06-22', 'NF12348');
""")

cursor.execute("""
INSERT INTO Servidor (endereco, ativo, jogo_ID)
VALUES
('1', 1, '1'),
('2', 1, '2'),
('3', 0, '3');
""")

cursor.execute("""
INSERT INTO Postagem (user_ID, num_postagem, conteudo)
VALUES
('1', 1, 'CS é muito bom!'),
('2', 1, 'Nice compartilhou uma dica de jogo.'),
('3', 1, 'Gabriel criou um guia de estratégia.'),
('4', 1, 'Luís divulgou promoção.'),
('5', 1, 'Joab comentou sobre um patch novo.');
""")


connection.commit()

connection.close()