CREATE DATABASE ahorcado;

USE ahorcado;

-- Tablas 


CREATE TABLE usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20),
    n_victorias INT DEFAULT 0,
    n_derrotas INT DEFAULT 0
);

CREATE TABLE palabras(
	id INT PRIMARY KEY AUTO_INCREMENT,
    palabra VARCHAR(50),
	categoria VARCHAR(25)
);

CREATE TABLE partidas(
	id_usuario INT NOT NULL,
    id_palabra INT NOT NULL,
	seGano boolean,
    PRIMARY KEY(id_usuario, id_palabra),
    CONSTRAINT foranea_usuarios FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    CONSTRAINT foranea_palabras FOREIGN KEY (id_palabra) REFERENCES palabras(id)
);

-- Insersión de datos



-- Frutas
INSERT INTO palabras (palabra, categoria) VALUES
('manzana', 'frutas'),
('platano', 'frutas'),
('naranja', 'frutas'),
('fresa', 'frutas'),
('uva', 'frutas'),
('pera', 'frutas'),
('sandia', 'frutas'),
('kiwi', 'frutas'),
('cereza', 'frutas'),
('melon', 'frutas'),
('ciruela', 'frutas'),
('mango', 'frutas'),
('papaya', 'frutas'),
('piña', 'frutas'),
('coco', 'frutas'),
('granada', 'frutas'),
('durazno', 'frutas'),
('mandarina', 'frutas'),
('arandano', 'frutas'),
('frambuesa', 'frutas'),
('higo', 'frutas'),
('aguacate', 'frutas'),
('moras', 'frutas'),
('nectarina', 'frutas'),
('limon', 'frutas');

-- Conceptos informáticos
INSERT INTO palabras (palabra, categoria) VALUES
('computadora', 'conceptos_informaticos'),
('programacion', 'conceptos_informaticos'),
('algoritmo', 'conceptos_informaticos'),
('redes', 'conceptos_informaticos'),
('internet', 'conceptos_informaticos'),
('base de datos', 'conceptos_informaticos'),
('sistemas operativos', 'conceptos_informaticos'),
('nube', 'conceptos_informaticos'),
('inteligencia artificial', 'conceptos_informaticos'),
('machine learning', 'conceptos_informaticos'),
('big data', 'conceptos_informaticos'),
('ciberseguridad', 'conceptos_informaticos'),
('programador', 'conceptos_informaticos'),
('desarrollador', 'conceptos_informaticos'),
('software', 'conceptos_informaticos'),
('hardware', 'conceptos_informaticos'),
('codificacion', 'conceptos_informaticos'),
('lenguajes de programacion', 'conceptos_informaticos'),
('cloud computing', 'conceptos_informaticos'),
('redes sociales', 'conceptos_informaticos'),
('web', 'conceptos_informaticos'),
('servidor', 'conceptos_informaticos'),
('cliente', 'conceptos_informaticos'),
('API', 'conceptos_informaticos'),
('firewall', 'conceptos_informaticos'),
('virtualizacion', 'conceptos_informaticos'),
('backend', 'conceptos_informaticos'),
('frontend', 'conceptos_informaticos');

-- Nombres de personas
INSERT INTO palabras (palabra, categoria) VALUES
('Juan', 'nombres_personas'),
('Maria', 'nombres_personas'),
('Pedro', 'nombres_personas'),
('Ana', 'nombres_personas'),
('Luis', 'nombres_personas'),
('Carlos', 'nombres_personas'),
('Marta', 'nombres_personas'),
('Jose', 'nombres_personas'),
('Sofia', 'nombres_personas'),
('David', 'nombres_personas'),
('Laura', 'nombres_personas'),
('Pablo', 'nombres_personas'),
('Elena', 'nombres_personas'),
('Raul', 'nombres_personas'),
('Julia', 'nombres_personas'),
('Andres', 'nombres_personas'),
('Sandra', 'nombres_personas'),
('Javier', 'nombres_personas'),
('Victor', 'nombres_personas'),
('Isabel', 'nombres_personas'),
('Ricardo', 'nombres_personas'),
('Cristina', 'nombres_personas'),
('Francisco', 'nombres_personas'),
('Fernando', 'nombres_personas'),
('Beatriz', 'nombres_personas'),
('Gabriel', 'nombres_personas'),
('Paula', 'nombres_personas'),
('Diego', 'nombres_personas'),
('Raquel', 'nombres_personas');
