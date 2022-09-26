# Docker and Git Workshop

One Day workshop on understanding Docker and Git

## Prerequisite
Machine/VM with linux, python3 (3.xx) and pip3 installed 
Please run the following commands on your virtual machine(linux) or machine with linux OS

Make sure you have an active internet connection while running these.

These will download certain files required for the workshop.


## Install git:
Commands to install the latest Git from the officially maintained package archives:

    sudo apt-add-repository ppa:git-core/ppa

    sudo apt-get update

    sudo apt-get install git
    
    git clone https://github.com/UniCourt/Analytics-Workshop1
    
creating a github account 
<br>Step 1: open  https://github.com/ and sign up
<br>Step 2: Login with your email
<br> Step 3: open https://github.com/UniCourt/Analytics-Workshop1 in your browser and Fork (option between watch and star) 

## Docker install 
    1. cd Analytics-Workshop1/ (which is cloned in above step)
    2. sh prerequisites_install_docker.sh (This will install docker)


## Docker image 
    1. sudo docker pull mysql:8.0
    2. sudo docker pull php:7.4-apache
    3. sudo docker pull hello-world
    4. sudo docker pull alpine
## Docker

- By the end of this workshop you will understand following things
- You will be Introduced to the concept of containerisation and why its required.
- You will learn how to Build and run your own Containers.
- You will learn how to Run Multiple Services with Docker Compose
- You will learn how to Expose Ports, Volume Mounts, Utilizing Networks, Limiting Resources (the 4 features we use regularly.)
## GIT
- You will be Introduced to GIT
- You will learn git commands (push, pull make Pull request etc)
## Schedule
| Time            | Topics
|-----------------|-------
| 09:00 - 09:30   |  [`Introduction`]
| 09:30 - 10:00   |  [`Introduction to GIT`](github_intro.md)
| 10:00 - 11:00   |  [`Git Commands (push, pull, make Pull request etc)`](github_commands.md)
| 11:00 - 11:30   |  [`What is docker`](docker_intro.md)
| 11:30 - 12:00   |  [`Docker Commands`](docker_commands.md)
| 12:00 - 01:30   |  [`Break`]
| 01:30 - 4:00    |  [`Building Custom Containers`](build_container.md)
|                 | [`Run Multiple Services with Docker Compose`](docker_compose.md)
| 4:00 -  5:00    |  [`Expose Ports, Volume Mounts, Utilizing Networks, Limiting Resources`](docker_ports_volumn_mount.md)
| 5:15 -  5:30    |  [`Wrapping Up`]