import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

# Cenário 3 com desenvolvedores e jogos

# Um documento com um array de referências para documentos

collection_desenvolvedor = database['desenvolvedor']
collection_jogo = database['jogo']

# Limpar a coleção
collection_desenvolvedor.delete_many({})
collection_jogo.delete_many({})

# Inserindo jogos
lista_jogos = [
    {'jogo_ID': '1', 'nome': 'Hades', 'preco': 99.90},
    {'jogo_ID': '2', 'nome': 'Terraria', 'preco': 59.90},
    {'jogo_ID': '3', 'nome': 'Hollow Knight', 'preco': 29.90},
    {'jogo_ID': '4', 'nome': 'Dead Cells', 'preco': 19.90},
    {'jogo_ID': '5', 'nome': 'Cuphead', 'preco': 49.90},
    {'jogo_ID': '6', 'nome': 'Celeste', 'preco': 39.90},
    {'jogo_ID': '7', 'nome': 'The Binding of Isaac', 'preco': 9.90},
    {'jogo_ID': '8', 'nome': 'Stardew Valley', 'preco': 29.99}
]

lista_jogos_insert = collection_jogo.insert_many(lista_jogos)
lista_jogos_ids = lista_jogos_insert.inserted_ids

# Inserindo desenvolvedores com os jogos associados
lista_desenvolvedores = [
    {
        'user_ID': '1', 
        'nome': 'Renan',
        'jogos': 
            [
                lista_jogos_ids[0], 
                lista_jogos_ids[6]
            ]
    },
    {
        'user_ID': '2', 
        'nome': 'Luis',
        'jogos': 
            [
                lista_jogos_ids[1]
            ]
    },
    {
        'user_ID': '3', 
        'nome': 'Joab',
        'jogos': 
            [
                lista_jogos_ids[2]
            ]
    },
    {
        'user_ID': '4', 
        'nome': 'Gabriel',
        'jogos': 
            [
                lista_jogos_ids[3],
                lista_jogos_ids[7]
            ]
    },
    {
        'user_ID': '5', 
        'nome': 'Hugo',
        'jogos': 
            [
                lista_jogos_ids[4]
            ]
    },
    {
        'user_ID': '6', 
        'nome': 'Diego',
        'jogos': 
            [
                lista_jogos_ids[5]
            ]
    }
]

collection_desenvolvedor.insert_many(lista_desenvolvedores)

# Consulta: nomes dos jogos de um desenvolvedor específico
id_jogos = lista_desenvolvedores[1]['jogos']
for id in id_jogos:
    documento_jogo = collection_jogo.find_one({'_id': id}, {'_id': 0, 'nome': 1})
    print(documento_jogo)
