CREATE TABLE Grupo(
    grupo_ID VARCHAR(8) PRIMARY KEY,
    Num_membros VARCHAR(3) NOT NULL,
    Nome VARCHAR(40) NOT NULL	
)

CREATE TABLE Cargo(
    cargo_ID VARCHAR(8) PRIMARY KEY,
    nivel_de_hierarquia VARCHAR(10) NOT NULL,
    Nome VARCHAR(40) NOT NULL	
)

CREATE TABLE Usuario(
    user_ID VARCHAR(10) PRIMARY KEY,
    username VARCHAR(40) NOT NULL,
    First_name VARCHAR(20) NOT NULL,
    Last_name VARCHAR(20) NOT NULL,
    amigo_ID VARCHAR(10),
    disc_amigo(8) UNIQUE,
    CONSTRAINT FK_AMIGO FOREIGN KEY (amigo_ID) REFERENCES Usuario (user_ID) 
)

CREATE TABLE Cartao_credito(
    user_ID VARCHAR(10) PRIMARY KEY,
    CONSTRAINT CC_FK FOREIGN KEY (user_ID REFERENCES Usuario (user_ID)
)

CREATE TABLE Jogo(
    jogo_ID VARCHAR(10) PRIMARY KEY,
    preco NUMBER(5,2) NOT NULL, 
    nome VARCHAR(40) NOT NULL
)

CREATE TABLE Item(
    item_ID VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    decim NUMBER(2, 5) NOT NULL
)

CREATE TABLE Inventario(
    user_ID VARCHAR(10) PRIMARY KEY,
     CONSTRAINT FK_I FOREIGN KEY (user_ID) REFERENCES Usuario (user_ID)
)

CREATE TABLE Promocao(
    promocao NUMBER(2, 2) PRIMARY KEY,
    data_inicio DATE,
    data_final DATE,
	nome VARCHAR(20) NOT NULL
)

CREATE TABLE Compra(
    user_ID VARCHAR(10),
    jogo_ID VARCHAR(10),
    promocao NUMBER(2, 2) UNIQUE, 
    data_compra DATE,
    nota_fiscal VARCHAR(8) NOT NULL,
        CONSTRAINT PK_COMPRA PRIMARY KEY(user_ID, jogo_ID),
        CONSTRAINT FK_USER FOREING KEY (user_ID) REFERENCES Usuario(user_ID),
        CONSTRAINT FK_JOGO FOREING KEY (jogo_ID) REFERENCES Jogo(jogo_ID),
        CONSTRAINT FK_PROMO FOREING KEY (promocao) REFERENCES Promocao(promocao)
)

CREATE TABLE Distribuidor(
    user_ID VARCHAR(10) PRIMARY KEY,
    distribuidor VARCHAR(8) NOT NULL,
    CONSTRAINT FK_DIST FOREING KEY (user_ID) REFERENCES Usuario (user_ID)
)

CREATE TABLE Desenvolvedor(
    user_ID VARCHAR(8) PRIMARY KEY,
    CONSTRAINT FK_USER FOREING KEY (user_ID) REFERENCES Usuario (user_ID)
)

CREATE TABLE Desenvolve(
    developer_ID VARCHAR(8),
    game_ID VARCHAR(10),
    CONSTRAINT PK_DEV PRIMARY KEY (developer_ID, game_ID),
    CONSTRAINT FK_DEV_ID FOREIGN KEY (developer_ID) REFERENCES Desenvolvedor (user_ID),
    CONSTRAINT FK_GAME FOREING KEY (game_ID) REFERENCES Jogo(jogo_ID)
)

CREATE TABLE Distribui(
    distribuidor_ID VARCHAR(8),
    game_ID VARCHAR(10),
    CONSTRAINT PK_DIST PRIMARY KEY (distribuidor_ID, game_ID),
    CONSTRAINT FK_DIST_ID FOREIGN KEY (distribuidor_ID) REFERENCES Distribuidor (user_ID),
    CONSTRAINT FK_GAME FOREING KEY (game_ID) REFERENCES Jogo(jogo_ID)
)

CREATE TABLE Possui(
    item_ID VARCHAR(10),
    user_ID VARCHAR(10),
    CONSTRAINT PF_POSS PRIMARY KEY (item_ID, user_ID),
    CONSTRAINT FK_ITEM FOREING KEY (item_ID) REFERENCES Item (item_ID),
    CONSTRAINT FK_USER FOREING KEY (user_ID) REFERENCES Inventario (user_ID)
)

CREATE TABLE UCG(
    grupo_ID VARCHAR(8),
    user_ID VARCHAR(10),
    cargo_ID VARCHAR(8) UNIQUE,
    CONSTRAINT PK_UCG PRIMARY KEY (grupo_ID, user_ID),
    CONSTRAINT FK_GRUPO FOREING KEY (grupo_ID) REFERENCES Grupo (grupo_ID),
    CONSTRAINT FK_USER FOREING KEY (user_ID) REFERENCES Usuario (user_ID),
    CONSTRAINT FK_CARGO FOREIGN KEY (cargo_ID) REFERENCES Cargo (cargo_ID)
)