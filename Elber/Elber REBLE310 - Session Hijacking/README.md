# Elber REBLE310 Session Hijacking Vulnerability

## Description:

The Elber REBLE310 product, firmware version 5.5.1.R, is vulnerable to session hijacking due to improper session management in the `/reble310//indexTH.htm` and `/reble310//indexR.htm` endpoints. An attacker can access an authenticated session without logging in, leading to unauthorized access to the system.

## Vendor Information

- **Vendor**: *Elber  
- **Vendor Homepage**: https://www.elber.it/en/index.php


## Affected Product(s)/Code Base:

- **Product**: Elber REBLE310
- **Firmware/Software Version Affected**:
    - Firmware Version: 5.5.1.R
    - Equipment Model: REBLE310/RX10/4ASI

## Vulnerable Endpoints:

### Session Hijacking Vulnerability:
- `/reble310//indexTH.htm`
- `/reble310//indexR.htm`

## Attack Type:

- **Type**: Session Hijacking
- **Classification**: Improper Session Management

## Impact:

- **Severity**: Critical
- **Description**:
    - The `/reble310//indexTH.htm` and `/reble310//indexR.htm` endpoints are vulnerable to session hijacking. An attacker can bypass the authentication process and directly access an authenticated session without providing valid credentials. This leads to unauthorized access to the system and allows attackers to perform actions with the privileges of an authenticated user.

## Affected Component(s):

- **Component**: Session Management
- **Vulnerable Endpoints**: `/reble310//indexTH.htm` and `/reble310//indexR.htm` (Missing Session Validation)

## Attack Vector(s):

- **Access Method**: Direct access to vulnerable endpoints via web browser
- **Authentication Requirement**: None (Attacker can bypass authentication)
- **Exploit Complexity**: Very Low

## Proof of Concept (PoC):

### Exploit: Session Hijacking (Bypass Login)

### Steps to Reproduce:

1. Open a web browser.
2. Navigate to the vulnerable URL:
    - `http://<target-ip>/reble310//indexTH.htm`
    - Or:
    - `http://<target-ip>/reble310//indexR.htm`
3. The attacker is redirected and granted access to an open session without having to log in, thus bypassing authentication.

### PoC Video:
https://github.com/user-attachments/assets/6ad64ce1-8d7e-4471-8ede-7fff650efdb8

## Vulnerability Type Info:

- **Vulnerability Type**: Session Hijacking
- **CWE-ID**:
    - CWE-613: Insufficient Session Expiration
    - CWE-319: Cleartext Transmission of Sensitive Information
- **Definition**:
    - The system fails to properly validate sessions, allowing attackers to bypass authentication and hijack existing sessions.

## Impact Info:

- **Impact Type**:
    - **Unauthorized Access**: Attackers can access the system and act as authenticated users.
    - **Privilege Escalation**: Attackers can gain access to sensitive data or settings using the privileges of authenticated users.
    - **Denial of Service (DoS)**: Attackers could potentially disrupt legitimate user sessions if exploited in certain contexts.

## Suggested Fixes:

1. **Implement Proper Session Validation**:
    - Ensure that the `/reble310//indexTH.htm` and `/reble310//indexR.htm` endpoints check whether a user is authenticated before granting access.

2. **Use Secure Session Management**:
    - Implement session expiration and token-based authentication to ensure that sessions are only valid for authenticated users.

3. **Incorporate Multi-Factor Authentication (MFA)**:
    - To enhance security, require multi-factor authentication for sensitive actions to prevent easy session hijacking.

## Mitigation & Workarounds:

Until a patch is released, administrators should:

1. Restrict direct access to `/reble310//indexTH.htm` and `/reble310//indexR.htm` using firewall rules or application-level controls.
2. Monitor access logs for unusual activities related to these endpoints.
3. Enforce session timeout and implement secure session management to avoid unauthorized session hijacking.
