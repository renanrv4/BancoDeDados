import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

# Cenário 2 com desenvolvedores e jogos

# Um documento embutindo apenas um documento

collection_desenvolvedor = database['desenvolvedor']
collection_jogo = database['jogo']

# Limpar a coleção
collection_desenvolvedor.delete_many({})
collection_jogo.delete_many({})

# Inserindo jogos
lista_jogos = [
    {'jogo_ID': '1', 'nome': 'Hades', 'preco': 99.90, 'desenvolvedor': {'user_ID': '1', 'nome': 'Renan'}},
    {'jogo_ID': '2', 'nome': 'Terraria', 'preco': 59.90, 'desenvolvedor': {'user_ID': '2', 'nome': 'Luis'}},
    {'jogo_ID': '3', 'nome': 'Hollow Knight', 'preco': 29.90, 'desenvolvedor': {'user_ID': '3', 'nome': 'Hugo'}},
    {'jogo_ID': '4', 'nome': 'Dead Cells', 'preco': 19.90, 'desenvolvedor': {'user_ID': '4', 'nome': 'Joab'}},
    {'jogo_ID': '5', 'nome': 'Cuphead', 'preco': 49.90, 'desenvolvedor': {'user_ID': '5', 'nome': 'Diego'}},
    {'jogo_ID': '6', 'nome': 'Celeste', 'preco': 39.90, 'desenvolvedor': {'user_ID': '6', 'nome': 'Gabriel'}},
    {'jogo_ID': '7', 'nome': 'The Binding of Isaac', 'preco': 9.90, 'desenvolvedor': {'user_ID': '1', 'nome': 'Renan'}}
]

lista_jogos_insert = collection_jogo.insert_many(lista_jogos)



# Consulta: nomes dos jogos e preços de cada jogo do desenvolvedor 'Renan'
resultado = collection_jogo.find({'desenvolvedor.nome': 'Renan'}, {'_id': 0, 'nome': 1, 'preco': 1})
for doc in resultado:
    print(doc)
