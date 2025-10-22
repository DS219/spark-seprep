#!/bin/bash

# A simple script to check the day and offer a small piece of advice.

# Define a color for output
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get the current day of the week (e.g., 'Mon', 'Tue')
CURRENT_DAY=$(date +%a)

# Print the date and time
echo -e "${BLUE}*** System Status Check ***${NC}"
echo "Today is: $(date +'%A, %B %d, %Y')"
echo "The time is: $(date +'%I:%M %p')"
echo

# A case statement to give unique output for each day
case "$CURRENT_DAY" in
    Mon)
        echo "It's **Monday**. Like Garfield, I believe it's the worst day."
        ;;
    Tue)
        echo "It's **Tuesday**. The week is gaining momentum!"
        ;;
    Wed)
        echo "It's **Wednesday**. Truly the Alpheren Sengun of weekdays."
        ;;
    Thu)
        echo "It's **Thursday**. I bet you have a midterm today, don't fluff it up!"
        ;;
    Fri)
        echo "It's **Friday**. You wanna install linux soooooo bad"
        ;;
    Sat)
        echo "It's **Saturday**. A day for recharge and reading horrible documentation for DS210."
        ;;
    Sun)
        echo "It's **Sunday**. Enjoy all of the cramming that you didn't do yesterday."
        ;;
    *)
        echo "An unexpected day of the week has occurred. Proceed with caution."
        ;;
esac

echo
echo -e "${BLUE}*** Check Complete ***${NC}"
