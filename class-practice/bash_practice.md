## Bash Practice for DS219

This exercise focuses on basic file and directory management, using a text editor, script execution, and essential file operations such as moving, copying, and removing files in the Bash shell.

### Part 1: Working with Directories and Files

1. **Create a New Directory**:  
   Create a directory named `ds219` on your Desktop.
   ```bash
   mkdir ~/Desktop/ds219
   ```

2. **Change Directory and Verify Location**:  
   Navigate to the `ds219` directory and confirm your current directory.
   ```bash
   cd ~/Desktop/ds219/
   pwd
   ```

3. **List Directory Contents**:  
   Show the contents of the current directory.
   ```bash
   ls -l
   ```

### Part 2: File Creation and Editing with `vi`

4. **Create and Edit a File using `vi`**:  
   Open `file1.txt` in `vi`, type some text, and save the file.
   ```bash
   vi file1.txt
   ```
   - In `vi`, type `i` to enter insert mode, write your text, press `Esc` to exit insert mode, and type `:wq` to save and quit.

5. **View File Contents with `cat`**:  
   Display the content of `file1.txt`.
   ```bash
   cat file1.txt
   ```

### Part 3: Script Writing and Execution

6. **Create a Script File**:  
   Create `myscript.sh`, make it executable, and edit it to perform an HTTP header check.
   ```bash
   touch myscript.sh
   chmod +x myscript.sh
   vi myscript.sh
   # In vi, add:
   #!/bin/sh
   curl https://raw.githubusercontent.com/DS219/spark-seprep/refs/heads/main/LICENSE
   ```

7. **Execute the Script**:  
   Execute the script and review the file permissions.
   ```bash
   ./myscript.sh
   ```

### Part 4: File Manipulation

8. **Rename a File with `mv`**:  
   Rename `file1.txt` to `newfile1.txt`.
   ```bash
   mv file1.txt newfile1.txt
   ```

9. **Copy a File with `cp`**:  
   Copy `newfile1.txt` to create a duplicate file named `copy_of_file1.txt`.
   ```bash
   cp newfile1.txt copy_of_file1.txt
   ```

10. **Using `less` to View Files**:  
    View the contents of `myscript.sh` using `less`.
    ```bash
    less myscript.sh
    ```

11. **Search Within Files Using `grep`**:  
    Search for 'curl' in `myscript.sh`.
    ```bash
    grep 'curl' myscript.sh
    ```

### Part 5: Safe File Removal

12. **Demonstrate Safe Removal with `rm`**:  
    Explain the risks of `rm` and practice safe removal techniques.
    - Request confirmation before removing `newfile1.txt`:
      ```bash
      rm -i newfile1.txt
      ```
    - List `.txt` files and remove them safely:
      ```bash
      ls *.txt
      rm -i *.txt
      ```

### Part 6: Clean Up

13. **Remove Temporary Files**:  
    Remove any remaining files to clean up the workspace.
    ```bash
    rm -i ~/Desktop/ds219/*
    ```
