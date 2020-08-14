# Automate New Project Creation
* Automate the process of creating a new project using this script + batch file.
* Using one shell command, create a new folder in your projects directory with a project name.
* Also creates a GitHub repository with the given project name. Adds a project remote, and performs initial commit with a README.
* Opens project in Visual Studio Code after creating new project folder and GitHub repository.
* Utilizes PyGitHub to access GitHub API

## Pre-Usage
* Add your GitHub API access token
* Add your projects folder directory
* pip install PyGithub

## Usage
* Open Command Prompt in the directory where this script is located
* Use the command "create projectName" to auto-create project folder and GitHub repository
