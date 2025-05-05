DROP DATABASE IF EXISTS cine_adrianGaona;

CREATE DATABASE cine_adrianGaona;

USE cine_adrianGaona;

-- Tabla de géneros
CREATE TABLE generos (
    id_genero VARCHAR(10) PRIMARY KEY,
    nombre_genero VARCHAR(50) NOT NULL
);

-- Tabla de películas
CREATE TABLE peliculas (
    id_pelicula VARCHAR(10) PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    director VARCHAR(100),
    anio INT,
    duracion INT, -- en minutos
    id_genero VARCHAR(10),
    FOREIGN KEY (id_genero) REFERENCES generos(id_genero)
);

-- Insertar géneros
INSERT INTO generos VALUES 
('G1', 'Animación'),
('G2', 'Acción'),
('G3', 'Superhéroes');

-- Insertar películas
INSERT INTO peliculas VALUES 
('P1', 'Toy Story', 'John Lasseter', 1995, 81, 'G1'),
('P2', 'Capitán América', 'Anthony y Joe Russo', 2014, 136, 'G2'),
('P3', 'Spider-Man: No Way Home', 'Jon Watts', 2021, 148, 'G3');
