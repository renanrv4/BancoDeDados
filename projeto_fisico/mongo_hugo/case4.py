import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_jogo = database['jogo']


# Limpar a coleção
collection_jogo.delete_many({})

# Mapeamento do caso 4 (um documento embutindo vários documentos) para o relacionamento Jogo/Servidor
# Como aqui os servidores não são documentos de classe maior, o mongo não associa a eles um id
lista_jogos = [
    {'nome': 'CS2',
     'preço': 86,
     'servidores': [{'servidor_ID': 1,'ativo' : True},
                    {'servidor_ID': 2,'ativo' : False},
                    {'servidor_ID': 3,'ativo' : True}]},
    {'nome' : 'Paladins',
     'preço': 0,
     'servidores': [{'servidor_ID': 4,'ativo' : True},
                    {'servidor_ID': 5,'ativo' : True}]},
    {'nome': 'Dead By Daylight',
     'preço': 60,
     'servidores': [{'servidor_ID': 6,'ativo' : True},
                    {'servidor_ID': 7,'ativo' : True},
                    {'servidor_ID': 8,'ativo' : False},
                    {'servidor_ID': 9,'ativo' : False},
                    {'servidor_ID': 10,'ativo' : False}]}
]

## 

lista_jogos_insert = collection_jogo.insert_many(lista_jogos)

# Consulta para o caso 4 -> Projetar os ids dos servidores do jogo cujo nome é "Dead By Daylight"

documento_dbd = collection_jogo.find_one({'nome': 'Dead By Daylight'})

servidores = documento_dbd['servidores']

id_list = []
for servidor in servidores:
    id_list.append(servidor['servidor_ID'])

print (id_list)