# Assignment 3

**Objective:**

This assignment aims to enhance your version control skills by guiding you through setting up GitHub repositories, creating files locally, and pushing the files to github.

**Instructions:**

**1. GitHub Repository Setup and Clone:**

   - Follow the instruction here https://github.com/DS219/github-fun/blob/master/1-repo.md to create a new repository if you did not already do so during class on February 4th.

**2. Create your File:**

   - Ensure that you are on your `main` branch `git checkout main`.
   - Create a new .txt file using any editor you like and call it `introduction.txt`.
   - Inside the file, add a few lines introducing yourself and what your favorite class has been so far at BU or any other fact you'd like to share publicly :)
   - Save the file.

**3. Push file to Github:**

Follow these steps to add, commit, and push your new file to your github repo.
    - First check the status of your git repository. This should show `introduction.txt` as untracked and red in color:
    ```
    git status
    ```
  - Add the file so that git can track it:
    ```
    git add introduction.txt
    ```
  - Check the status of your git repository again. This should now show `introduction.txt` as trcked and green in color:
    ```
    git status
    ```
  - Now commit the file so it can be added to your commit history:
    ```
    git commit -m "Add introduction.txt file"
    ```
  - Check the status of your git repository again. This should now show nothing new in your working tree as you have added and commited your new file:
    ```
    git status
    ```
  - Push the new chnges to your repository on github:
    ```
    git push origin main
    ```

**Submission:**

- Create and Push a file called `introduction.txt` to your github repository.
- Fill out form [https://forms.gle/J5RCDX5PJbgCVwKy6](https://forms.gle/jyDVodymhWZePjwM9) to submit your assignment.

If you have questions or need clarification, contact your instructor. Good luck and have fun!
