# ELCA Star Transmitter Remote Control - Information Disclosure Vulnerability

## Description
The **ELCA Star Transmitter Remote Control** firmware contains an **information disclosure vulnerability**, allowing **unauthenticated attackers** to retrieve **admin credentials** and **system settings** via an unprotected `/setup.xml` endpoint.  
The **admin password is stored in plaintext** under the `<p05>` XML tag, potentially leading to **remote compromise** of the transmitter system.


## Vendor Information
**Vendor:** ELCA Electronics

**Vendor Homepage:** 

## Affected Products & Versions
- **Product**: ELCA Star Transmitter Remote Control  
- **Firmware/Software Versions**:
  - STAR150
  - BP1000
  - STAR300
  - STAR2000
  - STAR1000
  - STAR500

## Vulnerable Endpoint(s)
- ** /setup.xml


## Attack Type
- **Type**: Exposure of Sensitive Information  
- **Classification**: Unauthorized Access to Credentials  

## Impact
- **Severity**: **Critical**
- **Description**:  
  The **ELCA Star Transmitter Remote Control** firmware contains an **unauthenticated sensitive information disclosure vulnerability**.  
  An attacker can retrieve **administrator credentials** and other **system configuration details** by sending an **unauthenticated GET request** to `/setup.xml`.  
  The XML response contains the **admin password in the `<p05>` field**, allowing a remote attacker to **gain full administrative access** to the system.

## Affected Component(s)
- **Setup Configuration XML File (`setup.xml`)**

## Attack Vector(s)
- **Access Method**: Remote unauthorized access via HTTP `GET` request  
- **Authentication Requirement**: None  
- **Exploit Complexity**: Low  

## Proof of Concept (PoC):
# Steps to Reproduce:

  - **  Identify the target transmitter IP address.

  - **  Send an unauthenticated GET request to /setup.xml.

```bash

curl http://<target-ip>/setup.xml
```

 - ** Look for the <p05> field in the response, which contains the admin password in plaintext:

   ```xml
    <setup>
      <p01>SomeSetting</p01>
      <p02>AnotherSetting</p02>
      ...
      <p05>SuperSecretAdminPassword</p05>
      ...
    </setup>
   ```

  - **  Use the extracted credentials to log in and gain full control of the transmitter system.

# poc video
[demo](https://github.com/user-attachments/assets/c7abba30-bc32-4b97-84b5-d094c76dc4d3)

## Vulnerability Type Info
- **Vulnerability Type**: **Sensitive Information Disclosure**  
- **CWE-ID**: [CWE-200](https://cwe.mitre.org/data/definitions/200.html)  
- **Definition**: The product exposes sensitive information to unauthorized users.  

## Impact Info
- **Unauthorized Access**: Attackers can retrieve **administrator credentials** without authentication.  
- **Full System Compromise**: Once logged in, an attacker can **change configurations, disrupt operations, or take full control** of the transmitter.  
- **Credential Reuse Attack**: If the same credentials are used across multiple transmitters, attackers can **exploit them elsewhere**.  

## Suggested Fixes
- **Restrict Access to `/setup.xml`**: Ensure that the file **is not accessible** without authentication.  
- **Remove Password Storage in Plaintext**: Encrypt stored credentials instead of exposing them in plaintext XML.  
- **Implement Proper Authorization Controls**: Require **admin authentication** before accessing sensitive configuration files.  
- **Enable Logging and Monitoring**: Monitor access to configuration files and **generate alerts** for unauthorized attempts.  

---

### Disclaimer
This information is provided **for educational and security research purposes only**. Unauthorized access to systems without permission is illegal.  

---

### References
- [Common Weakness Enumeration (CWE-200)](https://cwe.mitre.org/data/definitions/200.html)  
