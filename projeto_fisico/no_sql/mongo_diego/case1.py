import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_user = database['user']
collection_publicacao = database['post']

#Relacionamento: Usuário - Publicação
#Caso 1: Um documento referenciando apenas um documento

collection_user.delete_many({})
collection_publicacao.delete_many({})

lista_usuarios = [{'username': 'Francisco Oceano',
                    'first_name': 'Diego',
                    'last_name': 'Lyra'
                   },
                   {'username': 'niceas',
                    'first_name': 'Hugo',
                    'last_name': 'Nicéas'
                   },
                   {'username': 'Balaio',
                    'first_name': 'Gabriel',
                    'last_name': 'Moraes'
                   },
                   {'username': 'luis_erf',
                    'first_name': 'Luís Eduardo',
                    'last_name': 'Ribeiro'
                   },
                   {'username': 'joab',
                    'first_name': 'Joab',
                    'last_name': 'Silva'
                   },
                   {'username': 'rsc8',
                    'first_name': 'Renan',
                    'last_name': 'Santana'
                   }]

lista_usuarios_insert = collection_user.insert_many(lista_usuarios)

lista_usuarios_ids = lista_usuarios_insert.inserted_ids

lista_posts = [{'conteudo': 'Cs é muito bom!', 'user_ID': lista_usuarios_ids[0]},
               {'conteudo': 'Miadel', 'user_ID': lista_usuarios_ids[0]},
               {'conteudo': '+400 no keydrop', 'user_ID': lista_usuarios_ids[1]},
               {'conteudo': 'Especial liberado!', 'user_ID': lista_usuarios_ids[2]},
               {'conteudo': 'Luís divulgou promoção.', 'user_ID': lista_usuarios_ids[3]},
               {'conteudo': 'Joab postou um novo guia', 'user_ID': lista_usuarios_ids[4]},
               {'conteudo': 'Renan entrou no grupo IDK_Servidores!', 'user_ID': lista_usuarios_ids[5]}]

lista_posts_insert = collection_publicacao.insert_many(lista_posts)


#Consulta: Ver todas as publicações de Francisco Oceano

documento_francisco = collection_user.find_one({'username': 'Francisco Oceano'})
francisco_id = documento_francisco['_id']

posts_francisco = collection_publicacao.find({'user_ID': francisco_id})

for post in posts_francisco:
    print(post['_id'], ": ", post['conteudo'])
