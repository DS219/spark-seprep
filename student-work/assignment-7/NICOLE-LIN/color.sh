//#!/bin/sh

# colors
colors="Red Blue Green Yellow Purple Orange Pink Cyan Magenta Turquoise"

# convert string into an array 
set -- $colors

# generate a random number between 1 and $# (number of words)
random_index=$(( (RANDOM % $#) + 1 ))

# use eval to select the n-th positional parameter
eval random_color=\$$random_index

echo "🎨 Your color is: $random_color 🎨"


