# Mini 5  
## SQLite Python CRUD

[![CI](https://github.com/nogibjj/DEmini5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/DEmini5/actions/workflows/cicd.yml)

## Purpose
The purpose of this project is to create CRUD actions using SQLite and Python, and to build an ETL-query pipeline. Here, we use `alcohol.csv` as a sample dataset, convert it to a `.db` file, and conduct CRUD actions (with queries) on it.


## Workflow
![Workflow](assets/workflow.png)

## Perparation
1. Create: create a new codespaces with all required packages loaded.   
2. Extract data `make extract`: Extract `alcohol.csv` data from the url.     
3. Transform and load data `make transform_load`: connect the `alcohol.csv` file to the `alcoholDB.db` using SQLite.
<img width="1058" alt="image" src="https://github.com/user-attachments/assets/ad0c7fcd-c010-4f2d-a9e6-d1443a0f79cb">


## Actions 
1. **Format**: `make format`    
2. **Lint**: `make lint`
<img width="988" alt="image" src="https://github.com/user-attachments/assets/ffe525bb-23d5-44b1-a7e0-2ea83f830066">


3. **Test**: `make test`
<img width="1165" alt="image" src="https://github.com/user-attachments/assets/ffd0eca3-d37c-4bac-b8a2-eb5bbc4e3bd3">


## Tests
### CRUD Actions
1. **Create**   
Create a new record using `create()`: 
python main.py update 1000 country_A 1 1 1 1.1

2. **Read** 
Read all data using `read()`:   
python main.py read

3. **Update**   
Update a raw with primary key 3 using `update`:  
python main.py update 3 country_A 10 10 10 10

4. **Delete**   
Delete one record with primary key 1 using `delete()`: 
python delete 1


## Reference
https://github.com/nogibjj/sqlite-lab
