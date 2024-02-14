# Assignment 4 - Collaborative GitHub Project - Creating Team PRs

## Objective:

Enhance version control skills and teamwork by collaborating with assigned teammates to set up GitHub repositories, create folders, submit pull requests, and establish upstream repositories for P1 and P2.

## Instructions:

### 1. Team Pairings:

- Instructors have assigned pairs for all students, resulting in 15 teams for this assignment.
- Each team member is designated as either `P1` or `P2`.

### 2. GitHub Repository Setup:

- Work within the `DS219/spark-seprep/assignments/assignment4` directory structure on GitHub.

### 3. Update your local main branch:

- Ensure your local main branch is in sync with upstream/main before starting any new work.

```bash
git fetch --all
git rebase upstream/main
git push origin main
```

### 4. Set Up Upstream Repository for P1 (Pointing to P2's Fork):

- Open your terminal or command prompt.
- Navigate to the directory where you want to work on your local repository, or create a new directory if needed.
- Use the following command to add a remote named **p2_upstream** that points to your teammate P2's fork:

   ```bash
   git remote add p2_upstream https://github.com/Teammate_P2_username/spark-seprep.git
   ```

   Replace Teammate_P2_username with P2's GitHub username.
   
- Verify that the upstream repository has been added correctly:

   ```bash
   git remote -v
   ```

   You should see **p2_upstream** listed as a remote with the URL pointing to P2's fork.

### 5. Initiate PR to P2's fork:

- With the folder structure in place, P1 will add a new document to the team folder named `<Their Name>.md`. For instance, if P1 is Alice, the document should be named `Alice.md`.
- After creating the document, P1 will submit a pull request to P2's fork (P2's upstream repository).

### 6. P2 reviews and merges P1's PR on their fork:

- P2 should check if P1 has correctly created the folder with the suggested nomenclature.
- Once everything looks good, merge the PR.

### 7. Set Up Upstream Repository for P2 (Pointing to P1's Fork):

- Using the instructions in Step 6, P2 repeats the step to create an upstream pointing to P1's fork.

### 8. P2 initiates Pull Request (PR) to P1's Fork:

- Follow the same steps as described in P1's upstream repository setup, but replace P1's fork with P2's fork when adding the upstream remote and URL.
-  P2 will initiate the collaboration by submitting a pull request to P1's fork (P1's upstream repository).
-  P1 should review P2's pull request and merge it into their fork.

### 9. Final PR to Main Upstream:

- To complete the process, P1 will submit a pull request to the main upstream repository (`DS219/spark-seprep/assignments/assignment4`) containing the changes made by both teammates.

## Important Notes:

- Maintain clear and descriptive commit messages.
- Communicate effectively with your teammate to coordinate the process.
- Review each other's work thoroughly during the pull request phase.
- If you encounter any issues or have questions, seek assistance from your instructor.

## Submission:

- This assignment involves a series of pull requests within the GitHub repository.
- Ensure that all steps are completed, including setting up upstream repositories for P1 and P2, and that the final pull request to the main upstream repository is made.

This assignment not only helps you practice GitHub collaboration but also emphasizes effective communication and teamwork. If you have any questions or need clarification on any step, please reach out to on piazza. Good luck, and happy collaborating!
