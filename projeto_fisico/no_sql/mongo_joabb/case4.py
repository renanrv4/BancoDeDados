import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_evento = database['evento']

# Limpa a coleção
collection_evento.delete_many({})

# Caso 4 - Documento com vários documentos embutidos:
# Cada evento armazena uma lista de itens diretamente dentro dele, os itens são documentos embutidos no evento.

lista_eventos = [
    {'nome': 'Major CS2 2025',
     'evento_ID': 1,
     'duracao': 7,
     'itens': [
         {'item_ID': 1, 'nome': 'AK-47 | Redline', 'float': 0.15},
         {'item_ID': 2, 'nome': 'AWP | Dragon Lore', 'float': 0.05},
     ]},

    {'nome': 'Minecraft Hunger Games',
     'evento_ID': 2,
     'duracao': 5,
     'itens': [
         {'item_ID': 3, 'nome': 'Ender Pearl', 'float': 0.8},
         {'item_ID': 4, 'nome': 'Diamond Sword', 'float': 0.1}
     ]},

    {'nome': 'Habbo Party',
     'evento_ID': 3,
     'duracao': 14,
     'itens': [
         {'item_ID': 5, 'nome': 'HC', 'float': 0.5},
         {'item_ID': 6, 'nome': 'CA', 'float': 0.9}
     ]},

    {'nome': 'CinJogue Nessa Aventura',
     'evento_ID': 4,
     'duracao': 3,
     'itens': [
         {'item_ID': 7, 'nome': 'CinJogue AlgumaCoisa', 'float': 0.01}
     ]}
]

# Insere todos os eventos com os itens embutidos de uma vez
collection_evento.insert_many(lista_eventos)

# Consulta: pegar os itens do evento "Major CS2 2025"
documento_mc = collection_evento.find_one({'nome': 'Major CS2 2025'})
itens = documento_mc['itens']

print("Itens que participam do Major CS2 2025:")
for item in itens:
    print(item['item_ID'], "-", item['nome'])
