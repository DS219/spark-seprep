# GitHub Repository Setup and Clone

**Objective:**

This aims to enhance your version control skills by guiding you through setting up GitHub repositories, creating files locally, and pushing the files to github.

**Instructions:**

**1. GitHub Repository Setup and Clone:**

   - Follow the instruction here https://github.com/DS219/github-fun/blob/master/1-repo.md to create a new repository if you did not already do so.

**2. Create your File:**

   - Ensure that you are on your `main` branch `git checkout main`.
   - Create a new .txt file using any editor you like and call it `git-practice.md`.
   - Inside the file, add a few lines describing what we're doing in class today, or anything else you want to include. This will be pushed to GitHub so it will be visible to anyone who finds it :)
   - Save the file.

**3. Push file to Github:**

Follow these steps to add, commit, and push your new file to your github repo.
    - First check the status of your git repository. This should show `git-practice.md` as untracked and red in color:
    ```
    git status
    ```
  - Add the file so that git can track it:
    ```
    git add git-practice.md
    ```
  - Check the status of your git repository again. This should now show `introduction.txt` as trcked and green in color:
    ```
    git status
    ```
  - Now commit the file so it can be added to your commit history:
    ```
    git commit -m "Add git-practice.md file"
    ```
  - Check the status of your git repository again. This should now show nothing new in your working tree as you have added and commited your new file:
    ```
    git status
    ```
  - Push the new chnges to your repository on github:
    ```
    git push origin main
    ```

**Verify:**

- Check that a file called `git-practice.md` is visible in your github repository.

**Cleanup:**

- If you want to remove the test git repository you created, you can do so by going to the settings of your repository and scrolling down to the "Danger Zone" section. There you will find an option to delete the repository.
  Be careful, as this action is irreversible.

- If you want to remove the test git repository you cloned locally, you can do so by deleting the folder that contains the repository. You can do this using your file explorer or by running the following command in your terminal:

    ```
    rm -rf <repository-folder-name>
    ```
```
