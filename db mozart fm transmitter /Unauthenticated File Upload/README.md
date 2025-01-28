# DB Electronica Mozart FM Transmitter Unauthenticated File Upload Vulnerability

## Description 
The Mozart FM Transmitter web management interface contains an unauthenticated file upload vulnerability in the `/upload_file.php` endpoint. An attacker can exploit this by sending a crafted POST request with a malicious file (e.g., a PHP webshell) to the server. The uploaded file is stored in the `/upload/` directory, enabling remote code execution and full system compromise.

## Vendor of the Product(s)
**DB Electronica Telecomunicazioni S.p.A.**

## Vendor Homepage:** https://www.dbbroadcast.com/

## Affected Product(s)/Code Base
- **Product:** Mozart FM Transmitter
- **Firmware/Software Version:** 30 , 50 , 100 , 300 , 500 , 1000 , 2000 , 3000 , 3500 , 6000 , 7000

## Vulnerable Endpoint(s)
- `/upload_file.php`

## Attack Type
- **Type:** Unauthenticated File Upload Vulnerability
- **Classification:** Unrestricted File Upload

## Impact
- **Severity:** Critical
- **Description:**  
  The `/upload_file.php` endpoint allows unauthenticated users to upload files without any authentication, validation, or sanitization. This vulnerability enables attackers to upload malicious files (e.g., PHP webshells) directly to the server. Once uploaded, the attacker can access the file at `/upload/` and execute arbitrary commands to compromise the server.

## Affected Component(s)
- Web management interface of Mozart FM Transmitter

## Attack Vector(s)
- **Access Method:** Remote access via unauthenticated HTTP POST request
- **Authentication Requirement:** None
- **Exploit Complexity:** Low

## Impact Example

   - ** Execution:
   - Uploading the above webshell allows the attacker to execute arbitrary system commands directly on the server.

   - ** Result:
   - he attacker gains full control over the system, including the ability to modify files, extract sensitive information, or escalate privileges.

## Vulnerability Type Info

   - ** Vulnerability Type: Unrestricted File Upload

   - **  CWE-ID: CWE-434

   - ** Definition:
   - The software allows the uploading of files without sufficient validation, which can result in remote code execution, malware delivery, or other malicious actions.

## Impact Info

   - ** Impact Type:
   - Code Execution: Execute arbitrary commands on the server.
   - Privilege Escalation: Gain higher privileges on the system.
   - Data Exfiltration: Access or extract sensitive information.
   - System Compromise: Full control of the server.

---

## Proof of Concept (PoC)
### Steps to Reproduce
1. Craft a malicious PHP webshell (e.g., `poc.php`) to allow remote command execution.
2. Send an unauthenticated HTTP POST request to the `/upload_file.php` endpoint with the malicious file as payload.
3. Access the uploaded file at `/upload/poc.php`.
4. Execute arbitrary commands on the server via the webshell.

### Example Webshell (PHP)
```php
<?php
if(isset($_REQUEST['cmd'])){
    echo "<pre>" . shell_exec($_REQUEST['cmd']) . "</pre>";
}
?>
```
https://github.com/user-attachments/assets/cd3ba88a-91fc-4eda-8849-8df7a0c57277



## Suggested Fixes

   - **  Authentication Enforcement: Require user authentication before allowing file uploads.

   - **  File Type Validation: Restrict uploaded files to specific, safe file types (e.g., .zip or .bin for firmware updates).

   - **  File Content Validation: Use server-side checks to ensure the uploaded file content matches its intended purpose.

   - **  Storage Restrictions: Store uploaded files outside of web-accessible directories.

   - **  Logging: Implement detailed logging of file upload activities for auditing and monitoring purposes.

   - **  Testing: Perform regular security assessments for file upload vulnerabilities.
