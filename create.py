# Imports
from github import Github
import os
import sys
print("created")

# Name of the folder and repo created is given as an argument on the command line
foldername = str(sys.argv[1])

# Set the directory to your projects folder, then add the folder name to create a new folder
directory = r"your-projects-folder-directory" + '/' + foldername

# Get your GitHub user details
g = Github("your-GitHub-access-token")
user = g.get_user()
username = user.login

# Create private repo on your GitHub with name being the argument given on command line
repo = user.create_repo(foldername, private=True)

# Set the array of commands to be executed
# Creates a README file, initializes GitHub repo, does initial commit with README then opens folder in VS Code
commands = [f'echo "#{repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{username}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master',
            'code .']

# Create the new folder in projects folder
os.mkdir(directory)
os.chdir(directory)

# Execute all commands in array in new folder
for c in commands:
    os.system(c)

# Print confirmation
print(f'{foldername} created')
