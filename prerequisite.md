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
    1. Go to Analytics-workshop-1 (which is cloned in above step)
    2. sh prerequisites_install_docker.sh (This will install docker)


## Docker image 
    1. docker pull mysql:8.0
    2. docker pull php:7.4-apache
    3. docker pull hello-world
    4. docker pull alpine

