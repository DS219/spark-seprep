## Fork, Clone, Add Remote

1. From any public repository (GH website) click the upper right `Fork` button.
    - A copy of `someones/cool-repository` will now be in GH at `yourname/cool-repository`

2. Go to GH `yourname/cool-repository` and from there, go to the green `Code` button to copy the git clone command.

3. Open a Terminal and clone your forked repository to create a local copy.
     
    ```bash
    cd /path/to/directory/with/github.com
    git clone <paste from 2. above>
    cd cool-repository
    ```

4. You now have a local copy of **your** fork of the cool-repository. You probably want to add a `git remote` to track the original `someones/cool-repository`.
     
    ```bash
    git remote -v
    # you should see 'origin' as 'git@github.com:yourname/cool-repository.git'
    # now add the 'upstream'
    git remote add upstream git@github.com:someones/cool-repository.git
    ```

5. Continuously keep _your_ local and remote `main` branch even with _someones_ `main` branch
     
    ```bash
    git checkout main
    git fetch --all
    git rebase upstream/main
    git push origin main
    ```

6. Open a new branch for local development

    ```bash
    git checkout -b new-branch
    ```

7. Add a new commit to the new-branch and push to **your fork** in GH

    ```bash
    # make changes
    git add .
    git commit -m "a new commit"
    git push origin new-branch
    ```

    - You might now visit GH to open a PR, comparing `yourname/new-branch` to `someones/main` 

8. You might want to clean up your branches!

    - To remove local development branch

    ```bash
    git branch -D new-branch
    ```

    - To remove development branch from **your fork** in GH

    ```bash
    git push origin :new-branch
    ```
**NOTE**
  `origin` is the default remote name given to a local clone, and `upstream` is my habit. You can update to anything with:

  ```bash
  git remote rename origin anything
  git remote rename current updated
  ```
