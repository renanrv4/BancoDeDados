import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_promo = database['promocao']
collection_compra = database['compra']


# Limpar a coleção
collection_promo.delete_many({})
collection_compra.delete_many({})

# Mapeamento do caso 3 (um documento com um array de referências para documentos) para o relacionamento Jogo/Servidor
# Como aqui os servidores são um documento de ordem maior, o mongo associa a eles um id
lista_compras_ano_novo = [
    {
        'nota_fiscal' : '1234',
        'data' : '1/1/2025'
    },
    {
        'nota_fiscal' : '1235',
        'data' : '8/1/2025'
    },]

lista_compras_ano_novo_insert = collection_compra.insert_many(lista_compras_ano_novo)
compras_ano_novo_id = lista_compras_ano_novo_insert.inserted_ids

promo_ano_novo = {
    'nome': 'Ano novo 2025',
    'data_inicio' : '26/12/2024',
    'data_final' : '8/1/2025',
    'compras': compras_ano_novo_id
}

lista_compras_verao =  [
    {
        'nota_fiscal' : '1238',
        'data' : '26/6/2025'
    },
    {
        'nota_fiscal' : '1239',
        'data' : '27/6/2025'
    },
    {
        'nota_fiscal' : '4321',
        'data' : '28/6/2025'
    },
    {
        'nota_fiscal' : '1111',
        'data' : '29/6/2025'
    }
]

lista_compras_verao_insert = collection_compra.insert_many(lista_compras_verao)
compras_verao_id = lista_compras_verao_insert.inserted_ids

promo_verao = {
    'nome': 'Promoção de verão 2025',
    'data_inicio': '26/6/2025',
    'data_final': '10/7/2025',
    'compras': compras_verao_id
}

lista_compras_outono = [
    {
        'nota_fiscal' : '1236',
        'data' : '30/11/2024'
    },
    {
        'nota_fiscal' : '1237',
        'data' : '1/12/2024'
    },
]

lista_compras_outono_insert = collection_compra.insert_many(lista_compras_outono)
compras_outono_id = lista_compras_outono_insert.inserted_ids

promo_outono = {
    'nome': 'Promoção de Outono 2024',
    'data_inicio': '25/11/2024',
    'data_final': '1/12/2024',
    'compras': compras_outono_id
}

jogos_insert = collection_promo.insert_many([promo_ano_novo,promo_verao,promo_outono])

# Consulta para o caso 3 -> Projetar as NFs das compras feitas no Ano Novo

documento_ano_novo = collection_promo.find_one({'nome': 'Ano novo 2025'})

id_compras = documento_ano_novo['compras']

for id in id_compras:
    documento_compra = collection_compra.find_one({'_id' : id})
    print(documento_compra['nota_fiscal'])