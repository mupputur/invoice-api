#  Invoice Customer API using Flask

- [Overview](#overview)
- [Pre-requisites](#pre-requisites)
- [Docker-Setup](#docker-setup)
- [App-Deployment](#App-deployment)
- [Testing](#Testing)

## Overview 

## Pre-requisite 

## Docker Setuo

1. Download Docker Desktop on Windows
    **https://desktop.docker.com**
    
2. Run the following command in a terminal to install Docker Desktop
    **"Docker Desktop Installer.exe" install**
    
3. Run the following command in a terminal if your admin account is different to your user account, you must add the user to the docker-users group:
    **net localgroup docker-users <user> /add**
   
4. Search for Docker, and select Docker Desktop in the search results to start Docker Desktop

   
## App-Deployment
1. Clone the project  & open terminal download navigate project root directory where the Dockerfile placed
**Note:** Use service names(invoice-app, db) which are defined in the docker-compose file to run Flask app and MySQL in Docker container
1. Run the dockerized app by executing the following command
```**docker-compose up -d**```

2. If everything went right, you will see Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) in the terminal or you can see container logs in Docker Desktop app

3. Run the following command to stop the Docker container
        ``` **docker-compose down** ```
   
4. Run the following command to show all the containers
     ``` **docker ps** ```
   
**Testing:** 

**Customer APIs testing using curl command**
 ```
**Note:** Use localhost/127.0.0.1 as hosts to run Flask app and connect MySQL Database
1. To add a new customer

    **curl --X POST -H "Content-type:application/json" --data-binary "{\"customer_id\": 1002,\"first_name\": \"vishnu\",\"last_name\": \"patnayak\",\"company\": \"Google\",\"address\": \"USA\",\"city\": \"USA\",\"state\": \"USA\",\"country\": \"USA\",\"postal_code\": 54332,\"phone\": 564325456,\"email\": \"vishnu@gmail.com\"}" http://127.0.0.1:5000/add_customer**
    
2. To get all customers

    **curl -v http://127.0.0.1:5000/customers**
  
3. To get selected customer

    **curl -v http://127.0.0.1:5000/customers/{customerId}**
 
4. To remove selected customer
    **curl -X DELETE http://127.0.0.1:5000/customers/4567**
```   
