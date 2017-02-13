#!/usr/bin/env bash

#First, create a chain of five commits on the branch master:
for i in 1 2 3 4 5
do
	touch $i
	git add $i
	git commit -m $i
done

#Then, create three new commits starting from the first commit, on a branch called feature:
git branch feature HEAD~4
git checkout feature

for j in 6 7 8
do
	touch $j
	git add $j
	git commit -m $j
done

#Then, move the commits 4 and 5 to the feature branch:
git checkout master
git rebase HEAD~2 --onto feature

#Create a new commit attached to commit 3 in a branch called debug.
git reflog
git checkout HEAD@{11}
touch 9
git add 9
git commit -m "9"
git branch debug

#Finally, change the content of commit “9” to include file “7”.
git checkout master 7
git add 7
git commit --amend --no-edit
