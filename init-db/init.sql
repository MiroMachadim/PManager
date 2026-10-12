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
    pessoa_cpf VARCHAR(11),
    cargo_id INT,
    FOREIGN KEY (pessoa_cpf) REFERENCES Pessoa(cpf),
    FOREIGN KEY (cargo_id) REFERENCES Cargo(id)
);

CREATE TABLE IF NOT EXISTS Falta(
    id INT SERIAL PRIMARY KEY,
    policial_id INT,
    data_envio TIMESTAMP NOT NULL,
    data_fim DATE,
    justificativa TEXT
);
CREATE TABLE IF NOT EXISTS TipoOcorrencia(
    id INT SERIAL PRIMARY KEY,
    tipo VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS bo(
    id INT SERIAL PRIMARY KEY,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,
    Created_by VARCHAR(100),
    Updated_by VARCHAR(100),
    tipo_id INT NOT NULL,
    conteudo TEXT NOT NULL,
    resolvido BOOLEAN NOT NULL,
    FOREIGN KEY (Created_by) REFERENCES Pessoa(cpf),
    FOREIGN KEY (Updated_by) REFERENCES Pessoa(cpf),
    FOREIGN KEY (tipo_id) REFERENCES TipoOcorrencia(id)
);
CREATE TABLE IF NOT EXISTS Ficha(
    id INT SERIAL PRIMARY KEY,
    pessoa_cpf varchar(11),
    bo_pessoa int,
    FOREIGN KEY (pessoa_cpf) REFERENCES Pessoa(cpf),
    FOREIGN KEY (bo_pessoa) REFERENCES bo(id)
);


