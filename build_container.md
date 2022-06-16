#### What is a container?
Containers are instances of Docker images that can be run using the Docker run command. The basic purpose of Docker is to run containers.
- is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
- can be run on local machines, virtual machines or deployed to the cloud.
- is portable (can be run on any OS)
- Containers are isolated from each other and run their own software, binaries, and configurations.

#### What is a container image?
When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image. Since the image contains the container’s filesystem, it must contain everything needed to run an application - all dependencies, configuration, scripts, binaries, etc. The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.
### Build the app’s container image
in order to build the application, we need to use a Dockerfile. A Dockerfile is simply a text-based script of instructions that is used to create a container image

1. Get the app from git
```    
https://github.com/UniCourt/Analytics-Workshop1 ==> clone this repo or download zip
```
Unzip the file and cd into the app folder.

2. Create a file named Dockerfile in the above folder with the following contents.
```
FROM python:3.7-alpine

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


CMD ["flask", "run"]
```
Contents of Dockerfile:<br>
a. Get the base image: `FROM python:3.7-alpine`. This pulls the base python 3.7 image.<br>
b. Declaring environment variables.<br>
c. Copy the custom code into the image by `COPY . /app` and change working directory.<br>
c. Install required packages in the image. `RUN pip install -r requirements.txt`.<br>

3. Create a new requirements.txt file with following contents

```
Flask
psycopg2-binary
````
This will install Flask and psycopg2-binary, which is required for postgres connection.


4. open a terminal and go to the app directory with the Dockerfile. Now build the container image using the docker build command
```
docker build -t app-new .
````
<!-- Remember the -d and -p flags? We’re running the new container in “detached” mode (in the background) and creating a mapping between the host’s port 8000 to the container’s port 3000. Without the port mapping, we wouldn’t be able to access the application. -->

### Start an app container

Start your container using the docker run command and specify the name of the image we just created
```commandline
docker run app-new
```

### Note: Do not panic if you see errors mentioned below in your terminal, this is because we do not have necessary things to connect to db
```commandline
KeyError: 'POSTGRES_USER'
```

## To view the running container
```commandline
docker ps
```
This will list all the running containers.

## To stop the running container

    docker stop <container if that you see when you run>
