# Docker and Git Workshop
One Day workshop on understanding Docker and Git.
## Prerequisite
Machine/VM with Linux, Python3 (3.x) and pip3 installed.

### Linux Machine with following packages installed

1. Install Ubuntu 24.04 LTS from [here](https://releases.ubuntu.com/24.04/)
2. Install Git from your terminal by running following commands:
   ```bash
   sudo apt-get update
   sudo apt-get install git
   ```
3. Verify the installation was successful by typing:
   ```bash
   git --version
   ```

### GitHub Account

1. If you don't have an account on GitHub then create an account on [GitHub](https://github.com/join)
2. Configure SSH key by following the below steps:
   - [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)
   - [Adding your SSH key to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

   To list all contents of ssh folder:
   ```bash
   ls -al ~/.ssh
   ```

   To install xclip:
   ```bash
   sudo apt install xclip
   ```

   Copy SSH key:
   ```bash
   xclip -sel clip < ~/.ssh/id_ed25519.pub
   ```

   - [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account)

3. Create a new work directory named `WORKSHOP` inside the `/home` directory:
   ```bash
   mkdir -p ~/WORKSHOP
   ```

4. Fork the [current repository](https://github.com/UniCourt/Analytics-Workshop1)

5. Clone your forked repository inside the `WORKSHOP` directory

> **Info:**
> You can refer [this](https://docs.github.com/en/get-started/quickstart/fork-a-repo) guide to understand how to fork and clone

### Docker Installation

1. To install Docker, follow the steps below:
   - [Set up the repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
   - [Install Docker Engine](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

2. Configure Docker to run without sudo:
   - [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/)

3. Install Docker Compose plugin (comes with Docker Desktop or as a plugin):

   Verify if already installed:
   ```bash
   docker compose version
   ```

   If not installed, install the plugin:
   ```bash
   sudo apt-get update
   sudo apt-get install docker-compose-plugin
   ```

   You should see output similar to:
   ```
   Docker Compose version v2.30.3
   ```

4. Download the following Docker images to your local machine:

   ```bash
   docker pull postgres:16-alpine
   ```

   Verify the image:
   ```bash
   docker run --rm -ti postgres:16-alpine psql -V
   ```

   Output: **psql (PostgreSQL) 16.x**

### VS Code Setup

- [Install VS Code](https://code.visualstudio.com/Download)
- [Install Docker extension on your VS Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

## Docker

By the end of this workshop you will understand:
- The concept of containerization and why it's required
- How to build and run your own containers
- How to run multiple services with Docker Compose
- How to expose ports, use volume mounts, utilize networks, and limit resources (the 4 features we use regularly)

## Git

- You will be introduced to Git
- You will learn Git commands (push, pull, make Pull requests, etc.)

## Schedule

| Time          | Topics |
|---------------|--------|
| 09:00 - 09:30 | Introduction |
| 09:30 - 10:00 | [Introduction to Git](github_intro.md) |
| 10:00 - 11:00 | [Git Commands (push, pull, make Pull requests, etc.)](github_commands.md) |
| 11:00 - 11:30 | [What is Docker](docker_intro.md) |
| 11:30 - 12:00 | [Docker Commands](docker_commands.md) |
| 12:00 - 01:30 | Break |
| 01:30 - 4:00  | [Building Custom Containers](build_container.md) & [Run Multiple Services with Docker Compose](docker_compose.md) |
| 4:00 - 5:00   | [Expose Ports, Volume Mounts, Utilizing Networks, Limiting Resources](docker_ports_volume_mount.md) |
| 5:15 - 5:30   | Wrapping Up |
