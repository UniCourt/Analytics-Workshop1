## Docker post-installation setup
Do the optional precodure configuration to work better with Docker.

### Run Docker as non-root user
To create the docker group and add your user:
1. Create the docker group.
```
sudo groupadd docker
```
2. Add your user to the docker group.
```
sudo usermod -aG docker $USER
```

3. Activate the changes to groups:
```
newgrp docker 
```
4. Verify that you can run docker commands without sudo.
```
docker images
```

<br />

## Docker Commands
Docker is a containerization system which packages and runs the application with its dependencies inside a container. There are several docker commands you must know when working with Docker.
### 1. Docker version
To find the installed docker version
Command:
```
docker  -version
``` 
Example:
```
docker --version
Docker version 19.03.9, build 9d988398e7
```

<br>

### 2. Downloading image
To work with any docker image we need to download the docker image first.<br /> 
Command:
```
docker pull <IMAGE>
```
Example of pulling alpine:latest image
```
docker pull alpine:latest
```

<br>

### 3. List all the docker images
To list all the images that is locallt available in the host machine, simply run the below command. This will list all the docker images in the local system.
<br />
Command:
```
docker images
Example:
```
REPOSITORY  TAG  IMAGE ID       CREATED      SIZE
alpine     latest  c059bfaa849c 6 weeks ago  5.59MB
```
docker images
```

### 3. Run docker image
The docker run command first creates a writeable container layer over the specified image, and then starts it using the specified command.
<br>
Command:
```
docker run [options] <IMAGE>
```
> Explore options [here](https://docs.docker.com/engine/reference/run/)


Example of running alpine:latest image, the options -t allows us to acces the terminal and -i gets stdin stream added. Basicaly using -ti adds the terminal driver.
```
docker run -t -i alpine:latest
or
docker run -ti alpine:latest
```

<br>

### 4. Running containers
Let us check what all the container are running currently, The command. `docker ps` will list only running containers
<br>
Command:
```
docker ps
```
Emaple:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
8973c7347905        alpine:latest       "/bin/sh"           2 minutes ago       Up 2 minutes                            ecstatic_jang
```
<br />

### 5. Access the docker container
The `docker exec` command runs a new command in a running container. We need container id to execute into conatiner, get the container id by `docker ps`.
<br />
Command to execute into container:
```
docker exec [OPTIONS] <CONTAINER_ID> COMMAND
```
> Explore options [here](https://docs.docker.com/engine/reference/commandline/exec/)

Example: Execute into running alpine:latest container, and let us create one directory and a simple blank text file.
```
docker exec -ti 8973c7347905 sh
/ # mkdir demo
/ # cd demo
/demo # touch helloworld.txt
/demo # ls
helloworld.txt
/demo # 
```
`mkdir` command to create directory or folder<br />
`cd` change directory used to change the current working directory <br />
`touch` Touch command allows to create a blank file <br />
<br />

### 6. Stop the container
Now let us stop the running container 
<br />
Command:
```
docker stop [OPTIONS] <CONTAINER_ID>
```
> Explore options [here](https://docs.docker.com/engine/reference/commandline/stop/)<br />
Example of stopping alpine:latest running container
```
docker stop 8973c7347905
```
Here once you stop the container, the container is available locally but it is not in the running state. In the follwing step we will how to remove stopped container.   
<br  />

### 7. List all the containers
`docker ps -a` will list all the containers including stopped containers.
<br/>
Example output:
```
mis@mispl-lap-19:~$ docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS                       PORTS                                                 NAMES
4cc4008815d8        alpine:latest             "/bin/sh"                57 minutes ago      Exited (137) 2 minutes ago
```

<br />

### 8. Remove the container 
You can remove the container or multiple containers by `docker rm` command.<br />
Command
```
docker rm [OPTIONS] <CONTAINER...>
```
> Explore Options [here](https://docs.docker.com/engine/reference/commandline/rm/)
Example:
```
docker rm 4cc4008815d8
```
Note: Once you stop the container 

### 8. Start the container
Let's start the alpine:latest container again. Remember previously you have 
<br />
Command:
```
docker start [OPTIONS] <CONTAINER_ID>
```
> Explore options [here](https://docs.docker.com/engine/reference/commandline/start/)


Example of starting alpine:latest container. Before to start the container we need the container id, so let's get the container id by `docker ps -a` command.
```
docker ps -a

docker start 4cc4008815d8
```
<br />

### 10. Removing image
You can remove the local images by `docker rmi` command.
<br />
Command:
```
docker rmi [OPTIONS] <IMAGE_ID> / <IMAGE_ID...>
```
Example: Remove alpine:latest container
```
docker rmi c059bfaa849c
```
