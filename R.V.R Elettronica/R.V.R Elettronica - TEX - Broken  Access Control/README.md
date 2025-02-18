# R.V.R Elettronica TEX Broken Access Control Vulnerability

## Description

The **R.V.R Elettronica TEX** product (firmware **TEXL-000400**, Web GUI **TLAN-000400**) is vulnerable to **broken access control** due to improper authentication checks on the `/_Passwd.html` endpoint.  

An attacker can send an **unauthenticated** `POST` request to change the **Admin, Operator, and User** passwords, resulting in **complete system compromise**.

---

## Vendor Information

- **Vendor:** R.V.R Elettronica  
- **Vendor Homepage**: https://www.rvr.it/en/

---

## Affected Products

| Product Name | Firmware Version | Web GUI Version | Configuration Table |
|-------------|----------------|-----------------|---------------------|
| R.V.R Elettronica TEX | TEXL-000400 | TLAN-000400 | TEX-3K5L-01 |

---

## Vulnerable Endpoints

- **Broken Access Control:**
  - `/_Passwd.html`

---

## Attack Details

- **Type:** Broken Access Control  
- **Classification:** Improper Authentication & Authorization  
- **Severity:** **Critical**  

### Impact:
- The `/_Passwd.html` endpoint allows **unauthenticated** password changes for all user roles (**Admin, Operator, and User**).  
- An attacker can **reset** the admin password and gain **full control** over the system.  

### Affected Components:
- **Authentication & Authorization** (Weak Access Control in `/_Passwd.html`)  

### Attack Vectors:
- **Access Method:** Direct unauthenticated `POST` request  
- **Authentication Requirement:** **None** (No login required)  
- **Exploit Complexity:** **Very Low**  

---

## Proof of Concept (PoC)

### Exploit: Reset Admin, Operator, and User Passwords Without Authentication  

#### Steps to Reproduce:

1. Open a terminal or use a tool like **cURL** or **Burp Suite**.
2. Send the following **unauthenticated** `POST` request:

   ```bash
   curl -X POST "http://<target-ip>/_Passwd.html" \
        -d "PSW_User=new_User_password&PSW_Oper=new_Oper_password&PSW_Admin=new_admin_password"
    ```
3. The system accepts the request and updates the passwords without authentication.
4. The attacker can now log in using the new credentials and take full control of the device.

---

## PoC Video  
 https://github.com/user-attachments/assets/2fd47dd9-49c7-4b14-b5ef-faeb6b6769bf

---

## Vulnerability Classification  

- **Vulnerability Type:** Broken Access Control  
- **CWE-IDs:**  
  - **CWE-284** - Improper Access Control  
  - **CWE-306** - Missing Authentication for Critical Function  

### Definition:  
The `/_Passwd.html` endpoint does **not** enforce authentication, allowing **unauthorized password changes** for Admin, Operator, and User accounts.  

---

## Impact Information  

- **Unauthorized Access:** An attacker can change passwords and log in as **Admin**.  
- **Privilege Escalation:** The attacker can set their own credentials and gain **full system control**.  
- **Denial of Service (DoS):** By changing passwords, an attacker can **lock out legitimate users**.  

---

## Suggested Fixes  

### 1. Implement Proper Authentication  
- Ensure `/_Passwd.html` **requires authentication** before processing password changes.  

### 2. Use Role-Based Access Control (RBAC)  
- Restrict access to password reset functionality **based on user roles**.  

### 3. Enforce Secure Sessions  
- Implement **session-based authentication** to prevent unauthorized access.  

---

## Mitigation & Workarounds  

Until a **patch** is released, administrators should:  

- **Restrict access** to `/_Passwd.html` using **firewall rules** or **web server configurations**.  
- **Monitor logs** for unauthorized password change requests.  
- **Manually secure admin credentials** by **periodically changing** them.  

---

## Disclaimer  

This vulnerability disclosure is for **educational purposes only**. Unauthorized exploitation of security flaws is **illegal** and should only be conducted within **legal and ethical guidelines**.  

---
