## Prerequisite

Ensure that you are up to date with the upstream Github repo. Do the following before starting your assignment.

```
cd <to your github repo path>
git checkout main
git fetch upstream
git rebase upstream/main
# If there are any issues, if rebase doesn't complete, then:
# git rebase --abort
# git reset --hard upstream/main <- CAUTION: This will remove any current work in your main branch 
git checkout -b assignment-7 upstream/main
```

## Write a Script or Program

Write a script or a program that gives you an output - it can be anything! You can write it in python, bash, C, Go etc.
We just want something that gives us an output that runs, but feel free to go all out and create something amazing!

You can also use the python script you wrote when solving the Leetcode problem from the last assignment. Just update it to give you an output.

## Create a Containerfile

Head to the directory **student-work/assignment-7** and create a directory there with your name in the format **FIRSTNAME-LASTNAME**.
The directory should be **student-work/assignment-7/[FIRSTNAME-LASTNAME]** so you can add your Containerfile and script there.

```bash
cd student-work/assignment-7
mkdir FIRSTNAME-LASTNAME
cd FIRSTNAME-LASTNAME
# Add your Containerfile and your script to this directory
```

Create a Containerfile to package the script you just wrote. Set the **CMD** of your container image to call your executable file.

```
...
CMD ./path/to/your/executable
...
```

This is what an example Containerfile looks like

```
FROM alpine
COPY joke.sh .
RUN chmod +x joke.sh
RUN apk add curl
CMD ./joke.sh
```
Head to https://docs.docker.com/get-started/02_our_app/ for a quick tutorial on Containerfiles/Dockerfiles. Google is your friend, use it!

Look at [https://github.com/DS219/spark-seprep/tree/main/student-work/assignment-7/sally-omalley](https://github.com/DS219/spark-seprep/tree/main/student-work/assignment-7/sally-omalley) as an example!
Do not use the exact same script and Containerfile for your assignment, you will not get any points if you do!

## Build and tag your container image

```
cd student-work/assignment-7/[FIRSTNAME-LASTNAME]
podman build -t [image-name] .
```

## Create a free account on Docker hub if you don't already have one

Head to Docker hub (https://hub.docker.com/) and create a free account there. Make sure to remember your username and password!
Create a Personal Access Token for pushing images to your account. See Piazza announcement for how to do this.

## Push the built container image to your docker hub account

Login to the docker hub account you created above with podman and enter the username and token when prompted.
```
podman login docker.io -u your-dockerhub-username
# You will be prompted to provide your password. Paste your token as the password.
```

Now you can push the image you built to your docker hub account.
```
podman push [image-name] docker.io/[username]/[image-name]
```

Make sure to run your container image with podman to ensure it runs successfully!
```
podman run [image-name]
```
If your script is interactive and requires user input, you need to enable the interactive and tty flags so you are able to send this input to the container. Use this command to run your container instead:
```
podman run -it [image-name]
```

## Run a classmate's container image locally

Look through [this spreadsheet](https://docs.google.com/spreadsheets/d/1ZJRSFowp34LuONBqZ_ZYOvciuap3u3NWkdQ2GSzIXwg/edit?usp=sharing) and pick a container image that one of your classmate's built. Choose an image that was built on the same Operating System
as yours. When you fill out the form below, your image will also be listed, so your classmates can choose to try your image. Pull down your classmate's image and run it locally on your machine.

```
podman pull [classmate-image]
podman run [classmate-image]
```

Answer the questions in this [form](https://forms.gle/FpQiqsKitC6dNr7C6) and hit submit! Your response will be viewable to the class, this populates the spreadsheet above from which you choose your classmates' images to try out.

## Create a Pull Request

**Note:** Always check the files that you are comitting in your working tree before actually comitting. For this assignment, you only need 2
files - your Containerfile and your script. Do not commit any extra files. The following command will show you your working tree always.
```
git status
```

Then:

```bash
git add student-work/assignment-7/FIRSTNAME-LASTNAME
git commit -m "This is my assignment 7. I've added a Containerfile and a script"
git push origin assigment-7
# Go to GitHub and open a PR
```

**Grading Rubric:**
- Answered form questions (4 pts)
- Container image built runs successfully (2 pts)
- Containerfile syntax and format is correct (2 pts)
- Containerfile only has exactly what your script needs to run i.e no extra packages and files installed (2 pts)
- Descriptive and clear commit message (2 pts)
- Only 1 commit in your PR (2 pts)
- No extra junk files in PR (2 pts)
- Changes should be done on the assignment branch and not on main (2 pts)
- No modifications to any other files in the repo (2 pts)
