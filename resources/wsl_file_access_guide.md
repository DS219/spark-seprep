# WSL File System Access Guide for Students

## Overview

Windows Subsystem for Linux (WSL) creates a bridge between your Windows system and Linux environment. This guide explains how to access files between both systems seamlessly.

## Accessing Windows Files from WSL

### Automatic Mount Points

WSL automatically mounts your Windows drives under the `/mnt/` directory. No additional setup required!

```bash
# Access your C: drive
cd /mnt/c/

# Access other drives (if available)
cd /mnt/d/
cd /mnt/e/
```

### Common Windows Locations

```bash
# Your user profile
cd /mnt/c/Users/YourUsername/

# Desktop files
cd /mnt/c/Users/YourUsername/Desktop/

# Documents folder
cd /mnt/c/Users/YourUsername/Documents/

# Downloads folder
cd /mnt/c/Users/YourUsername/Downloads/

# Quick tip: Use $USER variable for your username
cd /mnt/c/Users/$USER/Desktop/
```

### Working with Windows Files in WSL

```bash
# List files in your Windows Documents folder
ls /mnt/c/Users/$USER/Documents/

# Edit a Windows file using Linux text editors
nano /mnt/c/Users/$USER/Desktop/my-file.txt
vim /mnt/c/Users/$USER/Documents/homework.md

# Copy files from Windows to your WSL home directory
cp /mnt/c/Users/$USER/Downloads/project.zip ~/

# Copy files from WSL to Windows Desktop
cp ~/my-script.sh /mnt/c/Users/$USER/Desktop/
```

## Accessing WSL Files from Windows

### Method 1: File Explorer

1. Open Windows File Explorer
2. In the address bar, type: `\\wsl$`
3. Navigate to your Linux distribution (e.g., `Ubuntu`)
4. Browse to `/home/yourusername/` for your files

**Full path example:** `\\wsl$\Ubuntu\home\yourusername\`

### Method 2: Direct Path Access

You can also type the direct path in File Explorer:
```
\\wsl$\Ubuntu\home\yourusername\Documents\
\\wsl$\Ubuntu\home\yourusername\projects\
```

### Method 3: Command Prompt/PowerShell

From Windows Command Prompt or PowerShell:
```cmd
# Navigate to WSL files
cd \\wsl$\Ubuntu\home\yourusername\

# Copy files from WSL to Windows
copy \\wsl$\Ubuntu\home\yourusername\file.txt C:\Users\YourName\Desktop\
```

## Best Practices

### Performance Considerations

**For better performance:**
- Store files you'll primarily work with in Linux tools in the WSL filesystem (`~/`)
- Store files you'll primarily work with in Windows applications in the Windows filesystem (`/mnt/c/`)

**Example workflow:**
```bash
# Good: Working on a Python project primarily in WSL
mkdir ~/my-python-project
cd ~/my-python-project

# Good: Editing a Word document primarily in Windows
code /mnt/c/Users/$USER/Documents/report.docx
```

### File Permissions

When working with Windows files from WSL, you might encounter permission issues. If needed, you can modify the default mount behavior by editing `/etc/wsl.conf`:

```bash
sudo nano /etc/wsl.conf
```

Add these lines:
```ini
[automount]
root = /mnt/
options = "metadata,umask=22,fmask=11"
```

Restart WSL after making changes:
```cmd
# In Windows Command Prompt
wsl --shutdown
wsl
```

## Common Tasks and Examples

### Setting Up a Development Environment

```bash
# Create a projects folder in WSL
mkdir ~/projects
cd ~/projects

# Clone a repository
git clone https://github.com/username/repo.git

# Access from Windows: \\wsl$\Ubuntu\home\yourusername\projects\repo\
```

### Moving Files Between Systems

```bash
# Move a downloaded file from Windows Downloads to WSL
mv /mnt/c/Users/$USER/Downloads/dataset.csv ~/projects/data-analysis/

# Copy your WSL project to Windows for backup
cp -r ~/my-project /mnt/c/Users/$USER/Desktop/project-backup/
```

### Working with Different File Types

```bash
# Edit code files (works great from either location)
code /mnt/c/Users/$USER/Desktop/website/index.html
nano ~/scripts/backup.sh

# Process data files
python ~/analysis.py --input /mnt/c/Users/$USER/Documents/data.csv
```

## Troubleshooting

### Common Issues

**Can't find your files?**
- Double-check the path: `/mnt/c/Users/YourActualUsername/`
- Use `ls /mnt/c/Users/` to see available usernames

**Permission denied errors?**
- Try copying the file to your WSL home directory first
- Check if the file is currently open in a Windows application

**Performance is slow?**
- Consider moving frequently-accessed files to the WSL filesystem
- Use native Linux tools for files stored in WSL, Windows tools for files stored in Windows

### Quick Commands Reference

```bash
# Check your current location
pwd

# See what drives are mounted
ls /mnt/

# Navigate to Windows user folder quickly
cd /mnt/c/Users/$USER/

# Go to WSL home directory
cd ~
# or
cd /home/$USER/

# List all files including hidden ones
ls -la
```

## Tips for Students

1. **Organize your work:** Keep school projects in clearly named folders
2. **Use version control:** Consider using git for important projects
3. **Regular backups:** Copy important work between systems for redundancy
4. **Learn both paths:** Understand how to access files from both Windows and WSL perspectives
5. **Use appropriate tools:** Use Linux command-line tools for development, Windows applications for documents and presentations

## Getting Help

If you encounter issues:
- Use `man` command for help with Linux commands: `man cp`
- Check WSL documentation: `wsl --help`
- Restart WSL if you encounter persistent issues: `wsl --shutdown` then `wsl`

Remember: The file systems are interconnected, so changes made in one environment are immediately visible in the other!