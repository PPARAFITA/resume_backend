-- Crear la tabla si no existe
CREATE TABLE IF NOT EXISTS user_data (
    userid SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    celular VARCHAR(20),
    nacionalidad VARCHAR(50),
    ubicacion VARCHAR(200),
    about_me JSONB,
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



CREATE TABLE IF not EXISTS skills(
    skillid SERIAL PRIMARY KEY,
    user_skill JSONB,
    userid INTEGER REFERENCES user_data(userid)
);

-- Insertar datos en las tablas
INSERT INTO user_data (userid, nombre, apellido, email, celular, nacionalidad, ubicacion, about_me, github, linkedin) 
VALUES 
    (1, 'Priscila', 'Parafita', 'priscila.parafita56@gmail.com', '654591486', 'Argentina', 'Barcelona', 
         '[
        {
            "type": "paragraph",
            "content": "I have over 13 years of experience as a backend developer, primarily working with ABAP in the SAP ecosystem.\nThroughout my career, I have developed and optimized business processes,\nimplemented complex data models,\nand integrated SAP systems to enhance enterprise efficiency."
        },
        {
            "type": "paragraph",
            "content": "My expertise spans custom development, performance tuning, and debugging within SAP environments, ensuring that solutions align with business needs."
        },
        {
            "type": "paragraph",
            "content": "In recent years, I decided to transition into Python development to expand my skill set and embrace modern backend technologies. This shift was driven by my interest in FastAPI, Django, and Flask, as well as my passion for working with APIs, microservices, and cloud computing."
        }
    ]',
     'https://github.com/PPARAFITA', 'https://linkedin.com/PPARAFITA'),
    
    (2, 'Daniel', 'Fontana', 'daniel@gmail.com', '654591486', 'Argentina', 'Barcelona', 
    '[
        {
            "type": "paragraph",
            "content": "I have over 13 years of experience as a backend developer, primarily working with ABAP in the SAP ecosystem."
        }]','',''),
    (3, 'Tone', 'Bird', 'tonecito@gmail.com', '678687', 'Argentina', 'Buenos Aires', 
    '[
        {
            "type": "paragraph",
            "content": "I have over 13 years of experience as a backend developer, primarily working with ABAP in the SAP ecosystem."
        }
    ]'
    ,'','');

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



INSERT INTO skills (skillid, user_skill, userid) 
VALUES (
    1, 
    '[
        {
            "skill_title": "Backend",
            "skill_tags": ["Node.js", "Express", "PostgreSQL", "MongoDB", "REST APIs"]
        },
        {
            "skill_title": "Tools",
            "skill_tags": ["Git", "Docker", "AWS", "Jest", "REST APIs"]
        },
        {   
            "skill_title": "Soft Skills",
            "skill_tags": ["Team Leadership","Communication","Problem Solving", "Agile"]
        },
         {
            "skill_title": "SAP",
            "skill_tags": ["ABAP", "CDS Views", "OData", "Fiori", "S/4"]
        }
    ]',
    1 
);

-- Asegurar que la secuencia se actualice
SELECT setval('user_data_userid_seq', (SELECT MAX(userid) FROM user_data));
SELECT setval('work_experience_workid_seq', (SELECT MAX(workid) FROM work_experience));
SELECT setval('education_educationid_seq', (SELECT MAX(educationid) FROM education));
