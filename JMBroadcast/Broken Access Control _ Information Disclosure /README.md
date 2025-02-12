# JMBroadcast JMB0150 - Broken Access Control & Information Disclosure

## Description

The **JMBroadcast JMB0150** (Firmware Version **JMB0150**) is vulnerable to **broken access control** and **information disclosure** due to missing authentication checks in the `/HOME.php` and `/LOGIN_DB.php` endpoints.  

- An attacker can directly access the **admin panel** without login credentials.
- The API leaks **hardcoded administrator passwords** in an unprotected response.
- These vulnerabilities can lead to **full system compromise**.


## Vendor Information

- **Vendor**: JMBroadcast  
- **Vendor Homepage**: http://jmbroadcast.com/


## Affected Product(s) / Code Base

- **Product:** JMBroadcast JMB0150  
- **Firmware/Software Version Affected:**  
  - **Model:** JMB0150  

## Vulnerable Endpoints

### Broken Access Control:
- `/HOME.php` → Allows **admin access** without authentication.

### Information Disclosure:
- `/LOGIN_DB.php` → Exposes **stored credentials** in JSON format.

## Attack Type

1. **Broken Access Control (Authentication Bypass)**
2. **Information Disclosure (Admin Credentials Leak)**  
**Classification:** Improper Access Control & Hardcoded Credentials Exposure

## Impact

**Severity: Critical**  

- `/HOME.php` allows **unauthenticated access** to admin pages, granting **full control** over the system.  
- `/LOGIN_DB.php` leaks **administrator credentials** in plaintext JSON format.  
- Combining these vulnerabilities allows an attacker to:  
  - Gain **full system control**  
  - Modify **configurations**  
  - Disrupt **broadcast operations**  

## Affected Components

1. **Authentication System** (Missing validation in `/HOME.php`)  
2. **Credential Storage** (Exposed in `/LOGIN_DB.php` without authentication)  

## Attack Vectors

- **Access Method:** Direct access to vulnerable endpoints via a **web browser** or **HTTP requests**  
- **Authentication Requirement:** None  
- **Exploit Complexity:** Very Low  

## Proof of Concept (PoC)

### Exploit 1: Broken Access Control (Admin Panel Bypass)

**Steps to Reproduce:**
1. Open a web browser.  
2. Navigate to: http://<target-ip>/HOME.php


3. The attacker is granted **admin access** without login.

---

### Exploit 2: Information Disclosure (Retrieve Admin Credentials)

**Steps to Reproduce:**
1. Send a `GET` request to: http://<target-ip>/LOGIN_DB.php

2. The server responds with **plaintext admin credentials** in JSON format:

```json
{
  "admin_user_id": "JMBroadcast",
  "admin_user_pw": "JMB0150",
  "guest_user_id": "JMBROAD",
  "guest_user_pw": "jmbroad"
}
```
3. Use the leaked credentials to log in as admin.

---

# Security Advisory: Broken Access Control & Information Disclosure

## PoC Video
https://github.com/user-attachments/assets/396294f7-3e64-49f4-b6db-6c3789e668fd

## Vulnerability Type Info

### Vulnerability Type:
- **Broken Access Control** (Unauthenticated Admin Panel Access)
- **Information Disclosure** (Credentials Exposed in API Response)

### CWE-ID:
- **CWE-285** - Improper Authorization  
- **CWE-200** - Exposure of Sensitive Information  

### Definition:
- The system **fails to enforce authentication** in `/HOME.php`, allowing **unauthorized access** to admin functions.  
- `/LOGIN_DB.php` **exposes stored credentials** without authentication, allowing attackers to retrieve **valid admin passwords**.  

---

## Impact Info

- **Unauthorized Admin Access:** Attackers gain **full administrative control** without login.  
- **Credential Theft:** Attackers can retrieve **plaintext usernames and passwords**.  
- **Configuration Tampering:** Attackers can modify **system settings**.  
- **Denial of Service (DoS):** Attackers can **shut down or alter broadcast settings**.  

---

## Suggested Fixes

### **Implement Proper Authentication for Admin Pages:**
- Require **valid credentials** before granting access to `/HOME.php`.  

### **Restrict Access to `/LOGIN_DB.php`:**
- Do **not expose credentials** in publicly accessible endpoints.  
- Store credentials securely using **bcrypt, Argon2**, or other secure hashing methods.  

### **Implement Secure Session Management:**
- Enforce **session-based authentication** using **secure cookies**.  

### **Remove Hardcoded Credentials:**
- Do not return **plaintext credentials** in API responses.  
- Use **environment variables** or **database authentication mechanisms**.  

---

## Mitigation & Workarounds

Until a patch is released, administrators should:

- **Restrict access** to `/LOGIN_DB.php` and `/HOME.php` using **firewall rules**.  
- **Monitor unauthorized access attempts** in **system logs**.  
- **Change default admin passwords immediately**.  
- **Implement Web Application Firewall (WAF) rules** to block direct access to vulnerable endpoints.  

---

## Disclaimer  

This information is provided for **educational purposes only**. The author is **not responsible** for any misuse of this information.  




