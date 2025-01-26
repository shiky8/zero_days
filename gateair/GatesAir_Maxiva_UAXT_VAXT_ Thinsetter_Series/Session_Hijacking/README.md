# GatesAir Maxiva UAXT , VAXT Transmitter Session Hijacking Vulnerability

## Description 
A session hijacking vulnerability exists in the web-based management interface of GatesAir Maxiva UAXT , VAXT transmitters. Unauthenticated attackers can access exposed log files (`/logs/debug/xteLog*`), potentially revealing sensitive session-related information such as session IDs (`sess_id`) and authentication success tokens (`user_check_password OK`). Exploiting this flaw could allow attackers to hijack active sessions, gain unauthorized access, and escalate privileges on affected devices.

## Vendor of the Product(s)
**GatesAir**

## Vendor Homepage:** https://www.gatesair.com/

## Affected Product(s)/Code Base
- **Product:** GatesAir Maxiva UAXT (UAXT-80G2-UC, UAXTE-24, UAXTE-4-G2, UAXTE-4, UAXTE-8, UAXTE-2R37, UAXTE-2P-C, UAXTE-1-G2, UAXTE-3-G2, UAXTE-100B) , VAXT (VAXTE-1P-C,VAXT-150G2, VAXT-80-DA, VAXT-300G2, VAXT-550G2-DA ) Transmitter
- **Firmware/Software Version:** 05.26.0003,05.25.0014,04.19.00073 , 01.13.0012,01.19.0005,05.26.0003

## Vulnerable Endpoints
- `/logs/debug/xteLog`  
- `/logs/debug/xteLog.0`  
- `/logs/debug/xteLog.1`  
- `/logs/debug/xteLog.2`  

## Attack Type
- **Type:**  Session Hijacking  
- **Classification:** Information Disclosure / Privilege Escalation  

## Impact
- **Severity:** High  
- **Description:**  
  Unauthorized access to sensitive log files containing session-related data (e.g., session IDs `sess_id` and authentication success tokens `user_check_password OK`). This can lead to session hijacking, unauthorized access, and potential privilege escalation.

## Affected Component(s)
Web-based management interface of GatesAir Maxiva UAXT , VAXT Transmitter.

## Attack Vector(s)
- **Access Method:** Remote over HTTP  
- **Authentication Requirement:** None (unauthenticated)  
- **Exploit Complexity:** Low (direct URL access)  

## Vulnerability Type Info
- **Vulnerability Type:** Incorrect Access Control  
- **CWE-ID:** CWE-284  
- **Definition:** The software does not restrict or incorrectly restricts access to a resource from an unauthorized actor.  

## Impact Info
- **Impact Type:**  
  - **Information Disclosure:** Sensitive session-related data such as session IDs and authentication success tokens are exposed.  
  - **Escalation of Privileges:** Attackers can leverage exposed session information to gain unauthorized access or escalate privileges.  


## poc
https://github.com/user-attachments/assets/332e617e-e9f0-4dc0-b8c8-61d2374990b5

## Suggested Fixes
1. **Access Control:** Restrict access to sensitive log files through authentication and role-based permissions.  
2. **File Permissions:** Apply strict permissions to log files.  
3. **Data Masking:** Avoid logging sensitive session-related data.  
4. **Security Review:** Conduct a thorough review of file storage, web server configurations, and access control policies.  
