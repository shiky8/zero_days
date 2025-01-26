# GatesAir Maxiva UAXTE-8 Transmitter Vulnerabilities

This directory contains details about critical vulnerabilities discovered in the **GatesAir Maxiva UAXTE-8 Transmitter** web-based management interface. These vulnerabilities expose the system to various attacks, including **Remote Code Execution (RCE)**, **Session Hijacking**, and **Information Disclosure**.

---

## Vulnerabilities Overview

### 1. **Remote Code Execution (RCE) via `/json` Endpoint**
- **Severity:** Critical  
- **Description:**  
  An attacker with a valid session ID (`sess_id`) can execute arbitrary system commands remotely if debugging mode is enabled. This can lead to full system compromise.  
- **Vulnerable Endpoints:**  
  - `/json?cmd=set&sess={sess_id}` (command execution)  
  - `/json?cmd=get&sess={sess_id}` (output retrieval)  
- **CWE-ID:** CWE-77 (Command Injection)  
- **Suggested Fixes:**  
  - Restrict access to debugging features.  
  - Implement stronger authentication and session management.  
  - Disable debugging mode in production environments.  

---

### 2. **Information Disclosure via `/logs/devcfg/` Endpoints**
- **Severity:** Critical  
- **Description:**  
  Unauthenticated attackers can access sensitive database backup files (`snapshot_users.db`) through exposed endpoints, leading to credential leakage and potential full system compromise.  
- **Vulnerable Endpoints:**  
  - `/logs/devcfg/snapshot/snapshot_users.db`  
  - `/logs/devcfg/user/snapshot_users.db`  
- **CWE-ID:** CWE-284 (Incorrect Access Control)  
- **Suggested Fixes:**  
  - Implement strict access control for sensitive directories.  
  - Apply restrictive file permissions on backup files.  
  - Encrypt sensitive data before storage.  

---

### 3. **Session Hijacking via `/logs/debug/` Endpoints**
- **Severity:** High  
- **Description:**  
  Unauthorized access to sensitive log files containing session-related data (e.g., session IDs `sess_id` and authentication success tokens `user_check_password OK`). This can lead to session hijacking, unauthorized access, and privilege escalation.  
- **Vulnerable Endpoints:**  
  - `/logs/debug/xteLog`  
  - `/logs/debug/xteLog.0`  
  - `/logs/debug/xteLog.1`  
  - `/logs/debug/xteLog.2`  
- **CWE-ID:** CWE-284 (Incorrect Access Control)  
- **Suggested Fixes:**  
  - Restrict access to sensitive log files through authentication.  
  - Avoid logging sensitive session-related data.  
  - Conduct a thorough review of file storage and access control policies.  

---

## Suggested Fixes Summary
1. **Access Control:** Restrict access to sensitive endpoints and files using authentication and role-based permissions.  
2. **File Permissions:** Apply strict permissions to sensitive files and directories.  
3. **Data Encryption:** Encrypt sensitive data before storage or transmission.  
4. **Debugging Mode:** Disable debugging mode in production environments.  
5. **Security Review:** Conduct a comprehensive security audit of the system and its configurations.  

---

## Disclaimer
This repository is for **educational and research purposes only**. The vulnerabilities described here are intended to raise awareness and help improve the security of affected systems. Use this information responsibly and only with proper authorization.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
