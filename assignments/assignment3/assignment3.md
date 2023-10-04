**Assignment: Collaborative GitHub Project - Creating Team Repositories**

**Objective:**
In this assignment, you will work collaboratively with your assigned teammate to set up GitHub repositories, create folders, submit pull requests to each other's forks, and establish upstream repositories for P1 and P2. The aim is to enhance your version control skills and teamwork.

**Instructions:**

**1. Team Pairings:**
   - Instructors have already assigned pairs for all students, resulting in a total of 15 teams for this assignment.
   - Each team member will be designated as either P1 or P2.

**2. GitHub Repository Setup:**
   - We will be working within the `DS219/spark-seprep/assignments/assignment3` directory structure on GitHub.

**3. Forking the Main Repository:**
   - Both P1 and P2 should create a fork of the `DS219/spark-seprep` repository.

**4. Folder Creation:**
   - After forking the repository, P2 will create a folder in `assignments/assignment3` with the following nomenclature: `<Team Number>_<Teammate 1 Name>_<Teammate 2 Name>`. For example, if your team number is 3 and the teammates are Alice and Bob, the folder name would be `Team3_Alice_Bob`.
   - Inside this folder, P2 should add a new document named `<Their Name>.md`.

**5. Upstream Repository Setup:**
   - After forking the repository, establish upstream repositories for both P1 and P2 to facilitate collaboration.

**For P1's Upstream Repository (Pointing to P2's Fork):**
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to work on your local repository, or create a new directory if needed.
3. Use the following command to add a remote named "upstream" that points to your teammate P2's fork:
   ```bash
   git remote add partner_upstream https://github.com/Teammate_P2_username/repository_name.git
   ```
   Replace `Teammate_P2_username` with P2's GitHub username and `repository_name` with the name of P2's forked repository.
4. Verify that the upstream repository has been added correctly by running:
   ```bash
   git remote -v
   ```
   You should see "partner_upstream" listed as a remote with the URL pointing to P2's fork.

**6. Initial Pull Request (PR) to P1's Fork:**
   - Do 
```
git status #to see your changes
git add . # to add all changes
git commit -m "Message goes here"
git push origin main
```
   - Go to UI and you will see your fork one commit ahead of upstream.
   - P2 will initiate the collaboration by submitting a pull request to P1's fork (P1's upstream repository).
   - P1 should review P2's pull request and merge it into their fork.

**7. Document Addition by P1:**
   - With the folder structure in place, P1 will now add a new document to the team folder named `<Their Name>.md`. For instance, if P1 is Alice, the document should be named `Alice.md`.
   - After creating the document, P1 will submit a pull request to P2's fork (P2's upstream repository).

**For P2's Upstream Repository (Pointing to P1's Fork):**
1. Follow the same steps as described in P1's upstream repository setup, but replace P1's fork with P2's fork when adding the upstream remote and URL.

**8. Final PR to Main Upstream:**
   - To complete the process, P2 will submit a pull request to the main upstream repository (`DS219/spark-seprep`) containing the changes to `assignments/assignment3` made by both teammates.

**9. Adding a PR to Somebody's Fork:**
   - As part of the collaboration, both P1 and P2 should become familiar with submitting pull requests to each other's forks. This process allows for reviewing and merging changes within the team.

**Important Notes:**
- Make sure to maintain clear and descriptive commit messages.
- Communicate effectively with your teammate to coordinate the process.
- Review each other's work thoroughly during the pull request phase.
- If you encounter any issues or have questions, don't hesitate to seek assistance from your instructor.

**Submission:**
- This assignment involves a series of pull requests within the GitHub repository.
- Ensure that all steps are completed, including setting up upstream repositories for P1 and P2, and that the final pull request to the main upstream repository is made.

This assignment not only helps you practice GitHub collaboration but also emphasizes effective communication and teamwork. If you have any questions or need clarification on any step, please reach out to your instructor. Good luck, and happy collaborating!
