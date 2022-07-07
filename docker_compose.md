### What is Docker Compose
Developing applications using Docker can become challenging when juggling multiple services and containers.<br>
Docker Compose is the tool that will help you run multi-container application environments.<br>

An application can consist of multiple containers running different services. It can be tedious to start and manage containers manually, so Docker created a useful tool that helps speed up the process - Docker Compose.<br>

Docker Compose works by applying rules defined in a docker-compose.yaml file. The YAML file configures the application's services and includes rules specifying how you want them to run. With the file in place, you can start, stop, or rebuild all the services using a single command. Additionally, you can check the status of a service, display log outputs, and run one-off commands.
### Docker Compose Basic Commands

```commandline
Command	Description
docker-compose --help	show help, usage instructions for and arguments for the docker-compose command
docker-compose build	look for all services containing the build: statement in the docker-compose.yml file and run a docker build for each one
docker-compose run	run a one-time command against a service
docker-compose up	build, (re)create, start, and attach to containers for a service
docker-compose -f 	specify the location of a docker-compose configuration file by adding the -f flag
docker-compose start	start existing containers for a service
docker-compose stop	stop running containers (without removing them)
docker-compose pause	pause running containers of a service
docker-compose unpause	unpause paused containers of a service
docker-compose down	stop containers (and remove containers, networks, volumes, and images)
docker-compose ps	list containers within the docker-compose configuration file
docker-compose images	list images used by created containers
docker-compose ls	list running Compose projects
```
Create a file named docker-compose.yaml in the same folder that you have cloned with the following contents.
```
version: "3.7"

services:
  db:
    image: postgres
    container_name: app_database
    ports:
      - '0.0.0.0:7000:7000'
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=flask_db
    volumes:
      - app-db:/var/lib/postgres
  web:
    build: .
    ports:
      - "0.0.0.0:8000:80"
    container_name: app_frontend
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - FLASK_ENV=development

volumes:
  app-db:


```


## To build using docker-compose
    docker-compose build --no-cache
- This command used the Dockerfile to build a new container image. You might have noticed that a lot of “layers” were downloaded. This is because we instructed the builder that we wanted to start from the python:3.7-alpine image and other packages. But, since we didn’t have that on our machine, those were needed to be downloaded.
- --no-cache allows users install packages with an index that is updated and not cached locally.


## Running the Application:

From the directory where `docker-compose.yaml` file is present, run `docker-compose up`. This will bring up both the containers and the link will be provided in the terminal. The app will be accessible from that link.

    docker-compose up



## updating content from the app.py
let us change the content from base.html
go to line 66 of app.py
    <br>From:<br>
    `  <p> <label for="phone">Phone : </label> <input type="number" name="phone" placeholder="Phone"> </p>`
    <br>To:<br>
    `  <p> <label for="phone">Phone Number : </label> <input type="number" name="phone" placeholder="Phone"> </p>`
<br><br>Refresh the page on which app is running.
<br>You will notice that the changes that you have made on local machine is not reflected. This is because the code that is present on local is not mounted to the docker container.
<br> Insert the below code on line 26 of docker-compose.yaml file.
```commandline
    volumes: 
      - .:app
```
<br> Now, whenever you make any changes to the code, it will be reflected on the application.