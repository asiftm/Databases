# :memo: PostgreSQL Job Market Analysis

This project analyzes job postings and skills data using **PostgreSQL**.  
It includes CSV datasets, SQL scripts for database setup, and queries to extract valuable insights about jobs, companies, and skills.


## :open_file_folder: Datasets

- [company_dim.csv](./csv_files/company_dim.csv) → Information about companies.
- [job_postings_fact.csv](./csv_files/job_postings_fact.csv) → Job postings with details like title, salary, and location.
- [skills_dim.csv](./csv_files/skills_dim.csv) → Skills reference table.
- [skills_job_dim.csv](./csv_files/skills_job_dim.csv) → Relationship between jobs and skills.

---

## :gear: Setup Instructions

1. Install PostgreSQL
Download the installer from the official website: :link: [PostgreSQL Downloads](https://www.postgresql.org/download/) .
Follow the wizard and remember the username/password you set.

2. Open ***PostgreSQL*** and run the scripts in [sql_load](./sql_load/):
   - [1_create_database.sql](./sql_load/1_create_database.sql) → Creates the database.
   - [2_create_tables.sql](./sql_load/2_create_tables.sql) → Creates necessary tables.
   - [3_modify_tables.sql](./sql_load/3_modify_tables.sql) → Adjusts schemas (constraints, indexes, etc.).

2. Load the [CSV data](./csv_files/) into the corresponding tables.

---

## :bar_chart: Analysis Queries

The queries in [project_sql/](./project_sql/) provide insights such as:

- [1_top_paying_jobs.sql](./project_sql/1_top_paying_jobs.sql) → Find the highest-paying jobs.
- [2_top_paying_job_skills.sql](./project_sql/2_top_paying_job_skills.sql) → Skills required for top-paying jobs.
- [3_top_demanded_skills.sql](./project_sql/3_top_demanded_skills.sql) → Most in-demand skills across postings.
- [4_top_paying_skills.sql](./project_sql/4_top_paying_skills.sql) → Skills that lead to high-paying opportunities.
- [5_optimal_skills.sql](./project_sql/5_optimal_skills.sql) → Best combination of skills to learn for career growth.

---
## :bulb: References
:link: [PostgreSQL](https://www.postgresql.org/)

:link: [Luke Barousse Youtube Tutorial](https://www.youtube.com/watch?v=7mz73uXD9DA&t=661s)
