--iniciação das tabelas se não existirem virão aqui, mas antes disso vamos diagramar tudo
CREATE TABLE IF NOT EXISTS Pessoa(
 cpf VARCHAR(11) PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 sexo CHAR(1) NOT NULL,
 idade INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Cargo(
    id SERIAL PRIMARY KEY,
    cargo VARCHAR(100) UNIQUE NOT NULL,
    posicao INT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Policial(
    id SERIAL PRIMARY KEY,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    admin BOOL NOT NULL,
    senha TEXT UNIQUE NOT NULL,
    cargo_id INT,
    FOREIGN KEY (cpf) REFERENCES Pessoa(cpf),
    FOREIGN KEY (cargo_id) REFERENCES Cargo(id)
);

CREATE TABLE IF NOT EXISTS Area(
    id SERIAL PRIMARY KEY,
    cep varchar(8) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Zona(
    id SERIAL PRIMARY KEY,
    nome varchar(50) UNIQUE NOT NULL,
    area_id int,
    FOREIGN KEY (area_id) REFERENCES Area(id)
);

CREATE TABLE IF NOT EXISTS Equipe(
    id SERIAL PRIMARY KEY,
    zona_id int,
    policial_id int,
    FOREIGN KEY (zona_id) REFERENCES Zona(id),
    FOREIGN KEY (policial_id) REFERENCES Policial(id)
);

CREATE TABLE IF NOT EXISTS Acesso_equipe(
    id SERIAL PRIMARY KEY,
    equipe_id int,
    policial_id int,
    FOREIGN KEY (equipe_id) REFERENCES Equipe(id),
    FOREIGN KEY (policial_id) REFERENCES Policial(id)
);

CREATE TABLE IF NOT EXISTS Setor(
    id SERIAL PRIMARY KEY,
    nome varchar(50)
);

CREATE TABLE IF NOT EXISTS Acesso_setor(
    id SERIAL PRIMARY KEY,
    setor_id int,
    policial_id int,
    FOREIGN KEY (setor_id) REFERENCES Setor(id),
    FOREIGN KEY (policial_id) REFERENCES Policial(id)
);

CREATE TABLE IF NOT EXISTS Falta(
    id SERIAL PRIMARY KEY,
    policial_id INT,
    created_at TIMESTAMP NOT NULL,
    data_fim DATE,
    justificativa TEXT,
    FOREIGN KEY (policial_id) REFERENCES Policial(id)
);

CREATE TABLE IF NOT EXISTS TipoOcorrencia(
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Estados(
    id SERIAL PRIMARY KEY,
    estado varchar(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Bo(
    id SERIAL PRIMARY KEY,
    created_at DATE NOT NULL,
    updated_at DATE,
    created_by VARCHAR(100) NOT NULL,
    updated_by VARCHAR(100),
    tipo_id INT NOT NULL,
    conteudo TEXT NOT NULL,
    area_id int,
    estado_id INT,
    FOREIGN KEY (created_by) REFERENCES Pessoa(cpf),
    FOREIGN KEY (updated_by) REFERENCES Pessoa(cpf),
    FOREIGN KEY (tipo_id) REFERENCES TipoOcorrencia(id),
    FOREIGN KEY (estado) REFERENCES Estados(id),
    FOREIGN KEY (area_id) REFERENCES Area(id)
);

CREATE TABLE IF NOT EXISTS Ficha(
    id SERIAL PRIMARY KEY,
    cpf varchar(11),
    bo_id int,
    FOREIGN KEY (cpf) REFERENCES Pessoa(cpf),
    FOREIGN KEY (bo_id) REFERENCES bo(id)
);


