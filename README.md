<h2>crawlDataTiki </h2>


## How to use
- ### Turn on Docker app

  - Back to terminal and use command line:
     </br> - `docker-compose up -d`
     </br> - `docker-compose up -d`
 
- ### Test api
  - in browser go to http://127.0.0.1:8000/docs
  
## Info Docker
  - Database: titki
  - User: root
  - Password: root
  - Table: product
  
## Test db
  - `docker exec -ti containerID mysql -u root -p`
    - Enter password
  - `show databases;`
  -  `use database_name;`
  -  `show tables;`
