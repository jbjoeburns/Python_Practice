## GitHub commands

These are the commands, and order, you need to create a github repositiory...

First, go to GitHub and create the repository.

Make sure to copy the HTTPS url provided to you!

Then, go to the local directory you want to make a repository for, then do the following commands...

git init
- initilises git repositiory locally

git branch -M main
- creates a branch named main and sets it to be the 'master' branch
- we do this because GitHub uses 'main' instead of 'master' when referring to these branches

git add .
- stages all files (aside from those in a gitignore)

git commit -m "<message>"
- commits staged files

Once the files are committed then proceed with connecting to GitHub

git remote add origin <url>
- for the url, paste the HTTPS url you copied earlier
- connects to the repository

git push origin main
- pushes the commits on the main branch to the online repository
