import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_jogo = database['jogo']
collection_servidor = database['servidor']

# Limpar a coleção
collection_jogo.delete_many({})
collection_servidor.delete_many({})

# Mapeamento do caso 1 (um documento referenciando apenas um documento) para o relacionamento jogo/servidor

lista_jogos = [
    {'nome': 'CS2',
     'preço': 86},
    {'nome' : 'Paladins',
     'preço': 0},
    {'nome': 'Dead By Daylight',
     'preço': 60}
]

lista_jogos_insert = collection_jogo.insert_many(lista_jogos)
lista_jogos_ids = lista_jogos_insert.inserted_ids

lista_servidores = [
    {'ativo' : True, 'jogo_ID': lista_jogos_ids[0]},
    {'ativo' : False, 'jogo_ID': lista_jogos_ids[0]},
    {'ativo' : True, 'jogo_ID': lista_jogos_ids[0]},
    {'ativo' : True, 'jogo_ID': lista_jogos_ids[1]},
    {'ativo' : True, 'jogo_ID': lista_jogos_ids[1]},
    {'ativo' : True, 'jogo_ID': lista_jogos_ids[2]},
    {'ativo' : True, 'jogo_ID': lista_jogos_ids[2]},
    {'ativo' : False, 'jogo_ID': lista_jogos_ids[2]},
    {'ativo' : False, 'jogo_ID': lista_jogos_ids[2]},
    {'ativo' : False, 'jogo_ID': lista_jogos_ids[2]}
]

lista_servidores_insert = collection_servidor.insert_many(lista_servidores)

# Consulta para o caso 1 -> Projetar os ids dos servidores do jogo cujo nome é "Dead By Daylight"

documento_dbd = collection_jogo.find_one({'nome': 'Dead By Daylight'})
dbd_id = documento_dbd['_id']

servidores_dbd = collection_servidor.find({'jogo_ID': dbd_id})

for servidor in servidores_dbd:
    print(servidor['_id'])