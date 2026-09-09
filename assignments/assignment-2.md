# Assignment 2: Your First Remote Linux Session

**Value:** 25 points
**Submit:** Use the Assignment 2 form linked in Blackboard.

In this assignment, you will use SSH to connect to your account on the class Linux VM, create a small record of your session, inspect and run a Bash script, and verify your work.

The VM address, temporary password, and verified host-key fingerprint are available in Blackboard. Do not post those details publicly.

> **Protect your private key.** Never paste, upload, email, or submit a file such as `id_ed25519`. The file ending in `.pub` is the public key.

Windows students should complete this assignment from WSL. macOS and Linux students should use their normal terminal.

## 1. Prepare SSH key access (5 points)

Check whether you already have an Ed25519 public key:

```bash
ls ~/.ssh/id_ed25519.pub
```

If the file does not exist, create a key pair:

```bash
ssh-keygen -t ed25519 -C "YOUR_BU_EMAIL"
```

Press `Enter` to accept the default file location. For this course exercise, press `Enter` again to leave the passphrase blank. This reduces setup friction, but it also means anyone who obtains your private key could use it. Never share or upload the private key.

Install **only your public key** on the class VM:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub YOUR_USERNAME@VM_ADDRESS
```

If `ssh-copy-id` is unavailable, use this fallback instead:

```bash
cat ~/.ssh/id_ed25519.pub | ssh YOUR_USERNAME@VM_ADDRESS 'umask 077; mkdir -p ~/.ssh; cat >> ~/.ssh/authorized_keys'
```

Use the temporary password from Blackboard when prompted. If SSH displays a host-authenticity warning, compare its fingerprint with the fingerprint in Blackboard. Continue only if they match.

## 2. Connect and orient yourself (5 points)

Connect to your account:

```bash
ssh -i ~/.ssh/id_ed25519 YOUR_USERNAME@VM_ADDRESS
```

Once connected, answer three questions:

```bash
whoami
pwd
ls
```

- Who am I?
- Where am I?
- What is here?

Your prompt and `whoami` output should contain your own username.

## 3. Create a record of your session (5 points)

Create a working directory and enter it:

```bash
mkdir -p ~/commandline-practice
cd ~/commandline-practice
```

Create `output.txt` and record some facts about the session:

```bash
date > output.txt
whoami >> output.txt
hostname >> output.txt
cat output.txt
```

Notice that `>` creates or replaces the file, while `>>` appends another line.

## 4. Inspect and run a Bash script (5 points)

Download the course's dad-joke script into your current directory:

```bash
curl -fL -o joke.sh https://raw.githubusercontent.com/DS219/spark-seprep/refs/heads/main/assignments/joke.sh
```

Inspect it **before** running it:

```bash
cat joke.sh
```

Make it executable, verify its permissions, and append its output to your session record:

```bash
chmod u+x joke.sh
ls -l joke.sh
./joke.sh >> output.txt
```

The joke service requires network access. If it is unavailable, the script prints a fallback joke so you can still complete the assignment.

## 5. Verify, explain, and submit (5 points)

Verify your final work:

```bash
pwd
ls -l
cat output.txt
```

Complete the Assignment 2 form in Blackboard. It will ask for:

1. the output of `whoami`, `pwd`, and `hostname`;
2. the permissions shown by `ls -l joke.sh`;
3. the final contents of `output.txt`;
4. the joke the script gave you, plus a short explanation of why you ran `./joke.sh` instead of `joke.sh`; and
5. one problem you encountered, or one step you verified carefully.

Do not submit your private key, public key, temporary password, or any passphrase.

When finished, leave the remote machine:

```bash
exit
```

## Grading

Each section is worth 5 points. Full credit reflects a genuine attempt with enough evidence to show that you completed and understood the workflow. If something fails, document the exact error and what you tried rather than hiding the problem.

Ask questions when you get stuck. Debugging is part of the assignment.
