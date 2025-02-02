-- Crear la tabla si no existe
CREATE TABLE IF NOT EXISTS user_data (
    userid SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    celular VARCHAR(20),
    nacionalidad VARCHAR(50),
    ubicacion VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS work_experience (
    workid SERIAL PRIMARY KEY,
    company_name VARCHAR(100),
    position VARCHAR(100),
    start_date VARCHAR(10),
    end_date VARCHAR(10),
    userid INTEGER REFERENCES user_data(userid)
);

CREATE TABLE IF NOT EXISTS education (
    educationid SERIAL PRIMARY KEY,
    school_name VARCHAR(100),
    degree VARCHAR(100),
    start_date VARCHAR(10),
    end_date VARCHAR(10),
    userid INTEGER REFERENCES user_data(userid)
);

-- Insertar datos en las tablas
INSERT INTO user_data (userid, nombre, apellido, email, celular, nacionalidad, ubicacion) 
VALUES 
    (1, 'Priscila', 'Parafita', 'priscila.parafita56@gmail.com', 654591486, 'Argentina', 'Barcelona'),
    (2, 'Daniel', 'Fontana', 'daniel@gmail.com', 654591486, 'Argentina', 'Barcelona');

INSERT INTO work_experience (workid, company_name, position, start_date, end_date, userid) 
VALUES 
    (1, 'Mercado Libre', 'ABAP Developer', 'Oct 2017', 'Apr 2021', 1),
    (2, 'Volkswagen', 'Python Backend Developer', 'Apr 2021', 'at present', 1),
    (3, 'Wurth Electronic', 'C# Developer', 'May 2021', 'At present', 2);

INSERT INTO education (educationid, school_name, degree, start_date, end_date, userid) 
VALUES 
    (1, 'Universidad Kennedy', 'System Analyst', 'Oct 2014', 'Dec 2018', 1),
    (2, 'Universidad Tecnologica', 'Data Engineer', 'Apr 2015', 'Dec 2020', 2);

-- Asegurar que la secuencia se actualice
SELECT setval('user_data_userid_seq', (SELECT MAX(userid) FROM user_data));
SELECT setval('work_experience_workid_seq', (SELECT MAX(workid) FROM work_experience));
SELECT setval('education_educationid_seq', (SELECT MAX(educationid) FROM education));
