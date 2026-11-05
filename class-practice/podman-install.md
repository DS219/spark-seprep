# Class activity: Install Podman on Mac or Windows

**Time: about 20 minutes.** Do this **before class** if you can: it downloads about 1 GB.

[Podman](https://podman.io) runs **containers**: apps packaged with everything they
need, so they run the same on every computer. Containers are a Linux feature. On a
Mac or Windows laptop, Podman runs them inside a small Linux virtual machine called
a **Podman machine**. You install Podman, then create and start that machine once.

## What you need

| | Requirement |
| --- | --- |
| Mac | Apple Silicon (M1 or newer). Check Apple menu > About This Mac. |
| Windows | **Windows 11**, with permission to run commands as Administrator (needed once, for WSL). |
| Disk | About 5 GB free for the Podman machine and a few container images. |

If you already have Podman, check with `podman --version`. Version 6.0 or newer is fine:
skip to step 2.

## 1. Install Podman

Use the **official installer** from the Podman project. The Podman team
[recommends it over Homebrew](https://podman.io/docs/installation#macos), which is
community-maintained.

### Mac (Apple Silicon)

1. Download the installer:
   [podman-installer-macos-arm64.pkg](https://github.com/podman-container-tools/podman/releases/latest/download/podman-installer-macos-arm64.pkg)
2. Open the downloaded file and click through the installer. It asks for your Mac password.
3. **Close and reopen Terminal**, then check:

   ```bash
   podman --version
   ```

   You should see `podman version 6.` followed by more numbers.

> **Already installed Podman with Homebrew?** Keep it, or switch, but do not have
> both. With both installed, `which -a podman` lists two paths, and the one that
> runs depends on your PATH. To switch to the installer, run `brew uninstall podman` first.

### Windows

Podman on Windows runs its machine on **WSL 2**, Microsoft's built-in Linux support.
The Podman installer does **not** install WSL for you.

1. **Install WSL** (skip if `wsl --status` already works). Right-click **PowerShell**
   and choose **Run as administrator**, then run:

   ```powershell
   wsl --install
   ```

   Restart your computer when it asks.
2. **Download the Podman installer** for your processor. Most Windows laptops are
   `amd64`. Check in **Settings > System > About > System type**: "ARM-based processor"
   means `arm64`.
   - [podman-installer-windows-amd64.msi](https://github.com/podman-container-tools/podman/releases/latest/download/podman-installer-windows-amd64.msi)
   - [podman-installer-windows-arm64.msi](https://github.com/podman-container-tools/podman/releases/latest/download/podman-installer-windows-arm64.msi)
3. Run the installer. Keep the default **per-user** install (no administrator needed)
   and choose **WSL** when it asks for a virtualization provider.
4. Close and reopen **PowerShell** (a normal one, not Administrator), then check:

   ```powershell
   podman --version
   ```

**Checkpoint:** `podman --version` prints version 6 or newer.

## 2. Create and start the Podman machine (Mac and Windows)

```bash
podman machine init
podman machine start
```

`podman machine init` downloads the Linux virtual machine, so it takes a few minutes
the first time. You only run it once. Check that the machine is running:

```bash
podman machine list
```

The `LAST UP` column should say `Currently running`.

## 3. Run your first container

```bash
podman run --rm quay.io/podman/hello
```

Podman downloads a tiny image from the `quay.io` registry, runs it, and prints a
seal (the Podman mascot) with a hello message. `--rm` deletes the container when it
finishes.

**Checkpoint:** you see the hello message.

## 4. Commands you will use again

| Command | What it does |
| --- | --- |
| `podman machine start` | Start the Podman machine. Run this after you restart your laptop. |
| `podman machine stop` | Stop the machine and free its memory. |
| `podman ps` | List running containers. Add `-a` to include stopped ones. |
| `podman images` | List downloaded images. |
| `podman logs <name>` | Show what a container printed. |
| `podman rm -f <name>` | Stop and delete a container. |

Keep Podman installed: later activities use it. To remove the machine and free its
disk, run `podman machine rm`.

## If something goes wrong

| Symptom | Next step |
| --- | --- |
| `podman: command not found` | Close and reopen the terminal. On Mac, check `/opt/podman/bin/podman --version`. |
| Mac installer says the processor is not supported | Intel Macs are not supported in this class. Pair with a classmate. |
| `Cannot connect to Podman` | The machine is not running. Run `podman machine start`. |
| Windows: `podman machine init` says WSL is not installed | Run `wsl --install` in an Administrator PowerShell, restart, and try again. |
| Windows: errors about virtualization | Hardware virtualization is off in your laptop's firmware (BIOS/UEFI). Ask for help, or pair with a classmate. |
| `podman machine init` says a machine already exists | That is fine. Run `podman machine start`. |
| Download is very slow | Classroom Wi-Fi is shared. Do this at home, or pair with a classmate. |

Full upstream guides: [Podman installation](https://podman.io/docs/installation) and
[Podman for Windows](https://github.com/podman-container-tools/podman/blob/main/docs/tutorials/podman-for-windows.md).
