import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_distribuidor = database['distribuidor']
collection_jogo = database['jogo']

# Limpar coleções
collection_distribuidor.delete_many({})
collection_jogo.delete_many({})

# Inserindo distribuidores com jogos embutidos (array de documentos)
lista_distribuidores = [
    {
        'user_ID': '1',
        'nome': 'Distribuidora Alpha',
        'jogos': [
            {'jogo_ID': '1', 'nome': 'CS2', 'preco': 86.50},
            {'jogo_ID': '4', 'nome': 'Left 4 Dead 2', 'preco': 15.30}
        ]
    },
    {
        'user_ID': '2',
        'nome': 'Distribuidora Beta',
        'jogos': [
            {'jogo_ID': '2', 'nome': 'Paladins', 'preco': 0.00},
            {'jogo_ID': '5', 'nome': 'Realm Royale', 'preco': 0.00}
        ]
    },
    {
        'user_ID': '3',
        'nome': 'Distribuidora Gamma',
        'jogos': [
            {'jogo_ID': '3', 'nome': 'Dead By Daylight', 'preco': 60.00}
        ]
    }
]

collection_distribuidor.insert_many(lista_distribuidores)

# Extrair todos os jogos dos distribuidores para inserir na coleção de jogos
todos_jogos = []
for dist in lista_distribuidores:
    for jogo in dist['jogos']:
        todos_jogos.append(jogo)

collection_jogo.insert_many(todos_jogos)

# Consulta: nomes dos jogos de um distribuidor específico (exemplo: Distribuidora Beta)
for jogo in lista_distribuidores[1]['jogos']:  # índice 1 = Distribuidora Beta
    documento_jogo = collection_jogo.find_one(
        {'jogo_ID': jogo['jogo_ID']},
        {'_id': 0, 'nome': 1}
    )
    print(documento_jogo)
