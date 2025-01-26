# GatesAir Maxiva UAXT , VAXT Transmitter RCE Vulnerability

## Description 
A critical remote code execution (RCE) vulnerability exists in the web-based management interface of GatesAir Maxiva UAXT , VAXT transmitters when debugging mode is enabled. An attacker with a valid session ID (`sess_id`) can send specially crafted POST requests to the `/json` endpoint, enabling arbitrary command execution on the underlying system. This vulnerability can lead to full system compromise, including unauthorized access, privilege escalation, and potentially full device takeover.

## Vendor of the Product(s)
**GatesAir**

## Vendor Homepage:** https://www.gatesair.com/

## Affected Product(s)/Code Base
- **Product:** GatesAir Maxiva UAXT (UAXT-80G2-UC, UAXTE-24, UAXTE-4-G2, UAXTE-4, UAXTE-8, UAXTE-2R37, UAXTE-2P-C, UAXTE-1-G2, UAXTE-3-G2, UAXTE-100B) , VAXT (VAXTE-1P-C,VAXT-150G2, VAXT-80-DA, VAXT-300G2, VAXT-550G2-DA )  Transmitter  
- **Firmware/Software Version:** 05.26.0003,05.25.0014,04.19.00073 , 01.13.0012,01.19.0005,05.26.0003

## Vulnerable Endpoints
- `/json?cmd=set&sess={sess_id}` (command execution)  
- `/json?cmd=get&sess={sess_id}` (output retrieval)  

## Attack Type
- **Type:** Remote Code Execution (RCE)  
- **Classification:** Code Execution / System Compromise  

## Impact
- **Severity:** Critical  
- **Description:**  
  An attacker with access to a valid session ID (`sess_id`) can execute arbitrary system commands remotely if debugging mode is enabled. This vulnerability can result in full system compromise.

## Affected Component(s)
Web-based management interface of GatesAir Maxiva UAXT , VAXT  Transmitter.

## Attack Vector(s)
- **Access Method:** Remote over HTTP  
- **Authentication Requirement:** Requires a valid session ID (`sess_id`)  
- **Exploit Complexity:** Medium (dependent on debugging mode being enabled)  


## Vulnerability Type Info
- **Vulnerability Type:** Improper Neutralization of Special Elements used in a Command (Command Injection)  
- **CWE-ID:** CWE-77  
- **Definition:** The software constructs all or part of a command using external input but fails to properly neutralize special elements, leading to command injection.  

## Impact Info
- **Impact Type:**  
  - **Code Execution:** Arbitrary system commands can be executed remotely.  
  - **Escalation of Privileges:** System compromise can lead to administrative access.  

## poc
![Image](https://github.com/user-attachments/assets/972e8648-183c-4e18-b2c0-fa755d1e3356)

## Suggested Fixes
1. **Access Control:** Restrict access to debugging features and administrative endpoints.  
2. **Authentication Hardening:** Implement stronger authentication and session management.  
3. **Command Sanitization:** Properly sanitize all user inputs and commands.  
4. **Debugging Mode Restriction:** Disable debugging mode in production environments.  
5. **Security Review:** Conduct a comprehensive security audit of the management interface and backend system.  
