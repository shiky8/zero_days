# BW Broadcast Transmitter Management System ,Session Hijacking Vulnerability

## Description 
A session hijacking vulnerability exists in the BW Broadcast Transmitter Management System due to exposed log files accessible over HTTP. The logs contain session identifiers (`sid`) related to successful remote logins. An attacker can extract these identifiers and use them to gain unauthorized access to the system, leading to potential administrative compromise.

## Vendor of the Product(s)
**BW Broadcast**

## Vendor Homepage:** https://www.bwbroadcast.com/

## Affected Product(s)/Code Base
- **Product:** BW Broadcast Transmitter Management System  
- **Firmware/Software Version:** TX600 (14980) , TX300 (32990) (31448) , TX150  , TX1000,TX30,TX50 

## Vulnerable Endpoints
- `/TX-V1.log`  
- `/TX-V2.log`  
- `/TX-V3.log`  
- `/log/TX-V1.log`  
- `/log/TX-V2.log`  
- `/log/TX-V3.log`  

## Attack Type
- **Type:** Session Hijacking  
- **Classification:** Information Disclosure / Unauthorized Access  

## Impact
- **Severity:** High  
- **Description:**  
  An attacker can access system logs exposed over HTTP without authentication. These logs contain sensitive session identifiers (`sid`), enabling unauthorized remote access and session hijacking.

## Affected Component(s)
Web-based management interface of BW Broadcast Transmitter.

## Attack Vector(s)
- **Access Method:** Remote over HTTP  
- **Authentication Requirement:** None (logs are publicly accessible)  
- **Exploit Complexity:** Low  


## Vulnerability Type Info
- **Vulnerability Type:** Information Exposure Through Log Files  
- **CWE-ID:** CWE-532  
- **Definition:** The software logs sensitive information in log files that are accessible by unauthorized users.  

## Impact Info
- **Impact Type:**  
  - **Information Disclosure:** Logs expose sensitive session identifiers.  
  - **Escalation of Privileges:** Full system compromise through session hijacking.  

## poc
https://github.com/user-attachments/assets/433d867f-89e8-42d4-a673-94e69c862b9d

## Suggested Fixes
1. **Access Control:** Restrict access to log files using authentication and authorization mechanisms.  
2. **Log Management:** Disable public access to log files and restrict access to administrators only.  
3. **Data Masking:** Redact sensitive data such as session IDs in log files.  
4. **Security Review:** Conduct a security audit to identify other possible exposure points.  
5. **Monitoring & Alerts:** Implement monitoring and alerting for unauthorized log access attempts.  
