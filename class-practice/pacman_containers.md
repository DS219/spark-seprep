## Clone PacMan repository

```
cd ~/Desktop/github
git clone git@github.com:sallyom/mongo-pacman.git
cd mongo-pacman
```

## Build PacMan

```bash
cd frontend
podman build -t pacman:latest -f docker/Dockerfile .
cd ../
```

## Run the built image

Now run the newly built image. `--rm` ensures the container will be cleaned up after you stop the container.
Add the `-d` to run this container in the background.
With `-p 8080:8080` port-forward port 8080 from the running container to port 8080 on your local system.
Name your container `pacman` to easily view the logs.

```bash
podman run --rm -d --name pacman -p 8080:8080 pacman:latest
```

You can see the container logs by running:

```bash
$ podman logs pacman
NODE VERSION:
v18.14.2
NPM  VERSION:
9.5.0
run pacman
PACMAN auth_details =  pacman:pacman@
DATABASE URL  mongodb://pacman:pacman@mongodb:27017/pacman
CONNECTING  mongodb://pacman:pacman@mongodb:27017/pacman
Options  { readPreference: 'secondaryPreferred' }
Listening on port 8080
```

To play `PACMAN`, head to your browser at `http://localhost:8080`

* `EXTRA CREDIT`: Make a change (any change!) that is visible when the program is run. Build and push that image.

You can use Podman, Docker, or any other container build tool.

## Push the built image to docker hub

You can push the image built to your docker hub account if you want. Replace **<YOURUSERNAME>** with your docker hub username.

```
podman push pacman:latest docker.io/<YOURUSERNAME>/pacman:latest
```

**To clean up your system after running and building the pacman image (after you're done with the assignment):**

```bash
podman stop pacman
podman rmi localhost/pacman:latest
```

![pacman screen shot](./screenshot.png)
