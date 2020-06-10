# Develops_today_test

This API gives access to CRUD operations with entities in the database.To get started with it, you will need Docker and Docker Compose 

#### Start

You have to create: 

1. settings_local.py an example settings_local.dev.py 
2. .env an example .env.example 
3. directory "run" in project folder 

Then start docker by command:

`docker-compose -f dc.yml up -d --build`

#### Tests

You can start tests. To do this, you need to run the command:
 
`docker exec -it backend_develops_today pytest ./src`

##### You can also visit this resource [here](http://67.205.134.130:8000/).
##### Postman collection you can find [here](https://documenter.getpostman.com/view/10902684/Szzegfh2?version=latest).