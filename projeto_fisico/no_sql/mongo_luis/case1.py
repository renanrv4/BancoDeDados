import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_distribuidor = database['distribuidor']
collection_jogo = database['jogo']

# Limpar coleções
collection_distribuidor.delete_many({})
collection_jogo.delete_many({})

lista_distribuidores = [
    {'user_ID': 1},
    {'user_ID': 2},
    {'user_ID': 3}
]

collection_distribuidor.insert_many(lista_distribuidores)

lista_jogos = [
    {'nome': 'CS2', 'preco': 86.50, 'distribuidor_user_ID': 1},
    {'nome': 'Paladins', 'preco': 0.00, 'distribuidor_user_ID': 2},
    {'nome': 'Dead By Daylight', 'preco': 60.00, 'distribuidor_user_ID': 3},
    {'nome': 'Left 4 Dead 2', 'preco': 15.30, 'distribuidor_user_ID': 1},
    {'nome': 'Realm Royale', 'preco': 0.00, 'distribuidor_user_ID': 2}
]

collection_jogo.insert_many(lista_jogos)

# Consulta: encontrar os jogos distribuídos pelo distribuidor com user_ID 1
distribuidor_ID = collection_distribuidor.find_one({'user_ID': 1})  

jogos_distribuidor = collection_jogo.find({'distribuidor_user_ID': distribuidor_ID['user_ID']})

for jogo in jogos_distribuidor:
    print(jogo['nome'])
