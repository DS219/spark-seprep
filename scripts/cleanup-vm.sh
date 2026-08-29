#!/bin/bash

# Script to remove all users except 'somalley' and 'fedora' from the system
# Use with caution - this will permanently delete user accounts and home directories

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Class VM User Cleanup Script${NC}"
echo "This script will remove ALL users except 'somalley' and 'fedora'"
echo

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}Error: This script must be run as root (use sudo)${NC}"
   exit 1
fi

# Confirm before proceeding
echo -e "${RED}WARNING: This will permanently delete all user accounts and home directories except 'somalley' and 'fedora' ${NC}"
read -p "Are you sure you want to proceed? (type 'YES' to confirm): " confirm

if [[ "$confirm" != "YES" ]]; then
    echo "Operation cancelled."
    exit 0
fi

echo
echo "Starting user cleanup..."

# Get list of all users with UID >= 1000 (regular users) except somalley
users_to_remove=$(awk -F: '$3 >= 1000 && $1 != "somalley" && $1 != "fedora" && $1 != "nobody" {print $1}' /etc/passwd)

if [[ -z "$users_to_remove" ]]; then
    echo -e "${GREEN}No users to remove (only somalley fedora and system users found)${NC}"
    exit 0
fi

echo "Users to be removed:"
echo "$users_to_remove"
echo

# Final confirmation
read -p "Proceed with removing these users? (y/N): " final_confirm
if [[ "$final_confirm" != "y" && "$final_confirm" != "Y" ]]; then
    echo "Operation cancelled."
    exit 0
fi

echo
removed_count=0

# Remove each user
for user in $users_to_remove; do
    echo -e "Removing user: ${YELLOW}$user${NC}"

    # Kill any processes owned by the user
    if pgrep -u "$user" > /dev/null 2>&1; then
        echo "  Killing processes owned by $user..."
        pkill -u "$user" || true
        sleep 1
        # Force kill if needed
        pkill -9 -u "$user" || true
    fi

    # Remove the user and their home directory
    if userdel -r "$user" 2>/dev/null; then
        echo -e "  ${GREEN}Successfully removed $user${NC}"
        ((removed_count += 1))
    else
        echo -e "  ${RED}Failed to remove $user${NC}"
        # Try without removing home directory
        if userdel "$user" 2>/dev/null; then
            echo -e "  ${YELLOW}Removed $user account (home directory may remain)${NC}"
            ((removed_count += 1))
        fi
    fi
done

echo
echo -e "${GREEN}Cleanup complete!${NC}"
echo "Removed $removed_count users"
echo "Remaining user accounts:"
awk -F: '$3 >= 1000 {print "  " $1}' /etc/passwd

# Optional: Clean up any remaining home directories
echo
read -p "Clean up any orphaned home directories? (y/N): " cleanup_homes
if [[ "$cleanup_homes" == "y" || "$cleanup_homes" == "Y" ]]; then
    echo "Checking for orphaned home directories..."
    for homedir in /home/*; do
        if [[ -d "$homedir" ]]; then
            username=$(basename "$homedir")
            if [[ "$username" != "somalley" ]] && ! id "$username" >/dev/null 2>&1; then
                echo -e "Found orphaned directory: ${YELLOW}$homedir${NC}"
                read -p "Remove $homedir? (y/N): " remove_dir
                if [[ "$remove_dir" == "y" || "$remove_dir" == "Y" ]]; then
                    rm -rf "$homedir"
                    echo -e "  ${GREEN}Removed $homedir${NC}"
                fi
            fi
        fi
    done
fi

echo -e "${GREEN}User cleanup script finished!${NC}"
