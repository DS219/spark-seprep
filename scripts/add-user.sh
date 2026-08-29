#!/bin/bash

if [[ $# -ne 1 || -z "$1" ]]; then
    echo "Usage: $0 <initial-password>" >&2
    exit 1
fi

# Path to the file containing the user names
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
USER_LIST="$SCRIPT_DIR/userlist.txt"

# Initial password to set for all users
INITIAL_PASSWORD=$1

# Loop through each line in the file
while IFS= read -r user
do
    # Create a new user with a home directory
    sudo useradd -m "$user"

    # Set the initial password
    printf '%s:%s\n' "$user" "$INITIAL_PASSWORD" | sudo chpasswd

    # Create .ssh directory and set permissions
    sudo mkdir -p "/home/$user/.ssh"
    sudo chmod 700 "/home/$user/.ssh"
    sudo chown "$user:$user" "/home/$user/.ssh"

    # Informative output
    echo "Created user $user with initial password set."
done < "$USER_LIST"

echo "All specified users have been added."
