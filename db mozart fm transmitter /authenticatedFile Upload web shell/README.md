# DB Electronica Mozart FM Transmitter authenticated File Upload Vulnerability

## Description
The Mozart FM Transmitter web management interface contains an unrestricted file upload vulnerability in the `/patch.php` endpoint. An attacker with administrative credentials can upload arbitrary files (e.g., PHP webshells), which are stored in the `/patch/` directory. This allows the attacker to execute arbitrary commands on the server, potentially leading to full system compromise.

## Vendor of the Product(s)
**DB Electronica Telecomunicazioni S.p.A.**

## Vendor Homepage:** https://www.dbbroadcast.com/

## Affected Product(s)/Code Base
- **Product:** Mozart FM Transmitter  
- **Firmware/Software Version:** 30 , 50 , 100 , 300 , 500 , 1000 , 2000 , 3000 , 3500 , 6000 , 7000

## Vulnerable Endpoint(s)
- `/patch.php`  

## Attack Type
- **Type:** File Upload Vulnerability  
- **Classification:** Unrestricted File Upload  

## Impact
- **Severity:** Critical  
- **Description:**  
  The `/patch.php` endpoint allows an authenticated user with administrative access to upload files without proper validation or sanitization. An attacker can exploit this vulnerability to upload a malicious file (e.g., a PHP webshell) to the server. Once uploaded, the attacker can execute arbitrary commands by accessing the webshell at `/patch/` and achieve full system compromise.

## Affected Component(s)
Web management interface of Mozart FM Transmitter.

## Attack Vector(s)
- **Access Method:** Remote access via web interface  
- **Authentication Requirement:** Administrative login required  
- **Exploit Complexity:** Low  


## Impact Example:

   - ** Execution: Uploading the above webshell allows the attacker to execute system commands directly on the server.

   - ** Result: The attacker gains full control over the system, including the ability to modify files, extract sensitive information, or escalate privileges.

## Vulnerability Type Info

   - ** Vulnerability Type: Unrestricted File Upload

   - **  CWE-ID: CWE-434

   - ** Definition: The software allows the uploading of files without sufficient validation, which can result in remote code execution, malware delivery, or other malicious actions.

## Impact Info

   - ** Impact Type:
   - Code Execution: Execute arbitrary commands on the server.
   - Privilege Escalation: Gain higher privileges on the system.
   - Data Exfiltration: Access or extract sensitive information.
   - System Compromise: Full control of the server.

## Proof of Concept (PoC)
### Steps to Reproduce:
1. Log in to the Mozart FM Transmitter web interface as an administrator.  
2. Navigate to the `/patch.php` endpoint.  
3. Upload a malicious PHP webshell (e.g., `webshell.php`).  
4. Access the uploaded file at `/patch/webshell.php`.  
5. Execute arbitrary system commands via the webshell interface.  

### Example Webshell (PHP):
```php
<?php
if(isset($_REQUEST['cmd'])){
    echo "<pre>" . shell_exec($_REQUEST['cmd']) . "</pre>";
}
?>
```
https://github.com/user-attachments/assets/cd3ba88a-91fc-4eda-8849-8df7a0c57277

## Suggested Fixes

   - ** File Type Validation: Restrict uploaded files to specific, safe file types (e.g., .zip or .bin for patches).

   - ** File Content Validation: Use server-side checks to ensure the content of the uploaded file matches its intended purpose.

   - ** Storage Restrictions: Store uploaded files outside of web-accessible directories.

   - ** Authentication Controls: Strengthen authentication mechanisms to prevent unauthorized access.

   - ** Access Controls: Restrict access to the /patch.php endpoint to authorized personnel only.

   - ** Logging: Log file upload activities for auditing and monitoring purposes.

   - ** Testing: Perform regular security testing for file upload vulnerabilities.
