# GatesAir Flexiva-LX Series - Session Hijacking Vulnerability


## Description
GatesAir Flexiva-LX devices expose sensitive session identifiers (`sid`) in the publicly accessible log file located at `/log/Flexiva%20LX.log`.  
An unauthenticated attacker can retrieve valid session IDs and hijack sessions without providing any credentials.

This attack requires the legitimate user (admin) to have previously closed the browser window **without logging out**.

---
## Vendor Information

- **Vendor**: GatesAir  
- **Vendor Homepage**: https://www.gatesair.com

## Product
- **Name**: GatesAir Flexiva-LX Series (e.g., LX100)
- **Firmware Versions**: All known versions

## Vulnerability Type
- Session Hijacking via Log File Exposure

## Attack Vector
- Network (HTTP)



---

## Affected Endpoints
- `/`
- `/log/Flexiva%20LX.log`

---

## Exploitation Steps
1. Visit:  
```
http://<target-ip>/log/Flexiva%20LX.log
```
2. Search for the `sid` value inside the log contents.
3. Copy the `sid`.
4. In your browser, set a cookie named `sid` with the copied value.
5. Refresh the main page (`/`).
6. You are now logged in as the legitimate admin user.

> **Note**: The victim must have closed the browser without properly logging out.

---
## Proof of Concept (PoC)
https://github.com/user-attachments/assets/1f3b414e-2634-4e6d-9ecc-987dc8d90426

---
## Impact
- Full administrative access to the device.
- Unauthorized changes to configurations.
- Possible disruption of critical broadcast services.

---

## Suggested Fixes
- Avoid logging session identifiers into any log files.
- Restrict access to `/log/` endpoints only to authenticated users.
- Bind session tokens to the user's IP address and User-Agent.
- Invalidate sessions when the browser is closed or after inactivity.
- Set session cookies with `Secure`, `HttpOnly`, and `SameSite=Strict` attributes.
- Encrypt and rotate log files regularly.

---

## Workarounds
- Implement web server restrictions to block access to `/log/` folders.
- Educate users to **always** log out instead of just closing the browser window.

---





