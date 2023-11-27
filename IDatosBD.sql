-- Crea la base de datos
CREATE DATABASE idatos;

-- Selecciona la base de datos para usar
\connect idatos;

-- Crea una tabla en la base de datos
CREATE TABLE busqueda (
    id SERIAL PRIMARY KEY,
    articulo VARCHAR(100),
    peso DECIMAL(10,2)
);

-- Crea una tabla en la base de datos
CREATE TABLE resultado (
    titulo VARCHAR(200) PRIMARY KEY,
    precio DECIMAL(10,2),
    moneda VARCHAR(3),
    url_resultado VARCHAR(200),
    busqueda_id INTEGER REFERENCES busqueda(id)
);

-- Subclase de resultado
CREATE TABLE ml (
    titulo VARCHAR(200) PRIMARY KEY REFERENCES resultado(titulo),
    costoEnvio DECIMAL(10,2)
);

-- Subclase de resultado
CREATE TABLE ebay (
    titulo VARCHAR(200) PRIMARY KEY REFERENCES resultado(titulo),
    costoEnvioDesdeUSA DECIMAL(10,2),
    impuestosAduana DECIMAL(10,2)
);