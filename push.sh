#!/bin/bash

"This script automates the process of adding, committing, and pushing changes to a Git repository."

"######Status######"
git status

"######Adding changes to staging area######"
git add .

"######Committing changes######"
read -p "Enter commit message: " commit_message

git commit -m "$commit_message"

"######Pushing changes to remote repository######"
git push origin master
