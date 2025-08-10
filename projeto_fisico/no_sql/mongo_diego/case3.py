import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_user = database['user']
collection_publicacao = database['post']

#Caso 3: Fazendo um documento guardar um array de referências

collection_user.delete_many({})
collection_publicacao.delete_many({})

lista_posts_diego = [{'conteudo': 'Cs é muito bom!'},
                            {'conteudo': 'Miadel'}]

lista_posts_diego_insert = collection_publicacao.insert_many(lista_posts_diego)
lista_posts_diego_id = lista_posts_diego_insert.inserted_ids

user_diego = {'username': 'Francisco Oceano',
                    'first_name': 'Diego',
                    'last_name': 'Lyra',
                    'posts': lista_posts_diego_id
                   }

lista_posts_hugo = [{'conteudo': '+400 no keydrop'}]

lista_posts_hugo_insert = collection_publicacao.insert_many(lista_posts_hugo)
lista_posts_hugo_id = lista_posts_hugo_insert.inserted_ids

user_hugo = {'username': 'niceas',
                    'first_name': 'Hugo',
                    'last_name': 'Nicéas',
                    'posts': lista_posts_hugo_id
                   }

lista_posts_gabriel = [{'conteudo': 'Especial liberado!'}]

lista_posts_gabriel_insert = collection_publicacao.insert_many(lista_posts_gabriel)
lista_posts_gabriel_id = lista_posts_gabriel_insert.inserted_ids

user_gabriel = {'username': 'Balaio',
                    'first_name': 'Gabriel',
                    'last_name': 'Moraes',
                    'posts': lista_posts_gabriel_id
                   }


lista_posts_luis = [{'conteudo': 'Luís divulgou promoção.'}]

lista_posts_luis_insert = collection_publicacao.insert_many(lista_posts_luis)

lista_posts_luis_id = lista_posts_luis_insert.inserted_ids

user_luis = {'username': 'luis_erf',
                    'first_name': 'Luís Eduardo',
                    'last_name': 'Ribeiro',
                    'posts': lista_posts_luis_id
                   }


lista_posts_joab = [{'conteudo': 'Joab postou um novo guia'}]

lista_posts_joab_insert = collection_publicacao.insert_many(lista_posts_joab)
lista_posts_joab_id = lista_posts_joab_insert.inserted_ids

user_joab = {'username': 'joab',
                    'first_name': 'Joab',
                    'last_name': 'Silva',
                    'posts': lista_posts_joab_id
                   }

lista_posts_renan = [{'conteudo': 'Renan entrou no grupo IDK_Servidores!'}]

lista_posts_renan_insert = collection_publicacao.insert_many(lista_posts_renan)
lista_posts_renan_id = lista_posts_renan_insert.inserted_ids

user_renan = {'username': 'rsc8',
                    'first_name': 'Renan',
                    'last_name': 'Santana',
                    'posts': lista_posts_renan_id
                   }

user_insert = collection_user.insert_many([user_diego, user_hugo, user_gabriel, user_luis, user_joab, user_renan])

doc_francisco = collection_user.find_one({'username': 'Francisco Oceano'})

id_publicacoes = doc_francisco['posts']

for id in id_publicacoes:

    post = collection_publicacao.find_one({'_id': id})
    print(id, ": ", post['conteudo'])
