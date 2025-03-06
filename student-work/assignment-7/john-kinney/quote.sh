QUOTE=$(curl -sSk https://api.quotable.io/random | jq -r '.content + " - " + .author')
# this file fetches and displays a random quote with the author

echo "$QUOTE"
echo
exit 0