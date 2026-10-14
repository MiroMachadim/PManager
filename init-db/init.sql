--iniciação das tabelas se não existirem virão aqui, mas antes disso vamos diagramar tudo
CREATE TABLE IF NOT EXISTS Pessoa(
 cpf VARCHAR(11) PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 sexo CHAR(1) NOT NULL,
 idade INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Cargo(
    id INT SERIAL PRIMARY KEY,
    cargo VARCHAR(100) UNIQUE NOT NULL,
    posicao INT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Policial(
    id INT SERIAL PRIMARY KEY,
    pessoa_cpf VARCHAR(11) UNIQUE NOT NULL,
    senha UUID UNIQUE NOT NULL,
    cargo_id INT,
    equipe_id  INT,
    FOREIGN KEY (pessoa_cpf) REFERENCES Pessoa(cpf),
    FOREIGN KEY (cargo_id) REFERENCES Cargo(id)
    FOREIGN KEY (equipe_id) REFERENCES Equipe(id)
);

CREATE TABLE IF NOT EXISTS Area(
    id INT SERIAL PRIMARY KEY,
    cep varchar(8) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Zona(
    id INT SERIAL PRIMARY KEY,
    nome varchar(50) UNIQUE NOT NULL,
    area_id int,
    FOREIGN KEY (area_id) REFERENCES Area(id),
);

CREATE TABLE IF NOT EXISTS Equipe(
    id INT SERIAL PRIMARY KEY,
    zona_id int,
    lider_id int,
    FOREIGN KEY (zona_id) REFERENCES Zona(id),
    FOREIGN KEY (lider_id) REFERENCES Policial(id)
);

CREATE TABLE IF NOT EXISTS Setor(
    id INT SERIAL PRIMARY KEY,
    nome varchar(50)
);

CREATE TABLE IF NOT EXISTS Acesso_setor(
    id INT SERIAL PRIMARY KEY,
    setor_id int,
    policial_id int,
    FOREIGN KEY (setor_id) REFERENCES Setor(id),
    FOREIGN KEY (policial_id) REFERENCES Policial(id)
)

CREATE TABLE IF NOT EXISTS Falta(
    id INT SERIAL PRIMARY KEY,
    policial_id INT,
    data_envio TIMESTAMP NOT NULL,
    data_fim DATE,
    justificativa TEXT,
    FOREIGN KEY (policial_id) REFERENCES Policial(id)
);

CREATE TABLE IF NOT EXISTS TipoOcorrencia(
    id INT SERIAL PRIMARY KEY,
    tipo VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Estados(
    id INT SERIAL PRIMARY KEY,
    estado varchar(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Bo(
    id INT SERIAL PRIMARY KEY,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,
    Created_by VARCHAR(100),
    Updated_by VARCHAR(100),
    tipo_id INT NOT NULL,
    conteudo TEXT NOT NULL,
    localidade int,
    estado INT,
    FOREIGN KEY (Created_by) REFERENCES Pessoa(cpf),
    FOREIGN KEY (Updated_by) REFERENCES Pessoa(cpf),
    FOREIGN KEY (tipo_id) REFERENCES TipoOcorrencia(id),
    FOREIGN KEY (estado) REFERENCES Estados(id),
    FOREIGN KEY (localidade) REFERENCES Area(id)
);

CREATE TABLE IF NOT EXISTS Ficha(
    id INT SERIAL PRIMARY KEY,
    pessoa_cpf varchar(11),
    bo_pessoa int,
    FOREIGN KEY (pessoa_cpf) REFERENCES Pessoa(cpf),
    FOREIGN KEY (bo_pessoa) REFERENCES bo(id)
);


