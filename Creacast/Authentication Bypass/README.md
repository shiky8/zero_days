# Creacast Creabox Manager - Authentication Bypass Vulnerability

## Description
Creacast Creabox Manager contains a critical authentication flaw that allows an attacker to bypass login validation. The system grants access when the username is `creabox` and the password **begins** with the string `creacast`, regardless of what follows.

---

## Vendor Information

- **Vendor**: CREACAST  
- **Vendor Homepage**: http://www.creacast.com/

## Product
- **Name**: Creacast Creabox Manager
- **Firmware Version**: 4.4.4

## Vulnerability Type
- Authentication Bypass

## Attack Vector
- Network (HTTP)


---

## Vulnerable Endpoint
- `/` (Login Portal)

---

## Exploitation

### Example Login
- **Username**: `creabox`
- **Password**: `creacast123`
  - Any password starting with `creacast` is accepted

### Manual Exploit
1. Navigate to the login page (e.g., `http://<target-ip>/`)
2. Use the credentials:
   - `Username: creabox`
   - `Password: creacast_test`
3. You are granted administrative access.

---

## Proof of Concept (PoC) for(RCE,Information Disclosure,Authentication Bypass)
https://github.com/user-attachments/assets/de63e189-2137-4521-8a32-8dc9502ae13a

---

## Impact
- Full administrative access to the web interface
- Unauthorized changes to device configuration
- Potential disruption of service or hijack of streaming infrastructure

---

## Suggested Fixes
- Enforce strict password validation on the backend
- Do not allow pattern-based or hardcoded password prefixes
- Apply proper authentication logic for admin users
- Implement rate limiting and logging for failed login attempts

---

## Workarounds
- Block access to the admin panel via external IPs using a firewall or VPN
- Change or disable default/system usernames like `creabox` if possible
- Monitor for suspicious login attempts using `creabox` and `creacast*` patterns

---


