#!/bin/sh
printf "Pick a number from 1 to 4 and press Enter to see your fortune : "
read -r choice
case "$choice" in
  1) echo "Good things are coming your way. Keep your eyes open." ;;
  2) echo "Good luck is on its way. Say yes to the next opportunity." ;;
  3) echo "You'll score higher than you expected. Trust what you studied." ;;
  4) echo "You'll bump into your crush soon. Look up from your phone!" ;;
  *) echo "That's not a number from 1 to 4. Run the container again and try once more." ;;
esac