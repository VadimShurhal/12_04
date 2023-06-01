# Main commands of git
1. Creating new branch:
```
git branch -b new_branch_name
```
2. Checkout to another branch
```
git checkout another_branch_name
```
3. Commit your changes to local repository:
```
git commit -a -m "title of commit"
```
4. Merge changes from feature branch to master branch (first of all you should be in master branch already before merge)
```
git merge feature
```
5. Check status of local repository:
```
git status
```
6. Push all committed changes from local repository to origin repository:
```
git push 
```
7. Push all committed changes to specific remote branch:
```
git push origin feature_25
```
8. Bind your local repository with remote repository:
```
git remote add origin https://github.com/path_to_your_repository.git
```
9. Get all latest changes from remote branch:
```
git pull
```
10. Add file / folder for tracking by git:
```
git add path_to_file_in_project
```