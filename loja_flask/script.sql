CREATE TABLE Categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    descricao TEXT,
    codigo VARCHAR(100)
);

CREATE TABLE Produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    descricao TEXT,
    preco DECIMAL(10, 2),
    estoque INTEGER,
    foto_url TEXT,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    is_authenticated BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    is_anonymous BOOLEAN DEFAULT FALSE
);

CREATE TABLE Venda (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER,
    data_venda TIMESTAMP,
    produto_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES "User"(id),
    FOREIGN KEY (produto_id) REFERENCES Produto(id)
);

CREATE TABLE ItemVenda (
    id SERIAL PRIMARY KEY,
    venda_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    preco_unitario DECIMAL(10, 2),
    FOREIGN KEY (venda_id) REFERENCES Venda(id),
    FOREIGN KEY (produto_id) REFERENCES Produto(id)
);
