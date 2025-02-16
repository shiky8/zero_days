# DAEnetIP4 METO Vulnerability Report

## Description:

The **DAEnetIP4 METO** product, firmware version v1.25, is vulnerable to session hijacking due to improper session management in the `/login_ok.htm` endpoint. An attacker can access an authenticated session without logging in, leading to unauthorized access to the system.

## Vendor Information

- **Vendor**: *DAEnetIP4  
- **Vendor Homepage**: http://denkovi.com/


## Affected Product(s)/Code Base

- **Product**: DAEnetIP4 METO
- **Firmware/Software Version Affected**: v1.25

## Vulnerable Endpoints

### Session Hijacking Vulnerability
- **Endpoint**: `/login_ok.htm`  
  (Allows session hijacking without login)

## Attack Type

- **Type**: Session Hijacking
- **Classification**: Improper Session Management

## Impact

- **Severity**: Critical
- **Description**:  
  The `/login_ok.htm` endpoint is vulnerable to session hijacking, where an attacker can bypass the authentication process and directly access an authenticated session without providing valid credentials. This results in unauthorized access to the application, enabling attackers to perform actions with the privileges of an authenticated user.

## Affected Component(s)

- **Component**: Session Management  
  (Missing Session Validation in `/login_ok.htm`)

## Attack Vector(s)

- **Access Method**: Direct access to vulnerable endpoint via web browser
- **Authentication Requirement**: None (Attacker can bypass authentication)
- **Exploit Complexity**: Very Low


## Proof of Concept (PoC)

### Exploit: Session Hijacking (Bypass Login)

### Steps to Reproduce:
1. Open a web browser.
2. Navigate to the vulnerable URL:http://<target-ip>/login_ok.htm
3. The attacker is redirected and granted access to an open session without having to log in, thus bypassing authentication.

### PoC Video

https://github.com/user-attachments/assets/3cb40082-fb94-4f6a-bebc-457dd074d102

## Vulnerability Type Info

- **Vulnerability Type**: Session Hijacking
- **CWE-ID**: 
- [CWE-613 - Insufficient Session Expiration](https://cwe.mitre.org/data/definitions/613.html)
- [CWE-319 - Cleartext Transmission of Sensitive Information](https://cwe.mitre.org/data/definitions/319.html)
- **Definition**: The system fails to validate sessions properly, allowing attackers to bypass authentication and hijack existing sessions.

## Impact Info

- **Impact Type**: 
- **Unauthorized Access**: Attackers can access the system and act as if they were authenticated users.
- **Privilege Escalation**: Attackers can gain access to sensitive data or settings using the privileges of authenticated users.
- **Denial of Service (DoS)**: Attackers could potentially disrupt legitimate user sessions if exploited in certain contexts.

## Suggested Fixes

1. **Implement Proper Session Validation**:  
Ensure that the `/login_ok.htm` endpoint performs session checks to validate if a user is authenticated before granting access.

2. **Use Secure Session Management**:  
Implement session expiration and token-based authentication to ensure sessions are only valid for authenticated users.

3. **Incorporate Multi-Factor Authentication (MFA)**:  
To increase security, ensure that sessions cannot be hijacked easily by requiring multi-factor authentication for sensitive actions.

## Mitigation & Workarounds

Until a patch is released, administrators should:

- Restrict direct access to `/login_ok.htm` using firewall rules or application-level controls.
- Monitor access logs for unusual activities related to this endpoint.
- Enforce session timeout and implement a secure session management mechanism to avoid unauthorized session hijacking.
