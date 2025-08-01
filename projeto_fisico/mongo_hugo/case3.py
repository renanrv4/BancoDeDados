import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_jogo = database['jogo']
collection_servidor = database['servidor']


# Limpar a coleção
collection_jogo.delete_many({})
collection_servidor.delete_many({})

# Mapeamento do caso 3 (um documento com um array de referências para documentos) para o relacionamento Jogo/Servidor
# Como aqui os servidores são um documento de ordem maior, o mongo associa a eles um id, porém ainda colocaremos um identificador artificial
lista_servidores_cs2 = [{'servidor_ID': 1,'ativo' : True},
                    {'servidor_ID': 2,'ativo' : False},
                    {'servidor_ID': 3,'ativo' : True}]

lista_servidores_cs2_insert = collection_servidor.insert_many(lista_servidores_cs2)
servidores_cs2_id = lista_servidores_cs2_insert.inserted_ids

jogo_cs2 = {'nome': 'CS2',
            'preço': 86,
            'servidores': servidores_cs2_id}

lista_servidores_paladins =  [{'servidor_ID': 4,'ativo' : True},
                            {'servidor_ID': 5,'ativo' : True}]

lista_servidores_paladins_insert = collection_servidor.insert_many(lista_servidores_paladins)
servidores_paladins_id = lista_servidores_paladins_insert.inserted_ids

jogo_paladins = {'nome' : 'Paladins',
                'preço': 0,
                'servidores': servidores_paladins_id}

lista_servidores_dbd = [{'servidor_ID': 6,'ativo' : True},
                    {'servidor_ID': 7,'ativo' : True},
                    {'servidor_ID': 8,'ativo' : False},
                    {'servidor_ID': 9,'ativo' : False},
                    {'servidor_ID': 10,'ativo' : False}]

lista_servidores_dbd_insert = collection_servidor.insert_many(lista_servidores_dbd)
servidores_dbd_id = lista_servidores_dbd_insert.inserted_ids

jogo_dbd = {'nome': 'Dead By Daylight',
     'preço': 60,
     'servidores': servidores_dbd_id }

jogos_insert = collection_jogo.insert_many([jogo_cs2,jogo_dbd,jogo_paladins])

# Consulta para o caso 3 -> Projetar os ids artificiais e os status dos servidores do jogo cujo nome é "Dead By Daylight"

documento_dbd = collection_jogo.find_one({'nome': 'Dead By Daylight'})

id_servidores = documento_dbd['servidores']

for id in id_servidores:
    documento_servidor = collection_servidor.find_one({'_id' : id})
    print(f"{documento_servidor['servidor_ID']} : está ativo? -> {documento_servidor['ativo']}")