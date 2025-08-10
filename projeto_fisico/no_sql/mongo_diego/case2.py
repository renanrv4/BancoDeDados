import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

#Caso 2: Fazendo um documento embutido em outro documento

collection_publicacao = database['post']

collection_publicacao.delete_many({})


lista_posts = [{'conteudo': 'Cs é muito bom!', 'user': {'user_ID': 1,
                                                        'username': 'Francisco Oceano',
                                                        'first_name': 'Diego',
                                                        'last_name': 'Lyra'}},

               {'conteudo': 'Miadel', 'user': {'user_ID': 1,
                                                        'username': 'Francisco Oceano',
                                                        'first_name': 'Diego',
                                                        'last_name': 'Lyra'}},

               {'conteudo': '+400 no keydrop', 'user': {'user_ID': 2,
                                                        'username': 'niceas',
                                                        'first_name': 'Hugo',
                                                        'last_name': 'Niceas'}},

               {'conteudo': 'Especial liberado!','user': {'user_ID': 3,
                                                        'username': 'Balaio',
                                                        'first_name': 'Gabriel',
                                                        'last_name': 'Moraes'}},

               {'conteudo': 'Luís divulgou promoção.', 'user': {'user_ID': 4,
                                                                'username': 'luis_erf',
                                                                'first_name': 'Luís Eduardo',
                                                                'last_name': 'Ribeiro'}},

               {'conteudo': 'Joab postou um novo guia', 'user': {'user_ID': 5,
                                                                'username': 'joab',
                                                                'first_name': 'Joab',
                                                                'last_name': 'Silva'}},

               {'conteudo': 'Renan entrou no grupo IDK_Servidores!', 'user': {'user_ID': 3,
                                                                                'username': 'rsc8',
                                                                                'first_name': 'Renan',
                                                                                'last_name': 'Santana'}}]


lista_posts_insert = collection_publicacao.insert_many(lista_posts)


#Consulta: Ver todos as publicações do usuário Francisco Oceano


posts_francisco = collection_publicacao.find({'user.username': 'Francisco Oceano'})

for post in posts_francisco:

    print(post['_id'], ": ", post['conteudo'])
