# Orban OPTIMOD 5950 - Broken Access Control Vulnerability

## Description

The Orban OPTIMOD 5950 (Firmware Version 1.0.0.2, System Version 2.2.15) is vulnerable to broken access control due to improper authentication handling in the web interface login page. By executing JavaScript commands in the browser’s developer console, an unauthenticated attacker can bypass the login page and gain administrative privileges, allowing full control over the device.

## Vendor Information

- **Vendor**: Orban  
- **Vendor Homepage**: https://www.orban.com/

## Affected Product(s) / Code Base

- **Product**: Orban OPTIMOD
- **Firmware/Software Versions Affected**:
  - **Model**: 5950
  - **OPTIMOD Version**: 1.0.0.2
  - **System Version**: 2.2.15
  - **Main PIC Version**: 1.04
  - **Aux PIC Version**: 0.3x
  - **Power PIC Version**: 1.0.4

## Vulnerable Endpoint(s)

- **Web Interface Login Page**:  http://<target-ip>/


## Attack Type

- **Type**: Broken Access Control
- **Classification**: Client-Side Authentication Bypass via JavaScript Console Manipulation

## Impact

- **Severity**: Critical  
- **Description**:  
The Orban OPTIMOD 5950 web interface is vulnerable to broken access control, allowing an unauthenticated attacker to bypass the login mechanism by executing JavaScript commands in the browser's developer console. This exploit grants full administrative access to the device without requiring a valid password.  

The attack exploits insecure JavaScript functions exposed on the login page, which can be invoked client-side to override authentication checks and gain unauthorized control over the transmitter’s settings.

## Affected Component(s)

- **Authentication System** (Client-Side JavaScript Validation)
- **Admin Panel Access Control Mechanism**

## Attack Vector(s)

- **Access Method**: Local execution via browser’s Developer Console (`F12 → Console Tab`)
- **Authentication Requirement**: None
- **Exploit Complexity**: Low

## Proof of Concept (PoC)

### Steps to Reproduce

1. Open the login page in a web browser: http://<target-ip>/
2. Press `F12` to open the browser's Developer Tools.
3. Navigate to the **Console** tab.
4. Execute the following JavaScript commands:
```javascript
overlay_off();
hide_signin();
res=1;
```
5. The login page disappears, and the attacker is granted admin access to the device.

---
# Proof of Concept (PoC) Video

https://github.com/user-attachments/assets/00bc7bc4-d20c-4ad1-9fc6-ed5bc21476f3

---

## Vulnerability Type Info

- **Vulnerability Type**: Broken Access Control via Client-Side Manipulation
- **CWE-ID**: [CWE-285 - Improper Authorization](https://cwe.mitre.org/data/definitions/285.html)
- **Definition**:  
  The system allows unauthorized users to bypass authentication mechanisms by invoking JavaScript functions intended for UI manipulation.

---

## Impact Info

### Impact Type

- **Unauthorized Access**: Attackers gain full administrative control over the transmitter.
- **Configuration Tampering**: Attackers can modify audio processing settings, causing signal degradation or unauthorized broadcast changes.
- **Denial of Service (DoS)**: Attackers can disable transmission or alter frequency settings, disrupting broadcast operations.

---

## Suggested Fixes

### Move Authentication to the Backend

- Implement **server-side authentication checks** for session validation instead of relying on client-side JavaScript.

### Remove Exposed JavaScript Functions

- The functions `overlay_off()`, `hide_signin()`, and `res=1` should **not be accessible** from the client-side console.

### Implement Secure Authentication Mechanisms

- Use **session-based authentication** with proper CSRF protection.
- Store authentication state **on the server** instead of relying on client-side JavaScript.

### Restrict Console Access to Debug Functions

- Ensure that sensitive UI functions **cannot be manipulated** through client-side debugging.

---

## Mitigation & Workarounds

Until a patch is released, administrators should:

- **Disable access** to the web interface from external networks using firewall rules.
- **Monitor logs** for unauthorized logins and system changes.
- **Implement Web Application Firewall (WAF) rules** to block unauthorized requests.

---

## Disclaimer

This information is provided for **educational and security research purposes only**.  
Unauthorized access to systems without explicit permission is **illegal**.

