-- Crear la tabla si no existe
CREATE TABLE IF NOT EXISTS user_data (
    userid SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    celular VARCHAR(20),
    nacionalidad VARCHAR(50),
    ubicacion VARCHAR(200),
    github VARCHAR(200),
    linkedin VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS work_experience (
    workid SERIAL PRIMARY KEY,
    company_name VARCHAR(100),
    position VARCHAR(100),
    description VARCHAR(255),
    start_date DATE,
    end_date DATE,
    userid INTEGER REFERENCES user_data(userid)
);

CREATE TABLE IF NOT EXISTS education (
    educationid SERIAL PRIMARY KEY,
    school_name VARCHAR(100),
    degree VARCHAR(100),
    start_date DATE,
    end_date DATE,
    userid INTEGER REFERENCES user_data(userid)
);

-- Insertar datos en las tablas
INSERT INTO user_data (userid, nombre, apellido, email, celular, nacionalidad, ubicacion) 
VALUES 
    (1, 'Priscila', 'Parafita', 'priscila.parafita56@gmail.com', 654591486, 'Argentina', 'Barcelona'),
    (2, 'Daniel', 'Fontana', 'daniel@gmail.com', 654591486, 'Argentina', 'Barcelona'),
    (3, 'Tone', 'Bird', 'tonecito@gmail.com', 678687, 'Argentina', 'Buenos Aires');

INSERT INTO work_experience (workid, company_name, position, description, start_date, end_date, userid) 
VALUES
    (1, 'Mercado Libre', 'ABAP Developer', 'Prueba de description', '2017-10-28', '2021-04-11', 1),
    (2, 'Volkswagen', 'Python Backend Developer', 'Prueba de description Prueba de description Prueba de description', '2021-04-11', NULL, 1),
    (3, 'Wurth Electronic', 'C# Developer', 'Prueba de description Prueba de description Prueba de description Prueba de description Prueba de description Prueba de description Prueba de description', '2021-01-21', NULL, 2),
    (4, 'Casa Rosada', 'Sultan', 'Prueba de description','2000-05-01', NULL, 3);


INSERT INTO education (educationid, school_name, degree, start_date, end_date, userid) 
VALUES 
    (1, 'Universidad Kennedy', 'System Analyst', '2014-10-04', '2018-12-31', 1),
    (2, 'Universidad Tecnologica', 'Data Engineer', '2015-04-01', '2020-12-31', 2),
    (3, 'Universidad Birds', 'El rey de todos', '1995-04-10', '2000-12-31', 3);


-- Asegurar que la secuencia se actualice
SELECT setval('user_data_userid_seq', (SELECT MAX(userid) FROM user_data));
SELECT setval('work_experience_workid_seq', (SELECT MAX(workid) FROM work_experience));
SELECT setval('education_educationid_seq', (SELECT MAX(educationid) FROM education));
