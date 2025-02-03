# Itel IP Stream WebSocket Vulnerability (Broken Access Control)

## Description
The Itel IP Stream WebSocket API suffers from broken access control, allowing unauthenticated attackers to send administrative commands without proper authorization. This vulnerability enables attackers to change stream settings, manipulate configurations, and potentially disrupt broadcasting services.  


## Vendor Information
**Vendor:** Itel Electronics

**Vendor Homepage:** https://www.itel.it/

## Affected Product(s)
- **Product:** Itel IP Stream  
- **Firmware/Software Version:** 1.7.0.6

## Vulnerability Details
- **Vulnerable Endpoint:** `ws://<target-ip>/` (WebSocket connection)  
- **Attack Type:** Broken Access Control  
- **Classification:** Authentication Bypass via WebSockets  

## Impact
- **Severity:** Critical  
- **Description:**  
  The Itel IP Stream device contains a broken access control vulnerability in its WebSocket API. Once a legitimate user is logged in, an unauthenticated attacker can send commands directly to the WebSocket backend without requiring valid authorization. This allows an attacker to:  
  - Manipulate stream settings  
  - Change configurations  
  - Potentially disrupt the broadcasting service  

## Affected Component(s)
- **WebSocket API** of the Itel IP Stream device  

## Attack Vector
- **Access Method:** Remote access via unauthenticated WebSocket commands  
- **Authentication Requirement:** None (requires only an active logged-in session by a legitimate user)  
- **Exploit Complexity:** Low  


## Proof of Concept (PoC)
### Steps to Reproduce:
1. Ensure a legitimate user is logged in to the web interface of the Itel IP Stream device.  
2. Connect to the WebSocket endpoint (`ws://<target-ip>/`) using a WebSocket client (e.g., `wscat`, `websocat`, or a simple Python script).  
3. Send the following commands to manipulate the system **without authentication**:

    ```plaintext
    SendLog
    RouteMeta true
    SetName Radio_Fiemme_Paganella
    SetUrl1 https://stream3.xdevel.com/audio6s975355-281/stream/icecast.audio5
    SetUrl2 https://stream3.xdevel.com/audio6s975355-281/stream/icecast.audio5
    SetPwd adt
    Login adt
    ```
    https://github.com/user-attachments/assets/9c70f77e-9d52-4a89-a753-33835596fe28

### Impact Examples:
- The attacker can change the station name to `"Radio_Fiemme_Paganella"`.  
- The attacker can change the streaming URLs, redirecting broadcasts to unauthorized sources.  
- The attacker can modify user credentials (`SetPwd/Login adt`), potentially locking out legitimate users.  

## Vulnerability Type Information
- **Vulnerability Type:** Broken Access Control  
- **CWE-ID:** [CWE-284](https://cwe.mitre.org/data/definitions/284.html)  
- **Definition:** The software does not properly enforce access control policies, allowing unauthorized actions.  

## Impact Information
- **Impact Type:**  
  - **Unauthorized Access:** Attackers can modify stream settings without authentication.  
  - **Service Disruption:** Malicious actors can redirect or stop streaming services.  
  - **Credential Manipulation:** Attackers can change credentials, leading to potential account hijacking.  

## Suggested Fixes
- **Implement WebSocket Authentication:** Require token-based authentication for all WebSocket requests.  
- **Session Validation:** Validate each WebSocket request against an active user session.  
- **Restrict WebSocket Access:** Limit WebSocket access to authorized users only.  
- **Logging & Monitoring:** Implement detailed logging of WebSocket requests for auditing and anomaly detection.  
- **Rate Limiting:** Enforce rate-limiting to prevent mass exploitation attempts.  

---

**Disclaimer:** This document is provided for educational and responsible disclosure purposes. The vulnerability should only be tested in environments where you have explicit permission to do so. Unauthorized access to systems is illegal and unethical.
