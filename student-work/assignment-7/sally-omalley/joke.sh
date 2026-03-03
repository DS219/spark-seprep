JOKE=$(curl -sS https://icanhazdadjoke.com | tail -n 1)
#this file contains a joke and the comment explains that
echo "$JOKE"
echo
exit 0
