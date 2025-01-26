# Electrolink FM/DAB/TV Transmitter Web Management System , Credentials Disclosure Vulnerability

## Description 
Electrolink FM/DAB/TV Transmitter web management system is vulnerable to credential disclosure due to an exposed JavaScript file (`controlloLogin.js`). The file contains hard-coded or sensitive credentials in plaintext, accessible without authentication. An attacker could retrieve this file and extract sensitive information, leading to unauthorized administrative access and complete system compromise.

## Vendor of the Product(s)
**Electrolink**

## Vendor Homepage:** https://www.electrolink.com

## Affected Product(s)/Code Base
- **Product:** Electrolink FM/DAB/TV Transmitter Web Management System  

## Vulnerable Endpoint
`/controlloLogin.js`

## Attack Type
- **Type:** Credentials Disclosure  
- **Classification:** Information Disclosure  

## Impact
- **Severity:** Critical  
- **Description:**  
  An unauthenticated attacker can access the `controlloLogin.js` file via HTTP, which contains plaintext credentials (e.g., passwords). This disclosure compromises system security and could lead to unauthorized access.

## Affected Component(s)
Web-based management interface of Electrolink FM/DAB/TV Transmitter.

## Attack Vector(s)
- **Access Method:** Remote over HTTP  
- **Authentication Requirement:** None (publicly accessible endpoint)  
- **Exploit Complexity:** Low  


## Vulnerability Type Info
- **Vulnerability Type:** Exposure of Sensitive Information to an Unauthorized Actor  
- **CWE-ID:** CWE-200  
- **Definition:** The software exposes sensitive information to unauthorized actors through an accessible resource, such as a public file.  

## Impact Info
- **Impact Type:**  
  - **Information Disclosure:** Plaintext credentials are exposed in a public file.  
  - **Escalation of Privileges:** Full system compromise through credential reuse.  

## poc
https://github.com/user-attachments/assets/40a1932a-ae32-44bb-a041-41d1cdf5c4ec

## Suggested Fixes
1. **Access Control:** Restrict access to sensitive files using authentication mechanisms.  
2. **Code Refactoring:** Remove hard-coded credentials from JavaScript files.  
3. **Data Masking:** Avoid storing sensitive information in client-side resources.  
4. **Security Review:** Conduct a thorough security audit to detect similar vulnerabilities.  
5. **Monitoring & Alerts:** Implement monitoring and alerting for unauthorized access attempts.

## info
it the same bug that Gjoko 'LiquidWorm' Krstic has found in 2024  (exploit-db , 51770) but they changed the endpoint name from login.htm to controlloLogin.js
