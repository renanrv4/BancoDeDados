import sqlite3

dict_consulta = {
    '1': 'Usuario',
    '2': 'Jogo',
    '3': 'Item',
    '4': 'Evento',
    '5': 'Promocao',
    '6': 'Grupo',
    '7': 'Cargo',
    '8': 'Desenvolvedor',
    '9': 'Distribuidor',
    '10': 'Postagem',
    '11': 'Inventario',
    '12': 'Compra',
    '13': 'UCG',
    '14': 'Servidor',
    '15': 'Possui',
    '16': 'Segue',
    '17': 'Cartao_credito'
}

connection = sqlite3.connect('steam.db')
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

def insert_usuario(user_id, username, first_name, last_name):
    cursor.execute("INSERT INTO Usuario (user_ID, username, First_name, Last_name) VALUES (?, ?, ?, ?)",
                   (user_id, username, first_name, last_name))

def insert_jogo(jogo_id, preco, nome, distribuidor_id, desenvolvedor_id):
    cursor.execute("INSERT INTO Jogo (jogo_ID, preco, nome, distribuidor_ID, desenvolvedor_ID) VALUES (?, ?, ?, ?, ?)",
                   (jogo_id, preco, nome, distribuidor_id, desenvolvedor_id))

def insert_item(item_id, nome, float, evento_id):
    cursor.execute("INSERT INTO Item (item_ID, nome, float, evento_ID) VALUES (?, ?, ?, ?)",
                   (item_id, nome, float, evento_id))

def insert_evento(evento_id, nome, data_inicio):
    cursor.execute("INSERT INTO Evento (evento_ID, nome, data_inicio) VALUES (?, ?, ?)",
                   (evento_id, nome, data_inicio))

def insert_promocao(promocao_id, data_inicio, data_final, nome):
    cursor.execute("INSERT INTO Promocao (promocao_ID, data_inicio, data_final, nome) VALUES (?, ?, ?, ?)",
                   (promocao_id, data_inicio, data_final, nome))

def insert_grupo(grupo_id, nome):
    cursor.execute("INSERT INTO Grupo (grupo_ID, Nome) VALUES (?, ?)", (grupo_id, nome))

def insert_cargo(cargo_id, nivel_hierarquia, nome):
    cursor.execute("INSERT INTO Cargo (cargo_ID, nivel_de_hierarquia, Nome) VALUES (?, ?, ?)",
                   (cargo_id, nivel_hierarquia, nome))

def insert_desenvolvedor(user_id):
    cursor.execute("INSERT INTO Desenvolvedor (user_ID) VALUES (?)", (user_id,))

def insert_distribuidor(user_id):
    cursor.execute("INSERT INTO Distribuidor (user_ID) VALUES (?)", (user_id,))

def insert_postagem(user_id, num_postagem, conteudo):
    cursor.execute("INSERT INTO Postagem (user_ID, num_postagem, conteudo) VALUES (?, ?, ?)",
                   (user_id, num_postagem, conteudo))

def insert_inventario(user_id, publico):
    cursor.execute("INSERT INTO Inventario (user_ID, publico) VALUES (?, ?)", (user_id, publico))

def insert_compra(user_id, jogo_id, promocao_id, data_compra, nota_fiscal):
    cursor.execute("INSERT INTO Compra (user_ID, jogo_ID, promocao_ID, data_compra, nota_fiscal) VALUES (?, ?, ?, ?, ?)",
                   (user_id, jogo_id, promocao_id, data_compra, nota_fiscal))

def insert_ucg(grupo_id, user_id, cargo_id):
    cursor.execute("INSERT INTO UCG (grupo_ID, user_ID, cargo_ID) VALUES (?, ?, ?)",
                   (grupo_id, user_id, cargo_id))

def insert_servidor(endereco, ativo, jogo_id):
    cursor.execute("INSERT INTO Servidor (endereco, ativo, jogo_ID) VALUES (?, ?, ?)",
                   (endereco, ativo, jogo_id))

def insert_possui(item_id, user_id):
    cursor.execute("INSERT INTO Possui (item_ID, user_ID) VALUES (?, ?)", (item_id, user_id))

def insert_segue(seguidor_id, seguido_id, data_inicio, valido):
    cursor.execute("INSERT INTO Segue (seguidor_ID, seguido_ID, data_inicio, valido) VALUES (?, ?, ?, ?)",
                   (seguidor_id, seguido_id, data_inicio, valido))
    
