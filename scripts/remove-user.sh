while read -r username; do
  sudo userdel -r "$username"
done < userlist-old.txt
