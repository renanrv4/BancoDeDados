import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_promo = database['promocao']


# Limpar a coleção
collection_promo.delete_many({})

# Mapeamento do caso 4 (um documento embutindo vários documentos) para o relacionamento compra/promocao
# Como aqui os servidores não são documentos de classe maior, o mongo não associa a eles um id
lista_promos = [
    {
        'nome': 'Ano novo 2025',
        'data_inicio': '26/12/2024',
        'data_final': '8/1/2025',
        'compras': [
            {
                'compra_ID' : 1,
                'nota_fiscal' : '1234', 
                'data' : '1/1/2025',
            },
            {
                'compra_ID' : 2,
                'nota_fiscal' : '1235',
                'data' : '8/1/2025'
            }]
    },
    {
        'nome': 'Promoção de verão 2025',
        'data_inicio': '26/6/2025',
        'data_final': '10/7/2025',
        'compras': [
            {
                'compra_ID' : 3,
                'nota_fiscal' : '1238',
                'data' : '26/6/2025'
            },
            {
                'compra_ID' : 4,
                'nota_fiscal' : '1239',
                'data' : '27/6/2025'
            },
            {
                'compra_ID' : 5,
                'nota_fiscal' : '4321',
                'data' : '28/6/2025',
            },
            {
                'compra_ID' : 6,
                'nota_fiscal' : '1111',
                'data' : '29/6/2025',
            }]
    },
    {
        'nome': 'Promoção de Outono 2024',
        'data_inicio': '25/11/2024',
        'data_final': '1/12/2024',
        'compras': [
            {
                'compra_ID' : 7,
                'nota_fiscal' : '1236',
                'data' : '30/11/2024',
            },
            {
                'compra_ID' : 8,
                'nota_fiscal' : '1237',
                'data' : '1/12/2024',
            }]
    }
]

## 

lista_promos_insert = collection_promo.insert_many(lista_promos)

# Consulta para o caso 4 -> Projetar as NFs das compras feitas no Ano Novo

documento_ano_novo = collection_promo.find_one({'nome': 'Ano novo 2025'})

compras = documento_ano_novo['compras']

id_list = []
for compra in compras:
    print(compra['nota_fiscal'])