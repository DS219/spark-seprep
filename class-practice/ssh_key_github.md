## SSH Key Generation and GitHub Setup for DS219

This exercise will show you how to generate an SSH key pair, add it to GitHub, and configure your Git settings with your global username and email.

### Part 1: Generating SSH Keys

1. **Open a Terminal**:  
   Start by opening your terminal application.

2. **Generate an SSH Key Pair**:  
   Use the `ssh-keygen` command to create a new SSH key pair. You will be prompted to enter a file path to save the key, and an optional passphrase for added security.
   Just hit enter to use the default path and leave the password blank (setting a password is not necessary).
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   - Replace `"your_email@example.com"` with your actual email address.
   - Press `Enter` to accept the default file location.
   - Press `Enter` to leave the password blank.

4. **View the Public Key**:  
   Display the contents of your public key using `cat`. This is the key that GitHub will use to authenticate your SSH connection.
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

### Part 2: Adding the SSH Key to GitHub

4. **Copy the Public Key**:  
   Select and copy the output from the previous command. This is your public SSH key.

5. **Log in to GitHub**:  
   Open your web browser and log in to your GitHub account.

6. **Navigate to SSH Keys Settings**:  
   Click on your profile picture in the upper right corner, then go to **Settings** > **SSH and GPG keys**.

7. **Add a New SSH Key**:  
   Click on **New SSH key**, provide a descriptive title (like `DS219 lab machine`), and paste your public key into the key field.

8. **Save the SSH Key**:  
   Click **Add SSH key** to save and apply the changes.

### Part 3: Configuring Git with Your Name and Email

9. **Configure Git Username and Email**:  
   Set your Git username and email globally. This information will be used in every Git repository you work on with this machine.
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"
   ```
   - Replace `"Your Name"` and `"your_email@example.com"` with your actual name and email.

### Part 4: Testing SSH Connection

10. **Test Your SSH Connection**:  
    Ensure that SSH can authenticate to GitHub correctly by running:
    ```bash
    ssh -T git@github.com
    ```
    - You should see a message saying that you've successfully authenticated but GitHub does not provide shell access.

### Part 5: Set SSH as Default for GitHub

11. **Set SSH as Default for GitHub**:  
    Configure Git to use SSH for GitHub operations by setting the global `git` configuration:
    ```bash
    git config --global url."git@github.com:".insteadOf "https://github.com/"
    ```
