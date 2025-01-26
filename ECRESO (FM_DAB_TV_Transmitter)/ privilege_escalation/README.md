# WorldCast Systems ECRESO FM/DAB/TV Transmitter , Privilege Escalation Vulnerability

## Description
ECRESO FM/DAB/TV Transmitter web management system is vulnerable to privilege escalation through the `/wscom` endpoint. An attacker can log in as a guest, intercept the server response, and modify the JSON payload to `{"login@auth":{"accessRight":"admin","retVal":true}}`. This bypasses authentication and grants unauthorized administrative privileges, leading to complete system compromise.

## Vendor of the Product(s)
**WorldCast Systems**

## Vendor Homepage:** https://www.worldcastsystems.com/en/

## Affected Product(s)/Code Base
- **Product:** ECRESO FM/DAB/TV Transmitter  
- **Firmware/Software Version:** 1.10.1

## Vulnerable Endpoint(s)
- `/wscom`  

## Attack Type
- **Type:** Privilege Escalation  
- **Classification:** Authentication Bypass via Manipulation  

## Impact
- **Severity:** Critical  
- **Description:**  
  An attacker with guest credentials can escalate privileges to administrator by intercepting the server response at the `/wscom` endpoint. By modifying the response payload to `{"login@auth":{"accessRight":"admin","retVal":true}}`, the attacker gains unauthorized administrative access to the web-based management interface.

## Affected Component(s)
Web-based management interface of ECRESO FM/DAB/TV Transmitter.

## Attack Vector(s)
- **Access Method:** Remote access via web interface  
- **Authentication Requirement:** Requires guest-level credentials (publicly available or easily obtainable)  
- **Exploit Complexity:** Low  


## Vulnerability Type Info
- **Vulnerability Type:** Improper Authorization  
- **CWE-ID:** CWE-285  
- **Definition:** The software does not properly restrict access to administrative privileges, allowing attackers to bypass authentication mechanisms.  

## Impact Info
- **Impact Type:**  
  - **Escalation of Privileges:** Unauthorized elevation of privileges to admin level.  
  - **Potential Full System Compromise:** Administrative access enables attackers to control and manipulate the device entirely.  

## poc 
https://github.com/user-attachments/assets/61f0b587-0275-4cfa-829a-c3d1a0c137bb

## Suggested Fixes
1. **Authorization Validation:** Enforce strict server-side validation for privilege changes.  
2. **Token Security:** Use secure tokens or session mechanisms to prevent client-side manipulation.  
3. **Encrypt Communications:** Implement HTTPS to secure data in transit and prevent response interception.  
4. **Restrict Guest Access:** Limit guest privileges and access to sensitive endpoints.  
5. **Audit Logs:** Add logging and monitoring for privilege escalation attempts.  
