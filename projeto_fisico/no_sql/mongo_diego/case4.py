import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_user = database['user']

#Caso 4: Vários documentos embuitidos em um documento

collection_user.delete_many({})

lista_usuarios = [{'username': 'Francisco Oceano',
                    'first_name': 'Diego',
                    'last_name': 'Lyra',
                    'posts': [{'ordem': 1, 'conteudo': 'Cs é muito bom!'}, {'ordem': 2, 'conteudo': 'Miadel'}]
                   },
                   {'username': 'niceas',
                    'first_name': 'Hugo',
                    'last_name': 'Nicéas',
                    'posts': [{'ordem': 1, 'conteudo': '+400 no keydrop'}]
                   },
                   {'username': 'Balaio',
                    'first_name': 'Gabriel',
                    'last_name': 'Moraes',
                    'posts': [{'ordem': 1, 'conteudo': 'Especial liberado!'}]
                   },
                   {'username': 'luis_erf',
                    'first_name': 'Luís Eduardo',
                    'last_name': 'Ribeiro',
                    'posts': [{'ordem': 1, 'conteudo': 'Luís divulgou promoção.'}]
                   },
                   {'username': 'joab',
                    'first_name': 'Joab',
                    'last_name': 'Silva',
                    'posts': [{'ordem': 1, 'conteudo': 'Joab postou um novo guia'}]
                   },
                   {'username': 'rsc8',
                    'first_name': 'Renan',
                    'last_name': 'Santana',
                    'posts': [{'ordem': 1, 'conteudo': 'Renan entrou no grupo IDK_Servidores!'}]
                   }]


lista_usuarios_insert = collection_user.insert_many(lista_usuarios)


documento_francisco = collection_user.find_one({'username': 'Francisco Oceano'})

posts = documento_francisco['posts']
for post in posts:

    print(post['ordem'], ": ", post['conteudo'])

