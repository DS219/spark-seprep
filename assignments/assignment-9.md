# Assignment 9: Containerization of Jupyter Notebooks

## Overview
Building on your work from **Assignment 8**, this assignment requires you to create a container image of your Jupyter notebook environment. This will help ensure that your notebook can be run by anyone else without any issues related to dependencies or environment setups. Additionally, you will engage in a peer review process to validate the reproducibility of other students' notebooks.

## Prerequisite

Ensure that you are up to date with the upstream Github repo. Do the following before starting your assignment. Make sure to switch to the branch you used for assignment 8.

```
cd <to your github repo path>
git checkout assignment-8-branch
git fetch upstream
git rebase upstream/main
```

## Objectives
1. **Create a Container Image**: Package your Jupyter notebook into a container that can be easily run by others.
2. **Peer Review**: Review the notebooks of two peers by running their container images and providing feedback on both logical and technical aspects.

### Part 1: Create Container Image
You are tasked with creating a container that encapsulates your Jupyter notebook environment from Assignment 8. Follow the instructions below to write a containerfile to create this container image.

#### Containerfile Instructions
Create a `Containerfile` with configuration similar to this:

```Dockerfile
FROM python:latest
WORKDIR /opt/app-root/bin
RUN pip install --upgrade jupyterlab 
WORKDIR /opt/app-root/src
CMD ["jupyter", "lab", "--port=8888", "--allow_origin=*", "--ip="]
```

Note: Make sure the port you are setting in CMD matches the port needed by your Jupyter notebook. You will also need to add a **requirements.txt** file during the image build process to install any requirements that your Jupyter notebook has.

Note: The containerfile shared above is just an example of what you might need and is not necessrily complete. You might have to add more lines in there based on what your Jupyter notebook needs. Google is your friend, google if you run into issues!

### Build and Run Your Container:
* Build your container image using:
```bash
podman build -t nb .
```
* Run your container to ensure that it is running as expected:
```bash
podman run -p 8888:8888 localhost/nb
```
Adjust the port settings as necessary, ensuring they are also adjusted in the port forwarding settings.

#### Additional Resources
For more configurations on the Jupyter server, refer to the Jupyter Server Configuration documentation https://jupyter-server.readthedocs.io/en/latest.

### Part 2: Peer Review

After the submission deadline for Assignment 8:
1.	Visit DS219/spark-seprep Pull Requests.
2.	Select **two** pull requests submitted for Assignment 8.
3.	Conduct your review focusing on:
  * **Logical Changes:** Comment on the logic and methodologies used in the notebooks.
  * **Technical Execution:** Attempt to pull and run the container images. Provide feedback on whether you could successfully execute the notebooks end-to-end.

#### Comment with Container Link and PRs reviewed:
1. Once you have created your container image, push it Docker hub and comment on your original PR for Assignment 8 with the link to your container image to facilitate the review process.
```bash
podman push [image-name] [docker.io/username/image-name]
```
2. Add another comment in your PR with links to the **two PRs** that you have reviewed.

##### Note:
Continue pushing to the same **assignment-8-branch** and add **one** addiitional commit with your Containerfile to the same PR as Assignment 8. This will consolidate all related work in a single pull request for ease of assessment and review.

Once you have added your Containerfile in **student-work/assignment-8/your-name**. Add, commit, and push to the same branch and your PR will automatically be updated.
```bash
git add Containerfile
git commit -m "Your message"
git push -u origin assignment-8-branch
```

**Grading Rubric:**
- **Two** PRs reviewed (4 pts)
- Comment with link to **Two** PRs reviewed (2 pts)
- Comment with link to container image you built (2 pts)
- Container image built runs successfully (2 pts)
- Containerfile syntax and format is correct (2 pts)
- Containerfile only has exactly what your script needs to run i.e no extra packages and files installed (2 pts)
- Descriptive and clear commit message (2 pts)
- Only 2 commits in your PR (2 pts)
- No extra junk files in PR (2 pts)
- Changes should be done on the assignment branch and not on main (2 pts)
- No modifications to any other files in the repo (2 pts)
