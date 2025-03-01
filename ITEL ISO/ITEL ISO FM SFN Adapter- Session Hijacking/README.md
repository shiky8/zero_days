# ITEL ISO FM SFN Adapter - Session Hijacking Vulnerability

## Description
The ITEL ISO FM SFN Adapter (firmware ISO2 2.0.0.0, WebServer 2.0) is vulnerable to session hijacking due to improper session management on the `/home.html` endpoint. An attacker can access an active session without authentication, allowing them to control the device, modify configurations, and compromise system integrity.

---

## Vendor Information

- **Vendor:** ITEL Electronics 
- **Vendor Homepage**: https://www.itel.it/

---

## Affected Product(s)/Code Base
- **Product:** ISO FM SFN Adapter  
- **Firmware/Software Version Affected:**  
  - WebServer: 2.0  
  - Firmware Version: ISO2 2.0.0.0  

---

## Vulnerable Endpoints
- **Session Hijacking:**  
  - `/home.html`

---

## Attack Type
- **Type:** Session Hijacking / Authentication Bypass
- **Classification:** Improper Session Handling & Authorization

---

## Impact
- **Severity:** High
- **Description:**
  - The `/home.html` endpoint is vulnerable to session hijacking, allowing an attacker to access an active session without authentication by simply navigating to this endpoint.
  - If an authenticated user has an active session, the attacker is automatically granted access to the system without needing credentials.
  - This could lead to unauthorized control over the ITEL ISO FM SFN Adapter, including modifications to system settings and potential service disruptions.

---

## Affected Component(s)
- **Session Management & Authorization** (Weak Access Control in `/home.html`)

---

## Attack Vector(s)
- **Access Method:** Direct navigation to `/home.html`
- **Authentication Requirement:** None (Attacker does not need to log in)
- **Exploit Complexity:** Very Low

---

## Proof of Concept (PoC)
### Exploit: Gain Unauthenticated Access to Admin Panel
#### Steps to Reproduce
1. Open a web browser.
2. Enter the following URL (replace `<target-ip>` with the device's IP address):
   ```
   http://<target-ip>/home.html
   ```
3. If an admin or user has an active session, the attacker automatically gains access to the control panel without authentication.

---

## PoC Video  
 https://github.com/user-attachments/assets/11d2ee2e-819c-4be7-90ed-ccc37344a7c9

---

## Vulnerability Type Info
- **Vulnerability Type:**
  - Session Hijacking / Broken Access Control
- **CWE-ID:**
  - CWE-384 - Session Fixation
  - CWE-306 - Missing Authentication for Critical Function
- **Definition:**
  - The `/home.html` endpoint does not enforce authentication, allowing unauthorized access to active sessions without validation.

---

## Impact Info
- **Impact Type:**
  - **Unauthorized Access:** An attacker can gain direct control over the system.
  - **Privilege Escalation:** The attacker inherits an authenticated session, potentially with admin rights.
  - **Denial of Service (DoS):** By modifying system settings, an attacker can disrupt services.

---

## Suggested Fixes
1. **Implement Proper Session Management:**
   - Require authentication before granting access to `/home.html`.
2. **Use Secure Session Cookies:**
   - Implement session expiration and secure cookies to prevent unauthorized access.
3. **Enforce Role-Based Access Control (RBAC):**
   - Restrict access to authenticated users only.

---

## Mitigation & Workarounds
Until a patch is released, administrators should:
- Restrict access to `/home.html` using firewall rules or web server configurations.
- Enable logout enforcement after inactivity.
- Manually monitor active sessions and clear unauthorized logins.

