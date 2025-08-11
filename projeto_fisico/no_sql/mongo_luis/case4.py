import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_distribuidor = database['distribuidor']

# Limpar coleções
collection_distribuidor.delete_many({})

# Mapeamento do caso 4 (um documento embutindo vários documentos) para o relacionamento Jogo/Servidor
lista_distribuidores = [
    {
        'user_ID': '1',
        'jogos': [
            {'jogo_ID': '1', 'nome': 'CS2', 'preco': 86.50},
            {'jogo_ID': '4', 'nome': 'Left 4 Dead 2', 'preco': 15.30}
        ]
    },
    {
        'user_ID': '2',
        'jogos': [
            {'jogo_ID': '2', 'nome': 'Paladins', 'preco': 0.00},
            {'jogo_ID': '5', 'nome': 'Realm Royale', 'preco': 0.00}
        ]
    },
    {
        'user_ID': '3',
        'jogos': [
            {'jogo_ID': '3', 'nome': 'Dead By Daylight', 'preco': 60.00}
        ]
    }
]

collection_distribuidor.insert_many(lista_distribuidores)

# Consulta: nomes dos jogos de um distribuidor específico
distribuidor = collection_distribuidor.find_one({'user_ID': '1'})

lista_jogos = distribuidor['jogos']
for jogo in lista_jogos:
    print(jogo)
