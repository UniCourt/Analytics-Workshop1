# What is Docker?

Docker is a container management service. The keywords of Docker are develop, ship and run anywhere. The whole idea of Docker is for developers to easily develop applications, ship them into containers which can then be deployed anywhere.

The initial release of Docker was in March 2013 and since then, it has become the buzzword for modern world development, especially in the face of Agile-based projects.


## Features of Docker
- Docker has the ability to reduce the size of development by providing a smaller footprint of the operating system via containers.

- With containers, it becomes easier for teams across different units, such as development, QA and Operations to work seamlessly across applications.

- You can deploy Docker containers anywhere, on any physical and virtual machines and even on the cloud.

- Since Docker containers are pretty lightweight, they are very easily scalable.

## What is a container?
Containers are instances of Docker images that can be run using the Docker run command. The basic purpose of Docker is to run containers.
- is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
- can be run on local machines, virtual machines or deployed to the cloud.
- is portable (can be run on any OS)
- Containers are isolated from each other and run their own software, binaries, and configurations.

## What is a container image?
When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image. Since the image contains the container’s filesystem, it must contain everything needed to run an application - all dependencies, configuration, scripts, binaries, etc. The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.

