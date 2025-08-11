
import pymongo

# Conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['steam_db']

# Coleções
collection_distribuidor = database['distribuidor']
collection_jogo = database['jogo']

# Limpar as coleções
collection_distribuidor.delete_many({})
collection_jogo.delete_many({})

# Inserir jogos primeiro
lista_jogos = [
    {'nome': 'CS2', 'preco': 86.50},
    {'nome': 'Paladins', 'preco': 0.00},
    {'nome': 'Dead By Daylight', 'preco': 60.00},
    {'nome': 'Left 4 Dead 2', 'preco': 15.30},
    {'nome': 'Realm Royale', 'preco': 0.00}
]

# Inserir jogos e obter seus IDs
resultado_jogos = collection_jogo.insert_many(lista_jogos)
jogos_ids = resultado_jogos.inserted_ids

# Inserir distribuidores com referências aos jogos
lista_distribuidores = [
    {
        'user_ID': '1',
        'jogos': [jogos_ids[0], jogos_ids[3]]  # CS2 e Left 4 Dead 2
    },
    {
        'user_ID': '2',
        'jogos': [jogos_ids[1], jogos_ids[4]]  # Paladins e Realm Royale
    },
    {
        'user_ID': '3',
        'jogos': [jogos_ids[2]]  # Dead By Daylight
    }
]

collection_distribuidor.insert_many(lista_distribuidores)

# Consulta: encontrar os jogos distribuidos por 'Valve'SSSS
for distribuidor in collection_distribuidor.find({'user_ID': '1'}):
    for jogo_id in distribuidor['jogos']:
        jogo = collection_jogo.find_one({'_id': jogo_id})
        if jogo:
            print(jogo)