COPY company_dim
FROM 'C:\Users\asifm\OneDrive\repos\Databases\PostgreSQL\csv_files\company_dim.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');

COPY skills_dim
FROM 'C:\Users\asifm\OneDrive\repos\Databases\PostgreSQL\csv_files\skills_dim.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');

COPY job_postings_fact
FROM 'C:\Users\asifm\OneDrive\repos\Databases\PostgreSQL\csv_files\job_postings_fact.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');

COPY skills_job_dim
FROM 'C:\Users\asifm\OneDrive\repos\Databases\PostgreSQL\csv_files\skills_job_dim.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');


-- Verify data insertion
SELECT * FROM company_dim LIMIT 10;

SELECT * FROM skills_dim LIMIT 10;

SELECT * FROM job_postings_fact LIMIT 10;

SELECT * FROM skills_job_dim LIMIT 10;

