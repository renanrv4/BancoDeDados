import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_compra = database['compra']
collection_promo = database['promocao']

# Limpar a coleção
collection_compra.delete_many({})
collection_promo.delete_many({})

# Mapeamento do caso 1 (um documento referenciando apenas um documento) para o relacionamento compra/promocao

lista_promos = [
    {
        'nome': 'Ano novo 2025',
        'data_inicio': '26/12/2024',
        'data_final': '8/1/2025'
    },
    {
        'nome': 'Promoção de verão 2025',
        'data_inicio': '26/6/2025',
        'data_final': '10/7/2025'
    },
    {
        'nome': 'Promoção de Outono 2024',
        'data_inicio': '25/11/2024',
        'data_final': '1/12/2024'
    },
]

lista_promos_insert = collection_promo.insert_many(lista_promos)
lista_promos_ids = lista_promos_insert.inserted_ids

lista_compras = [
    {
        'nota_fiscal' : '1234', 
        'data' : '1/1/2025',
        'promo_id' : lista_promos_ids[0]
    },
    {
        'nota_fiscal' : '1235',
        'data' : '8/1/2025',
        'promo_id' : lista_promos_ids[0]
    },
    {
        'nota_fiscal' : '1236',
        'data' : '30/11/2024',
        'promo_id' : lista_promos_ids[2]
    },
    {
        'nota_fiscal' : '1237',
        'data' : '1/12/2024',
        'promo_id' : lista_promos_ids[2]
    },
    {
        'nota_fiscal' : '1238',
        'data' : '26/6/2025',
        'promo_id' : lista_promos_ids[1]
    },
    {
        'nota_fiscal' : '1239',
        'data' : '27/6/2025',
        'promo_id' : lista_promos_ids[1]
    },
    {
        'nota_fiscal' : '4321',
        'data' : '28/6/2025',
        'promo_id' : lista_promos_ids[1]
    },
    {
        'nota_fiscal' : '1111',
        'data' : '29/6/2025',
        'promo_id' : lista_promos_ids[1]
    }
]

lista_compras_insert = collection_compra.insert_many(lista_compras)

# Consulta para o caso 1 -> Projetar as NFs das compras feitas no Ano Novo

documento_ano_novo = collection_promo.find_one({'nome': 'Ano novo 2025'})
ano_novo_id = documento_ano_novo['_id']

compras_ano_novo = collection_compra.find({'promo_id': ano_novo_id})

for compra in compras_ano_novo:
    print(compra['nota_fiscal'])