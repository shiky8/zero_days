# DB Electronica Mozart FM Transmitter xss Vulnerability

## Description
The Mozart FM Transmitter web management interface contains a reflected Cross-Site Scripting (XSS) vulnerability in the `/main0.php` endpoint. By injecting a malicious JavaScript payload into the `?m=` query parameter, an attacker can execute arbitrary code in the victim's browser, potentially stealing sensitive information, hijacking sessions, or performing unauthorized actions.

## Vendor of the Product(s)
**DB Electronica Telecomunicazioni S.p.A.**

## Vendor Homepage:** https://www.dbbroadcast.com/

## Affected Product(s)/Code Base
- **Product:** Mozart FM Transmitter  
- **Firmware/Software Version:** 30 , 50 , 100 , 300 , 500 , 1000 , 2000 , 3000 , 3500 , 6000 , 7000

## Vulnerable Endpoint(s)
- `/main0.php`  

## Attack Type
- **Type:** Cross-Site Scripting (XSS)  
- **Classification:** Reflected XSS  

## Impact
- **Severity:** High  
- **Description:**  
  The `/main0.php` endpoint is vulnerable to reflected Cross-Site Scripting (XSS). An attacker can inject malicious JavaScript payloads into the `?m=` query parameter, which are executed in the context of the victim’s browser. This can lead to sensitive data theft, session hijacking, or unauthorized actions on behalf of the victim.

## Affected Component(s)
Web management interface of Mozart FM Transmitter.

## Attack Vector(s)
- **Access Method:** Remote access via web interface  
- **Authentication Requirement:** Not required (depends on the configuration of the transmitter)  
- **Exploit Complexity:** Low  

##  Vulnerability Type Info:

  - **Vulnerability Type: Cross-Site Scripting (XSS)
  - **CWE-ID: CWE-79
  - **Definition: The software does not neutralize or incorrectly neutralizes user-controllable input before placing it in output that is used as a web page served to other users.

## Impact Info:

  - ** Impact Type:
  - ** Information Disclosure: Theft of cookies, tokens, or other sensitive data.
  - ** Session Hijacking: Unauthorized use of authenticated user sessions.
  - ** Defacement or Malware Injection: Potential injection of malicious content into the web interface.

## Proof of Concept (PoC)
### Request:
```http
GET /main0.php?m=<script>alert('XSS')</script> HTTP/1.1  
Host: [target]
```
https://github.com/user-attachments/assets/cd3ba88a-91fc-4eda-8849-8df7a0c57277

## Suggested Fixes:

  - ** Input Validation: Sanitize and validate user input to prevent script injection.
  - ** Output Encoding: Encode dynamic content before inserting it into the HTML response.
  - ** Content Security Policy (CSP): Enforce a robust CSP to prevent execution of unauthorized scripts.
  - ** Access Controls: Ensure that sensitive endpoints are authenticated and protected against unauthorized access.
  - ** Testing: Perform regular vulnerability assessments for XSS and related issues.
