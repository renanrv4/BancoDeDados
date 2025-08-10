import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['steam_db']

collection_evento = database['evento']
collection_item = database['item']

# Limpa as coleções
collection_evento.delete_many({})
collection_item.delete_many({})

# Mapeamento do caso 3 (documento com um array de referências para documentos)
# Cada evento tem um array de id de itens que participam dele. Cada item é um documento separado.

item_ak47 = {'item_ID': 1, 'nome': 'AK-47 | Redline', 'float': 0.15}
item_awp = {'item_ID': 2, 'nome': 'AWP | Dragon Lore', 'float': 0.05}

item_ender_pearl = {'item_ID': 3, 'nome': 'Ender Pearl', 'float': 0.8}
item_diamond_sword = {'item_ID': 4, 'nome': 'Diamond Sword', 'float': 0.1}

item_hc = {'item_ID': 5, 'nome': 'HC', 'float': 0.5}
item_ca = {'item_ID': 6, 'nome': 'CA', 'float': 0.9}

item_cinjogue = {'item_ID': 7, 'nome': 'CinJogue AlgumaCoisa', 'float': 0.01}

# Abaixo, o insert_one insere um documento e pega seu ID para usar como referência em outros documentos
# isso é necessário pois o documento do evento vai guardar uma lista de referências a IDs dos itens que participam dele

id_ak47 = collection_item.insert_one(item_ak47).inserted_id 
id_awp = collection_item.insert_one(item_awp).inserted_id

id_ender_pearl = collection_item.insert_one(item_ender_pearl).inserted_id
id_diamond_sword = collection_item.insert_one(item_diamond_sword).inserted_id

id_hc = collection_item.insert_one(item_hc).inserted_id
id_ca = collection_item.insert_one(item_ca).inserted_id

id_cinjogue = collection_item.insert_one(item_cinjogue).inserted_id

# Eventos separados, cada um referenciando os itens pelo _id
evento_ak = {
    'nome': 'Major CS2 2025',
    'evento_ID': 1,
    'duracao': 7,
    'itens': [id_ak47, id_awp]
}

evento_mc = {
    'nome': 'Minecraft Hunger Games',
    'evento_ID': 2,
    'duracao': 5,
    'itens': [id_ender_pearl, id_diamond_sword]
}

evento_habbo = {
    'nome': 'Habbo Party',
    'evento_ID': 3,
    'duracao': 14,
    'itens': [id_hc, id_ca]
}

evento_cinjogue = {
    'nome': 'CinJogue Nessa Aventura',
    'evento_ID': 4,
    'duracao': 3,
    'itens': [id_cinjogue]
}

collection_evento.insert_many([evento_ak, evento_mc, evento_habbo, evento_cinjogue])

# Consulta: itens do evento "Minecraft Hunger Games"

evento_mc_db = collection_evento.find_one({'nome': 'Minecraft Hunger Games'})
ids_itens_evento = evento_mc_db['itens']

print("Itens que participam do Minecraft Hunger Games:")
for item_id in ids_itens_evento:
    item = collection_item.find_one({'_id': item_id})
    print(item['item_ID'], "-", item['nome'])
