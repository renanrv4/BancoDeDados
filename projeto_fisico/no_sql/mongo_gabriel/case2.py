import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_compra = database['compra']

# Limpar a coleção
collection_compra.delete_many({})

# Mapeamento do caso 2 (um documento embutindo apenas um documentoo) para o relacionamento compra/promocao
# Como os jogos não são documentos de ordem superior, os ids serão artificiais
lista_compras = [
    {
        'nota_fiscal' : '1234', 
        'data' : '1/1/2025',
        'promocao' : 
        {
            'promo_ID' : 1,
            'nome': 'Ano novo 2025',
            'data_inicio': '26/12/2024',
            'data_final': '8/1/2025'
        }
    },
    {
        'nota_fiscal' : '1235',
        'data' : '8/1/2025',
        'promocao' : 
        {
            'promo_ID' : 1,
            'nome': 'Ano novo 2025',
            'data_inicio': '26/12/2024',
            'data_final': '8/1/2025'
        }
    },
    {
        'nota_fiscal' : '1236',
        'data' : '30/11/2024',
        'promo_id' : 
        {
            'nome': 'Promoção de Outono 2024',
            'data_inicio': '25/11/2024',
            'data_final': '1/12/2024'
        }
    },
    {
        'nota_fiscal' : '1237',
        'data' : '1/12/2024',
        'promocao' : 
        {
            'nome': 'Promoção de Outono 2024',
            'data_inicio': '25/11/2024',
            'data_final': '1/12/2024'
        }
    },
    {
        'nota_fiscal' : '1238',
        'data' : '26/6/2025',
        'promocao' : 
        {
            'nome': 'Promoção de Verão 2025',
            'data_inicio': '26/6/2025',
            'data_final': '10/7/2025'
        }
    },
    {
        'nota_fiscal' : '1239',
        'data' : '27/6/2025',
        'promocao' : 
        {
            'nome': 'Promoção de Verão 2025',
            'data_inicio': '26/6/2025',
            'data_final': '10/7/2025'
        }
    },
    {
        'nota_fiscal' : '4321',
        'data' : '28/6/2025',
        'promocao' : 
        {
            'nome': 'Promoção de Verão 2025',
            'data_inicio': '26/6/2025',
            'data_final': '10/7/2025'
        }
    },
    {
        'nota_fiscal' : '1111',
        'data' : '29/6/2025',
        'promocao' : 
        {
            'nome': 'Promoção de Verão 2025',
            'data_inicio': '26/6/2025',
            'data_final': '10/7/2025'
        }
    },
]

lista_compras_insert = collection_compra.insert_many(lista_compras)

# Consulta para o caso 2 -> Projetar as NFs das compras feitas no Ano Novo

nfs_ano_novo = collection_compra.find({'promocao.nome': 'Ano novo 2025'})

for nf in nfs_ano_novo:
    print(nf['nota_fiscal'])