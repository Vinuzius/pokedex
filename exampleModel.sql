-- 1. Criação do Schema
CREATE SCHEMA IF NOT EXISTS pokemon;

-- 2. Criação do ENUM (Garante que só aceite esses valores exatos)
CREATE TYPE pokemon.status_captura AS ENUM (
    'coletado', 
    'nao coletado', 
    'trocar', 
    'evoluir', 
    'breed'
);

-- 3. Criação das Tabelas
CREATE TABLE pokemon.game (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    geracao INT NOT NULL
);

CREATE TABLE pokemon.pokemon (
    id SERIAL PRIMARY KEY,
    numero_dex INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    status pokemon.status_captura NOT NULL -- Usando o ENUM que criamos acima
);

CREATE TABLE pokemon.local (
    id SERIAL PRIMARY KEY,
    id_game INT NOT NULL,
    rota VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_game) REFERENCES pokemon.game(id) ON DELETE CASCADE
);

CREATE TABLE pokemon.pokemonlocal (
    id_local INT NOT NULL,
    id_pokemon INT NOT NULL,
    descricao VARCHAR(255),
    PRIMARY KEY (id_local, id_pokemon),
    FOREIGN KEY (id_local) REFERENCES pokemon.local(id) ON DELETE CASCADE,
    FOREIGN KEY (id_pokemon) REFERENCES pokemon.pokemon(id) ON DELETE CASCADE
);

-- --4. Inserção de Dados (Games)
-- INSERT INTO pokemon.game (nome, geracao) VALUES 
-- ('Red', 1), ('Blue', 1), ('Yellow', 1),
-- ('Gold', 2), ('Silver', 2), ('Crystal', 2),
-- ('Ruby', 3), ('Sapphire', 3), ('Emerald', 3),
-- ('FireRed', 3), ('LeafGreen', 3),
-- ('Diamond', 4), ('Pearl', 4), ('Platinum', 4),
-- ('HeartGold', 4), ('SoulSilver', 4),
-- ('Black', 5), ('White', 5), ('Black 2', 5), ('White 2', 5),
-- ('X', 6), ('Y', 6), ('Omega Ruby', 6), ('Alpha Sapphire', 6),
-- ('Sun', 7), ('Moon', 7), ('Ultra Sun', 7), ('Ultra Moon', 7),
-- ('Sword', 8), ('Shield', 8), ('Legends: Arceus', 8),
-- ('Scarlet', 9), ('Violet', 9);

-- -- 5. Inserção de Dados de Teste (Pokémons, Locais e Relacionamento)
-- -- O Postgres converte a string automaticamente para o ENUM 'status_captura'
-- INSERT INTO pokemon.pokemon (numero_dex, nome, status) VALUES 
-- (1, 'Bulbasaur', 'coletado'),
-- (4, 'Charmander', 'trocar');

-- -- Assumindo que os IDs de 'Red' gerados acima são 1 e 2
-- INSERT INTO pokemon.local (id_game, rota) VALUES 
-- (1, 'Rota 1'),
-- (1, 'Rota 2');

-- INSERT INTO pokemon.pokemonlocal (id_local, id_pokemon, descricao) VALUES 
-- (1, 1, 'Aparece na grama alta durante o dia'),
-- (2, 2, 'Raro de encontrar, prefere áreas ensolaradas');
