### Git Exercises for College Students

#### Exercise 1: Initializing a Repository

1. **Description:** Initialize a new Git repository and create a `Readme.md` file.

2. **Steps:**
   - Open your terminal.
   - Navigate to the desired directory for your project.
   - Run the following commands:
     ```bash
     git init
     echo "# My Project" > Readme.md
     git add Readme.md
     git commit -m "Initial commit: Add Readme.md"
     ```

#### Exercise 2: Making Changes

1. **Description:** Make changes to the `Readme.md` file and commit them.

2. **Steps:**
   - Open `Readme.md` in your preferred text editor.
   - Add some text or make modifications to the file.
   - Save the changes.
   - Run the following commands:
     ```bash
     git add Readme.md
     git commit -m "Update Readme.md: Add project description"
     ```

#### Exercise 3: Viewing Changes

1. **Description:** View the differences between commits.

2. **Steps:**
   - Make additional changes to the `Readme.md` file.
   - Save the changes.
   - Run the following command to view the differences:
     ```bash
     git diff
     ```

#### Exercise 4: Branching

1. **Description:** Create a new branch and switch to it.

2. **Steps:**
   - Run the following commands:
     ```bash
     git branch feature
     git checkout feature
     ```
   - Make changes to the `Readme.md` file within the `feature` branch.
   - Add and commit the changes.

#### Exercise 5: Merging

1. **Description:** Merge changes from the `feature` branch into the `main` branch.

2. **Steps:**
   - Switch back to the `main` branch:
     ```bash
     git checkout main
     ```
   - Merge changes from the `feature` branch:
     ```bash
     git merge feature
     ```

#### Exercise 6: Resolving Conflicts

1. **Description:** Simulate a merge conflict and resolve it.

2. **Steps:**
   - Make conflicting changes to the `Readme.md` file in both the `main` and `feature` branches.
   - Attempt to merge the `feature` branch into `main`:
     ```bash
     git merge feature
     ```
   - Resolve the conflicts in the file.
   - Add and commit the resolved file.

#### Exercise 7: Remote Repositories

1. **Description:** Connect your local repository to a remote repository on GitHub.

2. **Steps:**
   - Create a new repository on GitHub.
   - Follow the instructions on GitHub to add the remote repository URL to your local repository.
   - Push your local changes to the remote repository:
     ```bash
     git push origin main
     ```

#### Exercise 8: Cloning

1. **Description:** Clone a repository from GitHub to your local machine.

2. **Steps:**
   - Find a repository on GitHub that you want to clone.
   - Copy the repository URL.
   - Open your terminal and navigate to the directory where you want to clone the repository.
   - Run the following command:
     ```bash
     git clone <repository_url>
     ```

#### Exercise 9: Pulling Changes

1. **Description:** Fetch and merge changes from a remote repository.

2. **Steps:**
   - Navigate to your local repository.
   - Run the following command to fetch and merge changes from the remote repository:
     ```bash
     git pull origin main
     ```

#### Exercise 10: Collaboration

1. **Description:** Collaborate with a classmate on a Git repository.

2. **Steps:**
   - Find a classmate to collaborate with.
   - Add them as a collaborator on your GitHub repository.
   - Have your classmate clone the repository to their local machine.
   - Make changes to the repository and push them to GitHub.
   - Fetch and merge their changes into your local repository.

#### Exercise 11: Undoing Changes

1. **Description:** Undo changes made to a file and discard them.

2. **Steps:**
   - Make changes to the `Readme.md` file.
   - Run the following command to discard the changes and revert to the last committed state:
     ```bash
     git checkout -- Readme.md
     ```

#### Exercise 12: Stashing Changes

1. **Description:** Temporarily store changes to work on something else.

2. **Steps:**
   - Make changes to the `Readme.md` file.
   - Run the following command to stash the changes:
     ```bash
     git stash
     ```
   - Make additional changes or switch branches.
   - Retrieve the stashed changes:
     ```bash
     git stash pop
     ```

#### Exercise 13: Rebasing

1. **Description:** Reapply commits on top of another branch.

2. **Steps:**
   - Create a new branch:
     ```bash
     git branch experiment
     git checkout experiment
     ```
   - Make changes and commit them.
   - Switch back to the `main` branch:
     ```bash
     git checkout main
     ```
   - Run the following command to rebase the `experiment` branch onto `main`:
     ```bash
     git rebase experiment
     ```

#### Exercise 14: Viewing History

1. **Description:** View commit history and explore different options.

2. **Steps:**
   - Run the following command to view commit history:
     ```bash
     git log
     ```
   - Explore different options such as formatting, filtering by author, date range, etc.

#### Exercise 15: Tagging Releases

1. **Description:** Tag a specific commit as a release.

2. **Steps:**
   - Identify the commit you want to tag:
     ```bash
     git log
     ```
   - Run the following command to tag the commit:
     ```bash
     git tag v1.0 <commit_id>
     ```
   - Push the tag to the remote repository:
     ```bash
     git push origin v1.0
     ```

#### Exercise 16: Collaborative Workflow

1. **Description:** Simulate a typical collaborative workflow with branching and merging.

2. **Steps:**
   - Divide into pairs (A and B).
   - A creates a new branch, makes changes, and commits them.
   - A pushes the branch to the remote repository.
   - B pulls the branch, reviews the changes, and merges them into the `main` branch.
   - Switch roles and repeat the process.

#### Exercise 17: Gitignore

1. **Description:** Ignore certain files or directories from version control.

2. **Steps:**
   - Create a `.gitignore` file in the root of your repository.
   - Add file patterns or directory names to ignore.
   - Commit the `.gitignore` file.
   - Verify that ignored files are not included in Git's tracking.

#### Exercise 18: Git Hooks

1. **Description:** Automate tasks with Git hooks.

2. **Steps:**
   - Create a Git hook script (e.g., pre-commit, post-commit) in the `.git/hooks` directory of your repository.
   - Add desired commands or scripts to the hook.
   - Make changes and commit to trigger the hook.
   - Verify that the hook executes the specified tasks.
