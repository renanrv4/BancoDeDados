import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

# Cenário 4 com desenvolvedores e jogos

# Um documento embutindo vários documentos

collection_desenvolvedor = database['desenvolvedor']
collection_jogo = database['jogo']

# Limpar a coleção
collection_desenvolvedor.delete_many({})
collection_jogo.delete_many({})

# Inserindo desenvolvedores com os jogos associados
lista_desenvolvedores = [
    {
        'user_ID': '1', 
        'nome': 'Renan',
        'jogos': 
            [
                {'jogo_ID': '1', 'nome': 'Hades', 'preco': 99.90},
                {'jogo_ID': '7', 'nome': 'The Binding of Isaac', 'preco': 9.90}
            ]
    },
    {
        'user_ID': '2', 
        'nome': 'Luis',
        'jogos': 
            [
                {'jogo_ID': '2', 'nome': 'Terraria', 'preco': 59.90},
                {'jogo_ID': '10', 'nome': 'Ori and the Will of the Wisps', 'preco': 49.90}
            ]
    },
    {
        'user_ID': '3', 
        'nome': 'Joab',
        'jogos': 
            [
                {'jogo_ID': '3', 'nome': 'Hollow Knight', 'preco': 29.90},
                {'jogo_ID': '11', 'nome': 'Celeste 2', 'preco': 19.90}
            ]
    },
    {
        'user_ID': '4', 
        'nome': 'Gabriel',
        'jogos': 
            [
                {'jogo_ID': '4', 'nome': 'Dead Cells', 'preco': 19.90},
                {'jogo_ID': '8', 'nome': 'Stardew Valley', 'preco': 29.99}
            ]
    },
    {
        'user_ID': '5', 
        'nome': 'Hugo',
        'jogos': 
            [
                {'jogo_ID': '5', 'nome': 'Cuphead', 'preco': 49.90},
                {'jogo_ID': '9', 'nome': 'Hollow Knight: Silksong', 'preco': 39.90}
            ]
    },
    {
        'user_ID': '6', 
        'nome': 'Diego',
        'jogos': 
            [
                {'jogo_ID': '6', 'nome': 'Celeste', 'preco': 39.90},
                {'jogo_ID': '12', 'nome': 'Cuphead: The Delicious Last Course', 'preco': 19.90}
            ]
    }
]

collection_desenvolvedor.insert_many(lista_desenvolvedores)

todos_jogos = []
for dev in lista_desenvolvedores:
    for jogo in dev['jogos']:
        todos_jogos.append(jogo)
collection_jogo.insert_many(todos_jogos)

# Consulta: nomes dos jogos de um desenvolvedor específico
for jogo in lista_desenvolvedores[1]['jogos']:
    documento_jogo = collection_jogo.find_one(
        {'jogo_ID': jogo['jogo_ID']},
        {'_id': 0, 'nome': 1}
    )
    print(documento_jogo)