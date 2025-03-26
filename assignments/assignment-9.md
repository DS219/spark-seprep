# Assignment 9: Containerization of Jupyter Notebooks

## Overview
Building on your work from Assignment 8, this assignment requires you to create a container image of your Jupyter notebook environment. This will help ensure that your notebook can be run by anyone else without any issues related to dependencies or environment setups. Additionally, you will engage in a peer review process to validate the reproducibility of other students' notebooks.

## Objectives
1. **Create a Container Image**: Package your Jupyter notebook into a Docker container that can be easily run by others.
2. **Peer Review**: Review the notebooks of two peers by running their containers and providing feedback on both logical and technical aspects.

### Part 1: Create Container Image
You are tasked with creating a Docker container that encapsulates your Jupyter notebook environment from Assignment 8. Follow the instructions below to create a basic Docker container.

#### Dockerfile Instructions
Create a `Dockerfile` with the following configuration:

```Dockerfile
FROM registry.access.redhat.com/ubi9/python-311:latest
WORKDIR /opt/app-root/bin
RUN pip install --upgrade jupyterlab 
WORKDIR /opt/app-root/src
CMD ["jupyter", "lab", "--port=8888", "--allow_origin=*", "--ip="]
```

### Build and Run Your Container:
* Build your container image using:
```bash
podman build -t nb .
```
* Run your container using:
```bash
podman run -p 8888:8888 localhost/nb
```

Adjust the port settings as necessary, ensuring they are also adjusted in the port forwarding settings.

#### Additional Resources
For more configurations on the Jupyter server, refer to the Jupyter Server Configuration documentation.

### Part 2: Peer Review

After the submission deadline for Assignment 8:
1.	Visit DS219/spark-seprep Pull Requests.
2.	Select two pull requests submitted for Assignment 8.
3.	Conduct your review focusing on:
  * **Logical Changes:** Comment on the logic and methodologies used in the notebooks.
  * **Technical Execution:** Attempt to pull and run the container images. Provide feedback on whether you could successfully execute the notebooks end-to-end.

#### Comment with Container Link:
Once you have created your Docker container, comment on your original PR for Assignment 8 with the link to your container image to facilitate the review process.

##### Note:
Continue pushing to the same assignment-8 branch and add additional commits to the same PR as Assignment 8. This will consolidate all related work in a single pull request for ease of assessment and review.
