import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_distribuidor = database['distribuidor']
collection_jogo = database['jogo']

# Limpar coleções
collection_distribuidor.delete_many({})
collection_jogo.delete_many({})

# Inserir distribuidores (user_ID é a chave que será usada no relacionamento)
lista_distribuidores = [
    {'user_ID': 1, 'nome': 'Valve'},
    {'user_ID': 2, 'nome': 'Hi-Rez Studios'},
    {'user_ID': 3, 'nome': 'Behaviour Interactive'}
]

collection_distribuidor.insert_many(lista_distribuidores)

# Inserir jogos referenciando o user_ID do distribuidor
lista_jogos = [
    {'nome': 'CS2', 'preco': 86.50, 'distribuidor_user_ID': 1},
    {'nome': 'Paladins', 'preco': 0.00, 'distribuidor_user_ID': 2},
    {'nome': 'Dead By Daylight', 'preco': 60.00, 'distribuidor_user_ID': 3},
    {'nome': 'Left 4 Dead 2', 'preco': 15.30, 'distribuidor_user_ID': 1},
    {'nome': 'Realm Royale', 'preco': 0.00, 'distribuidor_user_ID': 2}
]

collection_jogo.insert_many(lista_jogos)

# Consulta: pegar todos os jogos distribuídos pela "Valve"
distribuidor_valve = collection_distribuidor.find_one({'nome': 'Valve'})
valve_user_id = distribuidor_valve['user_ID']  # pegando o user_ID, não o _id

jogos_valve = collection_jogo.find({'distribuidor_user_ID': valve_user_id})

print("Jogos distribuídos pela Valve:")
for jogo in jogos_valve:
    print(jogo['nome'])
