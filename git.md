# Git

## Basic

```bash
# install on centos
sudo yum install git
```

## Branch

```bash
# force replace remote branch
git push -f <remote> <branch_name>

# delete remote branch
git push -d origin <branch_name>

# delete local branch
git branch -d origin/bugfix

# rename local branch
git branch -m <new_name>

# replace master with branch
git checkout <branch>
git merge -s ours master
git checkout master
git merge <branch>

# merge specific file
git checkout <feature_branch> my_file1 my_file2
```

## Tag

```bash
# add tag
git tag <tag_name>

# use tag to archive
git tag archive/<branch_name> <branch_name>

# delete tag
git tag -d oldtag

# rename tag
git tag <new_tag> <old_tag>
git tag -d <old_tag>

# update an exsisting Tag
git tag -f <tag_name>
```

## Remote

```bash
# show remote url
git remote -v

# set remote url
git remote set-url <repo>
git remote set-url --add origin <repo>
git remote set-url --delete origin <repo>

# add to github
git remote add github <repo>
git push github master
git branch -u github/master master
git remote set-url origin <repo>
```

## Submodule

```bash
# add other project as submodule
git submodule add <repo> <submodule_path_or_local_dir_name>

# init submodule
git submodule init

# update submodule
git submodule update

# delete submodule
git submodule deinit <submodule_path_or_local_dir_name>
git rm <submodule_path_or_local_dir_name>
rm -rf .git/modules/<submodule_path_or_local_dir_name>
```

## Error

```bash
# error: The following untracked working tree files would be overwritten by checkout
git clean  -d  -fx ""

# error: you need to resolve your current index first
git reset —merge

# fatal: pathspec '...' did not match any files
# list all index
git ls-files

# re init repo
cat .git/config  # note <github-uri>
rm -rf .git
git init
git add .
git commit -m "Initial commit"
git remote add origin <github-uri>
git push -u --force origin master
```

## .gitconfig

```bash
# set email of a single respository
git config user.email "zhiyang.wang@nio.com"
```

```config
[push]
 	default = simple
[user]
	name = zhiyang.wang
	email = wzy816@gmail.com
[core]
    editor = vim
    compression = 0
[alias]
    l = log --oneline --decorate --graph --all
    l20 = log --oneline --decorate --graph -20

    s = status
    co = checkout
    a = add -A
    cm = commit -a -m
    cb = checkout -b
    d = branch -d
    pd = push origin --delete

    cf= config --global -e

    pl= pull origin HEAD
    ps= push origin HEAD
    pss= push --set-upstream origin HEAD

[color]
    ui = always
```
