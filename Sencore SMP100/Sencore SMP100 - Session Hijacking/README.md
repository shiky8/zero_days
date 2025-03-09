# Sencore SMP100 SMP Media Platform Session Hijacking Vulnerability

## Description

The Sencore SMP100 SMP Media Platform (firmware versions V4.2.160, V60.1.4, V60.1.29) is vulnerable to session hijacking due to improper session management on the `/UserManagement.html` endpoint. Attackers who are on the same network as the victim and have access to the target’s logged-in session can access the endpoint and add new users without any authentication. This allows attackers to gain unauthorized access to the system and perform malicious activities.

---

## Vendor Information

- **Vendor**: Sencore
- **Vendor Homepage**: [Sencore](https://www.sencore.com/)

---

## Affected Product(s)/Code Base

- **Product**: Sencore SMP100 SMP Media Platform
- **Firmware/Software Version Affected**:
  - **Mainboard Version**: V4.2.160
  - **Decoder-CC Version**: V60.1.4
  - **EN2SDI-2H Version**: V60.1.29
  - **EN2SDI-2H Submodule Version**: V60.1.10
  - **Advanced Type Version**: 0x14 Decoder-CC V60.1.4, 0x3F EN2SDI-2H-FW V60.1.10, 0x7F EN2SDI-2H V60.1.6, 0x48 EN2SDI-2Hv2 V60.1.29

---

## Vulnerable Endpoints

- `/UserManagement.html`

---

## Attack Type

- **Type**: Session Hijacking
- **Classification**: Session Management Flaw

---

## Impact

- **Severity**: High
- **Description**:
  - The Sencore SMP100 SMP Media Platform is vulnerable to session hijacking. If an attacker is on the same network as the target and the target is already logged in, the attacker can access the `/UserManagement.html` endpoint.
  - The attacker can then add new users without any form of authentication, allowing them to gain access to the system as the newly created user. This can lead to unauthorized access, allowing attackers to modify system configurations or carry out further attacks on the platform.

---

## Affected Component(s)

- **Session Management**: Insecure session handling allowing unauthorized access to critical management interfaces.
- **User Management**: Flawed logic in the user management interface that permits unauthorized addition of users.

---

## Attack Vector(s)

- **Access Method**: Attacker must be on the same local network as the target.
- **Authentication Requirement**: None (as long as the target is already logged in).
- **Exploit Complexity**: Low

---

## Proof of Concept (PoC)

### Exploit: Session Hijacking via `/UserManagement.html`

#### Steps to Reproduce:

1. Ensure the attacker and target are on the same network.
2. Ensure the target device is logged in and has an active session.
3. The attacker navigates to the `/UserManagement.html` page of the target device’s management interface.
4. The attacker can add new users with full privileges without any authentication or validation, bypassing security controls.
5. The attacker can now use the newly created user credentials to log in and perform administrative tasks on the device.

---

### PoC Video
https://github.com/user-attachments/assets/440352ec-523c-4006-96dc-b0b1c06f01d1

---

## Vulnerability Type Info

- **Vulnerability Type**:
  - Session Hijacking
  - Unrestricted User Management
- **CWE-ID**:
  - [CWE-287](https://cwe.mitre.org/data/definitions/287.html) - Improper Authentication
  - [CWE-384](https://cwe.mitre.org/data/definitions/384.html) - Session Fixation
  - [CWE-862](https://cwe.mitre.org/data/definitions/862.html) - Missing Authorization

---

## Impact Info

- **Impact Type**:
  - **Unauthorized Access**: The attacker can add new users to the system and log in without authentication.
  - **Privilege Escalation**: The attacker can assign admin-level privileges to newly created users.
  - **Potential for Malicious Activity**: The attacker can reconfigure the device or use it for further attacks.

---

## Suggested Fixes

### Implement Secure Session Handling

- Ensure that session tokens are securely validated for every request, especially for sensitive operations like user management.
- Consider using session expiration or re-authentication for sensitive actions like adding new users.

### Implement Access Control Checks

- Enforce proper authorization checks to ensure that users can only add or modify users when they have the appropriate privileges.

---

### Monitor Session Activity

- Continuously monitor active sessions and implement mechanisms to detect and respond to abnormal activity.

## Mitigation & Workarounds

Until a patch is released, administrators should:

- Restrict access to the `/UserManagement.html` endpoint via IP whitelisting or VPNs.
- Monitor for unauthorized user creation or other suspicious activity on the device.
- Disable remote management or limit it to trusted IPs only.
