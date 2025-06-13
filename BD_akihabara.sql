-- 1. Crear base de datos
CREATE DATABASE IF NOT EXISTS akihabara_db;
USE akihabara_db;

-- 2. Crear tabla producto
CREATE TABLE IF NOT EXISTS producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(100),
    precio DECIMAL(10, 2),
    stock INT
);

-- 3. Crear el usuario userAkihabara con contraseña segura
CREATE USER IF NOT EXISTS 'userAkihabara'@'localhost' IDENTIFIED BY 'Akihabara2025!';

-- 4. Conceder permisos CRUD al usuario sobre la base de datos akihabara_db
GRANT SELECT, INSERT, UPDATE, DELETE ON akihabara_db.* TO 'userAkihabara'@'localhost';

-- 5. Aplicar cambios de privilegios
FLUSH PRIVILEGES;

-- 6. Insertar productos de prueba en todas las categorías
INSERT INTO producto (nombre, categoria, precio, stock) VALUES
('Figura de Goku', 'Figura', 34.99, 5),
('Manga One Piece Vol. 1', 'Manga', 7.95, 12),
('Póster Naruto', 'Póster', 9.50, 8),
('Llavero Pikachu', 'Llavero', 4.75, 20),
('Camiseta Attack on Titan', 'Ropa', 19.99, 6),
('Figura de Luffy', 'Figura', 39.90, 4),
('Manga Naruto Vol. 3', 'Manga', 8.25, 10),
('Póster Demon Slayer', 'Póster', 10.00, 5),
('Llavero Totoro', 'Llavero', 5.00, 15),
('Sudadera Tokyo Revengers', 'Ropa', 29.95, 3);



-- Sentencia SELECT para comprobación
SELECT * FROM akihabara_db.producto;