while True:
    print('O que você deseja fazer?\n' \
          '1 - Inserir\n' \
          '2 - Consulta\n' \
          '3 - FIM')
    
    comando = input()
    if comando == '1':
        print('Aonde você quer inserir?\n' \
              '1 - Usuário\n' \
              '2 - Jogo\n' \
              '3 - Item\n' \
              '4 - Evento\n' \
              '5 - Promoção\n' \
              '6 - Grupo\n' \
              '7 - Cargo\n' \
              '8 - Desenvolvedor\n' \
              '9 - Distribuidor\n' \
              '10 - Postagem\n'\
              '11 - Inventário\n' \
              '12 - Compra\n' \
              '13 - UCG\n' \
              '14 - Servidor\n' \
              '15 - Possui\n' \
              '16 - Segue')
        tabela = input()
        try:
            if tabela == '1':
                insert_usuario(input('USER ID: '), input('USERNAME: '), input('FIRST NAME: '), input('LAST NAME: '))
            elif tabela == '2':
                insert_jogo(input('JOGO ID: '), float(input('PREÇO: ')), input('NOME: '), input('DISTRIBUIDOR ID: '), input('DESENVOLVEDOR ID: '))
            elif tabela == '3':
                item_id = input('ITEM ID: ')
                insert_item(item_id, input('NOME: '), float(input('FLOAT: ')), input('EVENTO ID (ou deixe vazio): ') or None)
                insert_possui(item_id, input('USER ID (inventário): '))
            elif tabela == '4':
                insert_evento(input('EVENTO ID: '), input('NOME: '), input('DATA DE INÍCIO (YYYY-MM-DD): '))
            elif tabela == '5':
                insert_promocao(input('PROMOÇÃO ID: '), input('DATA INÍCIO (YYYY-MM-DD): '), input('DATA FINAL (YYYY-MM-DD): '), input('NOME: '))
            elif tabela == '6':
                insert_grupo(input('GRUPO ID: '), input('NOME: '))
            elif tabela == '7':
                insert_cargo(input('CARGO ID: '), input('NÍVEL DE HIERARQUIA: '), input('NOME: '))
            elif tabela == '8':
                insert_desenvolvedor(input('USER ID: '))
            elif tabela == '9':
                insert_distribuidor(input('USER ID: '))
            elif tabela == '10':
                insert_postagem(input('USER ID: '), int(input('NÚMERO DA POSTAGEM: ')), input('CONTEÚDO: '))
            elif tabela == '11':
                insert_inventario(input('USER ID: '), input('PÚBLICO (True/False): ') == 'True')
            elif tabela == '12':
                insert_compra(input('USER ID: '), input('JOGO ID: '), input('PROMOÇÃO ID (ou deixe vazio): ') or None,
                            input('DATA DA COMPRA (YYYY-MM-DD): '), input('NOTA FISCAL: '))
            elif tabela == '13':
                insert_ucg(input('GRUPO ID: '), input('USER ID: '), input('CARGO ID: '))
            elif tabela == '14':
                insert_servidor(input('ENDEREÇO: '), input('ATIVO (True/False): ') == 'True', input('JOGO ID: '))
            elif tabela == '15':
                insert_possui(input('ITEM ID: '), input('USER ID (inventário): '))
            elif tabela == '16':
                insert_segue(input('SEGUIDOR ID: '), input('SEGUIDO ID: '), input('DATA DE INÍCIO (YYYY-MM-DD): '),
                            input('VÁLIDO (True/False): ') == 'True')
            else:
                print("Opção inválida!")
            connection.commit()
            print("Inserção realizada com sucesso.")
        except Exception as e:
            print("Erro durante a inserção:", e)

    elif comando == '2':
        print('Aonde você quer consultar?\n' \
              '1 - Usuário\n' \
              '2 - Jogo\n' \
              '3 - Item\n' \
              '4 - Evento\n' \
              '5 - Promoção\n' \
              '6 - Grupo\n' \
              '7 - Cargo\n' \
              '8 - Desenvolvedor\n' \
              '9 - Distribuidor\n' \
              '10 - Postagem\n' \
              '11 - Inventário\n' \
              '12 - Compra\n' \
              '13 - UCG\n' \
              '14 - Servidor\n' \
              '15 - Possui\n' \
              '16 - Segue')
        
        tabela = input()

        cursor.execute(f"""
            SELECT * FROM {dict_consulta[tabela]}
        """)

        for i in cursor.fetchall():
            print(i)

    else:
        print('Tchau!')
        break

connection.close()