import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

# Cenário: distribuidor embutido no documento de jogo
collection_distribuidor = database['distribuidor']  # não será usada para armazenar separadamente
collection_jogo = database['jogo']

# Limpar coleções
collection_distribuidor.delete_many({})
collection_jogo.delete_many({})

# Inserir jogos com distribuidor embutido
lista_jogos = [
    {'jogo_ID': '1', 'nome': 'CS2', 'preco': 86.50, 'distribuidor': {'user_ID': '1', 'nome': 'Valve'}},
    {'jogo_ID': '2', 'nome': 'Paladins', 'preco': 0.00, 'distribuidor': {'user_ID': '2', 'nome': 'Hi-Rez Studios'}},
    {'jogo_ID': '3', 'nome': 'Dead By Daylight', 'preco': 60.00, 'distribuidor': {'user_ID': '3', 'nome': 'Behaviour Interactive'}},
    {'jogo_ID': '4', 'nome': 'Left 4 Dead 2', 'preco': 15.30, 'distribuidor': {'user_ID': '1', 'nome': 'Valve'}},
    {'jogo_ID': '5', 'nome': 'Realm Royale', 'preco': 0.00, 'distribuidor': {'user_ID': '2', 'nome': 'Hi-Rez Studios'}}
]

collection_jogo.insert_many(lista_jogos)

# Consulta: nomes e preços de todos os jogos distribuídos pela Valve
resultado = collection_jogo.find(
    {'distribuidor.nome': 'Valve'},
    {'_id': 0, 'nome': 1, 'preco': 1}
)

print("Jogos distribuídos pela Valve:")
for doc in resultado:
    print(doc)
