import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_servidor = database['servidor']

# Limpar a coleção
collection_servidor.delete_many({})

# Mapeamento do caso 2 (um documento embutindo apenas um documentoo) para o relacionamento jogo/servidor
# Como os jogos não são documentos de ordem superior, os ids serão artificiais
lista_servidores = [
    {'ativo' : True,
     'jogo': {
         'jogo_ID': 1,
         'nome': 'CS2',
         'preço': 86
     }},
    {'ativo' : False,
     'jogo': {
         'jogo_ID': 1,
         'nome': 'CS2',
         'preço': 86
     }},
    {'ativo' : True,
     'jogo': {
         'jogo_ID': 1,
         'nome': 'CS2',
         'preço': 86
     }},
    {'ativo' : True,
     'jogo': {
         'jogo_ID': 2,
         'nome': 'Paladins',
         'preço': 0
     }},
    {'ativo' : True,
     'jogo': {
         'jogo_ID': 2,
         'nome': 'Paladins',
         'preço': 0
     }},
    {'ativo' : True,
     'jogo': {
         'jogo_ID': 3,
         'nome': 'Dead By Daylight',
         'preço': 60
     }},
    {'ativo' : True,
     'jogo': {
         'jogo_ID': 3,
         'nome': 'Dead By Daylight',
         'preço': 60
     }},
    {'ativo' : False,
     'jogo': {
         'jogo_ID': 3,
         'nome': 'Dead By Daylight',
         'preço': 60
     }},
    {'ativo' : False,
     'jogo': {
         'jogo_ID': 3,
         'nome': 'Dead By Daylight',
         'preço': 60
     }},
    {'ativo' : False,
     'jogo': {
         'jogo_ID': 3,
         'nome': 'Dead By Daylight',
         'preço': 60
     }}
]

lista_servidores_insert = collection_servidor.insert_many(lista_servidores)

# Consulta para o caso 2 -> Projetar os ids dos servidores do jogo cujo nome é "Dead By Daylight"

servidores_dbd = collection_servidor.find({'jogo.nome': 'Dead By Daylight'})

for servidor in servidores_dbd:
    print(servidor['_id'])