import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_item = database['item']

# Limpar a coleção
collection_item.delete_many({})

# Mapeamento do caso 2: documento embutido (cada item tem o evento dos dados embutido no próprio documento)

lista_itens = [
    {'item_ID': 1, 'nome': 'AK-47 | Redline', 'float': 0.15,
     'evento': {
         'evento_ID': 1,
         'nome': 'Major CS2 2025',
         'duracao': 7
     }},

    {'item_ID': 2, 'nome': 'AWP | Dragon Lore', 'float': 0.05,
     'evento': {
         'evento_ID': 1,
         'nome': 'Major CS2 2025',
         'duracao': 7
     }},

    {'item_ID': 3, 'nome': 'Ender Pearl', 'float': 0.8,
     'evento': {
         'evento_ID': 2,
         'nome': 'Minecraft Hunger Games',
         'duracao': 5
     }},

    {'item_ID': 4, 'nome': 'Diamond Sword', 'float': 0.1,
     'evento': {
         'evento_ID': 2,
         'nome': 'Minecraft Hunger Games',
         'duracao': 5
     }},

    {'item_ID': 5, 'nome': 'HC', 'float': 0.5,
     'evento': {
         'evento_ID': 3,
         'nome': 'Habbo Party',
         'duracao': 14
     }},

    {'item_ID': 6, 'nome': 'CA', 'float': 0.9,
     'evento': {
         'evento_ID': 3,
         'nome': 'Habbo Party',
         'duracao': 14
     }},

    {'item_ID': 7, 'nome': 'CinJogue AlgumaCoisa', 'float': 0.01,
     'evento': {
         'evento_ID': 4,
         'nome': 'CinJogue Nessa Aventura',
         'duracao': 3
     }}
]

collection_item.insert_many(lista_itens)

# Consulta: IDs e nomes dos itens que participam do evento "Habbo Party"

itens_evento = collection_item.find({'evento.nome': 'CinJogue Nessa Aventura'})

print("Itens que participam do CinJogue Nessa Aventura:")
for item in itens_evento:
    print(item['item_ID'], "-", item['nome'])
