PRAGMA foreign_keys=on;

CREATE TABLE IF NOT EXISTS evento (
    id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
    hmac VARCHAR(255) NOT NULL,
    nome_evento VARCHAR(50) NOT NULL,
    data_evento DATE NOT NULL,
    hora_inicio VARCHAR(10) NOT NULL,
    hora_fim VARCHAR(10) NOT NULL,
    local_evento VARCHAR(15) NOT NULL,
    observacao VARCHAR(100) 
);


CREATE TABLE IF NOT EXISTS registro_presenca (
    id_presenca INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30),
    email VARCHAR(30),
    id_evento INTEGER,
    FOREIGN KEY (id_evento) REFERENCES evento(id_evento)
);


