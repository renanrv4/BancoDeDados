import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_evento = database['evento']
collection_item = database['item']

# Limpar as coleções
collection_evento.delete_many({})
collection_item.delete_many({})

# Mapeamento do caso 1 (um documento referenciando apenas um documento)

lista_eventos = [
    {'nome': 'Major CS2 2025', 'evento_ID': 1, 'duracao': 7},
    {'nome': 'Minecraft Hunger Games', 'evento_ID': 2, 'duracao': 5},
    {'nome': 'Habbo Party', 'evento_ID': 3, 'duracao': 14},
    {'nome': 'CinJogue Nessa Aventura', 'evento_ID': 4, 'duracao': 3}
]

eventos_insert = collection_evento.insert_many(lista_eventos)
eventos_ids = eventos_insert.inserted_ids

# Lista de itens que participam dos eventos
lista_itens = [
    {'item_ID': 1, 'nome': 'AK-47 | Redline', 'float': 0.15, 'evento_ID': eventos_ids[0]},
    {'item_ID': 2, 'nome': 'AWP | Dragon Lore', 'float': 0.05, 'evento_ID': eventos_ids[0]},
    {'item_ID': 3, 'nome': 'Ender Pearl', 'float': 0.8, 'evento_ID': eventos_ids[1]},
    {'item_ID': 4, 'nome': 'Diamond Sword', 'float': 0.1, 'evento_ID': eventos_ids[1]},
    {'item_ID': 5, 'nome': 'HC', 'float': 0.5, 'evento_ID': eventos_ids[2]},
    {'item_ID': 6, 'nome': 'CA', 'float': 0.9, 'evento_ID': eventos_ids[2]},
    {'item_ID': 7, 'nome': 'CinJogue AlgumaCoisa', 'float': 0.01, 'evento_ID': eventos_ids[3]}
]

collection_item.insert_many(lista_itens)

# Consulta: IDs e nomes dos itens que participam do evento "Habbo Party"

documento = collection_evento.find_one({'nome': 'Habbo Party'})
evento_id = documento['_id']

itens_evento = collection_item.find({'evento_ID': evento_id})

print("Itens que participam do Habbo Party:")
for item in itens_evento:
    print(item['item_ID'], "-", item['nome'])
