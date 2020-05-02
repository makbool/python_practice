# python_practice

GitHub

Repository hosting service

	Similar : BitBucket

Repository

	Place where we can save/maintain project source code

Branch

	Place where code actually resides

	master - default branch

	branch_a - add/modify

	branch_b - add/modify


Git

Source Control Management (SCM)	 tool




Untracked 

	New Files


Unstaged

	Modified but added to Stage


Staged

	Files which we want commit	



Git Commands

git clone

	copies remote repository to local machine


git checkout

	switch between branches

git status

	shows the current branch status including commits, staged, unstaged and untracked files

git add

	to move files from unstaged to staged

git rm

	to delete files

git commit -m "message"

	commits staged changes to branch in local repository


git push

	sends all the commits to branch in remote repository


git log
	
	displays the list of all commits

git log --one-line

git log --one-line --graph

git pull
	
	updates branch in local repo with the branch in remote repo along with other repo updates (new branches).
	Advanced (TBD) : Performs Fetch and Merge

branch origin vs branch HEAD

origin
	
	Last/Latest commit of the branch in local repo synced with remote repo. 

HEAD

	Top commit of the branch in local repo

----------------------------------------
Git merge 

Merging b2 to b1

git checkout b1

git merge --no-ff b2

git push

-----------------------------
Git rebase

switch to target branch

git rebase source-branch-name


---------------------------------

-------------------------------------------------
https://git-scm.com/

--------------------------------------------------


Python

print function

integers

floats

Operators 

<p>+ - * / // % **</p>

+=, -=,...

EDMAS

booleans

Comparison Operators >,<,>=, <=, ==,!=

strings

Read Inputs

converters

string functions

List [value,...]

Set {value,...}

Tuple (value,...)

Dictionary{key:value,....}
