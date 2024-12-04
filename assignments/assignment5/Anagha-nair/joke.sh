#!/bin/sh
echo "What do you call a fake noodle? An impasta."
JOKE=$(curl -sS https://icanhazdadjoke.com | tail -n 1)
echo "$JOKE"
exit 0

