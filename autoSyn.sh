#!/bin/sh
git init 
git status  
git add .  
git commit -m 'add some code from Mac'
# git commit -m 'add some results from Server'
git remote add origin https://github.com/Colourful10/MyRepositories.git
git pull --rebase origin master   #domnload data
git push origin master            #upload data
git stash pop