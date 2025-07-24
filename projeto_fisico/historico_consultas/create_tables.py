import sqlite3

connection = sqlite3.connect('steam.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE Grupo(
    grupo_ID VARCHAR(8) PRIMARY KEY,
    Num_membros VARCHAR(3) NOT NULL,
    Nome VARCHAR(40) NOT NULL
);
""")

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
    amigo_ID VARCHAR(10),
    disc_amigo VARCHAR(8) UNIQUE,
    CONSTRAINT FK_AMIGO FOREIGN KEY (amigo_ID) REFERENCES Usuario (user_ID)
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
    nome VARCHAR(40) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Item(
    item_ID VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    decim NUMERIC(7, 5) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Inventario(
    user_ID VARCHAR(10) PRIMARY KEY,
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
    user_ID VARCHAR(8) PRIMARY KEY,
    CONSTRAINT FK_USER FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID)
);
""")

cursor.execute("""
CREATE TABLE Desenvolve(
    developer_ID VARCHAR(8),
    game_ID VARCHAR(10),
    CONSTRAINT PK_DEV PRIMARY KEY (developer_ID, game_ID),
    CONSTRAINT FK_DEV_ID FOREIGN KEY (developer_ID) REFERENCES Desenvolvedor (user_ID),
    CONSTRAINT FK_GAME FOREIGN KEY (game_ID) REFERENCES Jogo(jogo_ID)
);
""")

cursor.execute("""
CREATE TABLE Distribui(
    distribuidor_ID VARCHAR(8),
    game_ID VARCHAR(10),
    CONSTRAINT PK_DIST PRIMARY KEY (distribuidor_ID, game_ID),
    CONSTRAINT FK_DIST_ID FOREIGN KEY (distribuidor_ID) REFERENCES Distribuidor (user_ID),
    CONSTRAINT FK_GAME FOREIGN KEY (game_ID) REFERENCES Jogo(jogo_ID)
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
    cargo_ID VARCHAR(8) UNIQUE,
    CONSTRAINT PK_UCG PRIMARY KEY (grupo_ID, user_ID),
    CONSTRAINT FK_GRUPO FOREIGN KEY (grupo_ID) REFERENCES Grupo (grupo_ID),
    CONSTRAINT FK_USER FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID),
    CONSTRAINT FK_CARGO FOREIGN KEY (cargo_ID) REFERENCES Cargo (cargo_ID)
);
""")

connection.close()