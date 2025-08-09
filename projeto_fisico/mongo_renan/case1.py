import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

# Cenário 1 com desenvolvedores e jogos

# Um documento referenciando apenas um documento

collection_desenvolvedor = database['desenvolvedor']
collection_jogo = database['jogo']

# Limpar a coleção
collection_desenvolvedor.delete_many({})
collection_jogo.delete_many({})

# Inserir desenvolvedores
lista_desenvolvedores = [
    {'user_ID': '1', 'nome': 'Renan'},
    {'user_ID': '2', 'nome': 'Luis'},
    {'user_ID': '3', 'nome': 'Joab'},
    {'user_ID': '4', 'nome': 'Gabriel'},
    {'user_ID': '5', 'nome': 'Hugo'},
    {'user_ID': '6', 'nome': 'Diego'}
]

lista_desenvolvedores_insert = collection_desenvolvedor.insert_many(lista_desenvolvedores)
lista_desenvolvedores_ids = lista_desenvolvedores_insert.inserted_ids

# Inserindo jogos
lista_jogos = [
    {'jogo_ID': '1', 'nome': 'Hades', 'preco': 99.90, 'desenvolvedor_id': lista_desenvolvedores_ids[0]},
    {'jogo_ID': '2', 'nome': 'Terraria', 'preco': 59.90, 'desenvolvedor_id': lista_desenvolvedores_ids[1]},
    {'jogo_ID': '3', 'nome': 'Hollow Knight', 'preco': 29.90, 'desenvolvedor_id': lista_desenvolvedores_ids[0]},
    {'jogo_ID': '4', 'nome': 'Dead Cells', 'preco': 19.90, 'desenvolvedor_id': lista_desenvolvedores_ids[2]},
    {'jogo_ID': '5', 'nome': 'Cuphead', 'preco': 49.90, 'desenvolvedor_id': lista_desenvolvedores_ids[3]}
]

lista_jogos_insert = collection_jogo.insert_many(lista_jogos)

# Consulta: nomes dos jogos de um desenvolvedor específico
dev_id = lista_desenvolvedores_ids[0]
resultado = collection_jogo.find({'desenvolvedor_id': dev_id}, {'_id': 0, 'nome': 1})
for doc in resultado:
    print(doc)
