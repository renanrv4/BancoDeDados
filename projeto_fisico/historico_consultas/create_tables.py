import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE Grupo(
    grupo_ID VARCHAR(8) PRIMARY KEY,
    Nome VARCHAR(40) NOT NULL
);
""")

#View pra contar o atributo derivado
cursor.execute("""

CREATE VIEW Grupo_View AS
    SELECT G.grupo_ID as grupo_ID, G.Nome as Nome, 
                    (SELECT COUNT(*) as num_membros
                    FROM UCG
                    WHERE grupo_ID = G.grupo_ID)
           AS Num_membros
    FROM Grupo G

#""")

cursor.execute("""
CREATE TABLE Cargo(
    cargo_ID VARCHAR(8) PRIMARY KEY,
    nivel_de_hierarquia VARCHAR(10) NOT NULL,
    Nome VARCHAR(40) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Usuario(
    user_ID VARCHAR(10) PRIMARY KEY,
    username VARCHAR(40) NOT NULL,
    First_name VARCHAR(20) NOT NULL,
    Last_name VARCHAR(20) NOT NULL,
);
""")

#Checar como funcionaria amizade bidirecional
#cursor.execute("""
#CREATE TABLE Amizade(
    
#            user1_ID VARCHAR(10),
#            user2_ID VARCHAR(10),
#            data_inicio DATE NOT NULL,
#            valido BOOLEAN,
#          CONSTRAINT Amizade_PK PRIMARY KEY (user1_ID, user2_ID, data_inicio),
#           CONSTRAINT user1_FK FOREIGN KEY (user1_ID) REFERENCES Usuario (user_ID),
#           CONSTRAINT user2_FK FOREIGN KEY (user2_ID) REFERENCES Usuario (user_ID)
#              
#              );


#""")


#Opção mais prática: Follow/Unfollow

cursor.execute("""
CREATE TABLE Segue(
    
            seguidor_ID VARCHAR(10),
            seguido_ID VARCHAR(10),
            data_inicio DATE NOT NULL,
            valido BOOLEAN,
            CONSTRAINT FU_PK PRIMARY KEY (user1_ID, user2_ID, data_inicio),
            CONSTRAINT seguidor_FK FOREIGN KEY (user1_ID) REFERENCES Usuario (user_ID),
            CONSTRAINT seguido_FK FOREIGN KEY (user2_ID) REFERENCES Usuario (user_ID)
              
              );


""")

cursor.execute("""
CREATE TABLE Cartao_credito(
    cartao_ID VARCHAR(10), 
    user_ID VARCHAR(10),
    CONSTRAINT CC_PK PRIMARY KEY (cartao_ID, user_ID),
    CONSTRAINT CC_FK FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID)
);
""")

cursor.execute("""
CREATE TABLE Jogo(
    jogo_ID VARCHAR(10) PRIMARY KEY,
    preco NUMERIC(5,2) NOT NULL,
    nome VARCHAR(40) NOT NULL,
    distribuidor_ID VARCHAR(10),
    desenvolvedor_ID VARCHAR(10),
               
    CONSTRAINT DISTRIBUIDOR_FK FOREIGN KEY (distribuidor_ID) REFERENCES Distribuidor (user_ID),
    CONSTRAINT DESENVOLVEDOR_FK FOREIGN KEY (desenvolvedor_ID) REFERENCES Desenvolvedor (user_ID)
               
    
);
""")

#Ver se o item fazer parte de um evento é notnull
cursor.execute("""
CREATE TABLE Item(
    item_ID VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    float NUMERIC(7, 5) NOT NULL,
    evento_ID VARCHAR(8), 
               
    CONSTRAINT FK_EVENTO FOREIGN KEY (evento_ID) REFERENCES Evento (evento_ID)
    
);
""")

cursor.execute("""
CREATE TABLE Inventario(
    user_ID VARCHAR(10) PRIMARY KEY,
    publico BOOLEAN NOT NULL,
    CONSTRAINT FK_I FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID)
);
""")

cursor.execute("""
CREATE TABLE Promocao(
    promocao NUMERIC(2, 2) PRIMARY KEY,
    data_inicio DATE,
    data_final DATE,
    nome VARCHAR(20) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Compra(
    user_ID VARCHAR(10),
    jogo_ID VARCHAR(10),
    promocao NUMERIC(2, 2) UNIQUE,
    data_compra DATE,
    nota_fiscal VARCHAR(8) NOT NULL,
    CONSTRAINT PK_COMPRA PRIMARY KEY(user_ID, jogo_ID),
    CONSTRAINT FK_USER FOREIGN KEY (user_ID) REFERENCES Usuario(user_ID),
    CONSTRAINT FK_JOGO FOREIGN KEY (jogo_ID) REFERENCES Jogo(jogo_ID),
    CONSTRAINT FK_PROMO FOREIGN KEY (promocao) REFERENCES Promocao(promocao)
);
""")

cursor.execute("""
CREATE TABLE Distribuidor(
    user_ID VARCHAR(10) PRIMARY KEY,
    distribuidor VARCHAR(8) NOT NULL,
    CONSTRAINT FK_DIST FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID)
);
""")

cursor.execute("""
CREATE TABLE Desenvolvedor(
    user_ID VARCHAR(10) PRIMARY KEY,
    desenvolvedor VARCHAR(8) NOT NULL,
    CONSTRAINT FK_USER FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID)
);
""")



cursor.execute("""
CREATE TABLE Possui(
    item_ID VARCHAR(10),
    user_ID VARCHAR(10),
    CONSTRAINT PF_POSS PRIMARY KEY (item_ID, user_ID),
    CONSTRAINT FK_ITEM FOREIGN KEY (item_ID) REFERENCES Item (item_ID),
    CONSTRAINT FK_USER FOREIGN KEY (user_ID) REFERENCES Inventario (user_ID)
);
""")

cursor.execute("""
CREATE TABLE UCG(
    grupo_ID VARCHAR(8),
    user_ID VARCHAR(10),
    cargo_ID VARCHAR(8),
    CONSTRAINT PK_UCG PRIMARY KEY (grupo_ID, user_ID),
    CONSTRAINT FK_GRUPO FOREIGN KEY (grupo_ID) REFERENCES Grupo (grupo_ID),
    CONSTRAINT FK_USER FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID),
    CONSTRAINT FK_CARGO FOREIGN KEY (cargo_ID) REFERENCES Cargo (cargo_ID)
);
""")

cursor.execute("""

    CREATE TABLE Evento(
        
        evento_ID VARCHAR(8) PRIMARY KEY,
        nome VARCHAR(30),
        data_inicio DATE
        );

""")

cursor.execute("""
    CREATE TABLE Servidor(
        endereco VARCHAR(10) PRIMARY KEY,
        ativo BOOLEAN NOT NULL,
        jogo_ID VARCHAR(10),
               
        CONSTRAINT FK_JOGO FOREIGN KEY (jogo_ID) REFERENCES Jogo (jogo_ID)
               
        
        );
""")

cursor.execute("""

    CREATE TABLE Postagem(
    user_ID VARCHAR(10),
    num_postagem NUMBER,
    conteudo VARCHAR(100),
    
    CONSTRAINT PK_POST PRIMARY KEY (user_ID, disc_post),
    CONSTRAINT FK_POST FOREIGN KEY (user_id) REFERENCES Usuario (user_ID)
    );



""")



connection.close()