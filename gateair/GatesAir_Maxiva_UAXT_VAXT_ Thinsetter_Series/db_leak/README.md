# GatesAir Maxiva UAXT , VAXT  Transmitter db Data Breach Vulnerability

## Description 
A critical information disclosure vulnerability exists in the web-based management interface of GatesAir Maxiva UAXT , VAXT  transmitters due to Incorrect Access Control (CWE-284). Unauthenticated attackers can directly access sensitive database backup files (`snapshot_users.db`) via publicly exposed URLs (`/logs/devcfg/snapshot/` and `/logs/devcfg/user/`). Exploiting this vulnerability allows retrieval of sensitive user data, including login credentials, potentially leading to full system compromise.

## Vendor of the Product(s)
**GatesAir**

## Vendor Homepage:** https://www.gatesair.com/

## Affected Product(s)/Code Base
- **Product:** GatesAir Maxiva UAXT (UAXT-80G2-UC, UAXTE-24, UAXTE-4-G2, UAXTE-4, UAXTE-8, UAXTE-2R37, UAXTE-2P-C, UAXTE-1-G2, UAXTE-3-G2, UAXTE-100B) , VAXT (VAXTE-1P-C,VAXT-150G2, VAXT-80-DA, VAXT-300G2, VAXT-550G2-DA ) Transmitter
- **Firmware/Software Version:** 05.26.0003,05.25.0014,04.19.00073 , 01.13.0012,01.19.0005,05.26.0003

## Vulnerable Endpoints
- `/logs/devcfg/snapshot/snapshot_users.db`  
- `/logs/devcfg/user/snapshot_users.db`  

## Attack Type
- **Type:** Remote File Retrieval  
- **Classification:** Information Disclosure / Data Breach  

## Impact
- **Severity:** Critical  
- **Description:**  
  Unauthenticated attackers can access sensitive database backup files (`snapshot_users.db`) through exposed endpoints, leading to credential leakage and potential full system compromise.

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
  - **Information Disclosure:** Sensitive database files containing user credentials are exposed.  
  - **Escalation of Privileges:** Attackers can use leaked credentials to gain administrative access.  

## poc
https://github.com/user-attachments/assets/27e2ccf2-2b33-463d-903d-9d17ffbb0750

## Suggested Fixes
1. **Access Control:** Implement strict access control for sensitive directories.  
2. **File Permissions:** Apply restrictive file permissions on backup files.  
3. **Data Encryption:** Encrypt sensitive data before storage.  
4. **Security Review:** Conduct a comprehensive security audit of the system and its file handling processes.  
