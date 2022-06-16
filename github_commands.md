# Basic GIT Commands:
## Create a gitHub account
https://github.com/



Run following command to verify if Git works on your computer:

    git --version

## Configure git:
After installing to start using git from your computer, you must enter your credentials to identify yourself as the author of your work. The username and email address should match the ones you use in GitHub.

Add your user name:

    git config --global user.name "your_username"

Add your email address:

    git config --global user.email "your_email_address@example.com"

To check the configuration, run:

    git config --global --list

Add ssh keys to your GitHub account:
    
    1. sudo apt install xclip
    2. ssh-keygen -t ed25519 -C  "your_email"
    3. xclip -sel clip < ~/.ssh/id_ed25519.pub
    4. Visit this url: https://github.com/settings/ssh/new. Paste the key and save.


## Fork a repository
Forking refers to making a copy of a project you want to contribute to. Now lets fork a project provided to complete this activity. 

Follow these steps to fork a project:

1. Go to the project url using this link:https://github.com/nireekshith-uc/workshop or any other link
2. Click on the fork button in the project page
3. Select a namespace to fork our project. Select your namespace here.

## Clone a repository
Cloning a repository means the files from the remote repository are downloaded to your computer, and a connection is created.

This connection requires you to add credentials. There are two ways to add credentials SSH and HTTPS. We use SSH method here.

Authenticate with GitLab by following the instructions in the SSH documentation.

1. Go to your project’s landing page and click Clone.
2. Copy the URL for Clone with SSH.
3. Open a terminal and go to the directory where you want to clone the files. Run this command:

        git clone <url_to_clone>

    For example,

        git clone "git@github.com:nireekshith-uc/workshop.git"

## View your remote repositories
To view the remote repositories that you have added, run following command:

    git remote -v
## Configuring remote repositories

We now need to configure our local sytem to the remote repositories in the git. Generally two remote repositories are maintained origin and upstream. 
- Origin is a clone of your forked repository, from which you push and pull.
- Upstream is the main repo you forked, from where you pull and keep cloned repository updated, but you generally don't have push access to it.

Since you cloned your repo from github.com you should have already have a remote called origin.

Run the following command to add upstream repository.

    git remote add upstream <upstream_clone_url>

For example,

    git remote add upstream "git@github.com:nireekshith-uc/workshop.git"


## Create a branch
Branches allow you to develop features, fix bugs, or safely experiment with new ideas in a contained area of your repository. You always create a branch from an existing branch. Typically, you might create a new branch from the default branch of your repository.


To create a new branch called excercise run the following command:

    git checkout -b excercise


To switch to an existing branch we use the following command:

    git checkout <branch_name>


To see what branch you are currently on try the following command.

```shell
git branch
```

Make sure you are on the exercise branch by running

```shell
git checkout exercise
```

## Download the latest changes in the project
To get an up-to-date copy of the project, we use pull command. This gets all the changes made to the repository, since the last clone or pull. 

To get all the latest updates run the following command:

    git pull upstream <branch_name>

To pull changes to your newly created branch, run following command:

    git pull upstream main

## Create new text file
Create new file index.txt in your local system.
Add following line to your index.txt file and save:

    Welcome to GIT workshop!

## View the changed files 
This command displays the state of the working directory and the staging area.
To check all the files you have changed run following command.

    git status
## View differences
Now lets see the differences between your local unstaged changes and the latest version that you cloned or pulled. 

Run following command to see the differences:

    git diff

## Stage the local changes
We use git add to add all/required files that are changed to the staging area.
To stage a file that you have changed for commit run following command:

    git add <file_name>

To add your index.txt file, run following command:

    git add index.txt

To stage all files in the current directory and subdirectory, we can use following command:

    git add .

## Commit the stagged files:
The git commit command creates a snapshot of all the stagged changes in the project history.
Now to commit all the changed that are made run the following command:

    git commit -m "message"
The message in the commit command must describe the intension of your commit. For example,

    git commit -m "Adding new file"


## Send the changes to the remote repository
Push command sends all the committed changes to the remote repository. To push all your changes to the remote repository run the following command:

    git push origin <branch_name>

To push your changes

    git push origin excercise

You can now go to github.com and see the updated code in your browser.

## Create a pull request:
Pull request is the process of merging the changed version of code to its original version. A pull request allows us to visualize the differences between the original code and our proposed code changes. 

Steps to create a pull request:
1. When we push changes to the remote repository, git prompts us with a link to create a merge request. We can copy-paste the link in the browser or create a new pull request from the project page in the browser.

2. Then select the base branch and compare branch that needs to be merged. The base branch is the one that has your changes and the compare branch is the original branch.

3. Add proper title, description and submit the merge request.
