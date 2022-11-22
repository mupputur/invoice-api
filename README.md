# invoice-api

## Docker set up
**Step1**: Download Docker Desktop on Windows
    **https://desktop.docker.com**
**Step2**: Run the following command in a terminal to install Docker Desktop
    **"Docker Desktop Installer.exe" install**
**Step3**: Run the following command in a terminal if your admin account is different to your user account, you must add the user to the docker-users group:
    **net localgroup docker-users <user> /add**
**Step4**: Search for Docker, and select Docker Desktop in the search results to start Docker Desktop

## Build and run the Docker container
**Step1**: Open terminal and navigate project root directory where the Dockerfile placed
**Step2**: Run the following command to build a docker image
    **docker build -t <imagename>:<tag> .**
**Step3**: Run the following command to show the latest created container
    **docker ps -l**
**Step4**: Run the following command to run the Docker container
    **docker run <imagename/id>**
**Step5**: Run the following command to show all the running commands
    **docker ps**

##Testing
**Customer APIs testing using curl command**
1. To add a new customer
    **curl --X POST -H "Content-type:application/json" --data-binary "{\"customer_id\": 1002,\"first_name\": \"vishnu\",\"last_name\": \"patnayak\",\"company\": \"Google\",\"address\": \"USA\",\"city\": \"USA\",\"state\": \"USA\",\"country\": \"USA\",\"postal_code\": 54332,\"phone\": 564325456,\"email\": \"vishnu@gmail.com\"}" http://127.0.0.1:5000/add_customer**
2. To get all customers
    **curl -v http://127.0.0.1:5000/customers**
3. To get selected customer
    **curl -v http://127.0.0.1:5000/customers/{customerId}**
4. To remove selected customer
    **curl -X DELETE http://127.0.0.1:5000/customers/4567**