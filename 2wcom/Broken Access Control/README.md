# 2wcom IP-4c Vulnerability Disclosure: Broken Access Control

##  Description

The 2wcom IP-4c device suffers from a **Broken Access Control** vulnerability.  
Certain sensitive endpoints are intended to be accessible only after the **admin** explicitly grants access to a manager-level account.  
However, a manager-level user can **bypass these controls** by intercepting and modifying requests in tools like Burp Suite.

---

## Vendor Information

- **Vendor**: 2wcom  
- **Vendor Homepage**: https://www.2wcom.com/

## 🎯 Affected Product

**Device:** 2wcom IP-4c  
**Firmware/Software Bundle:** 2.15.5  
**File/Recovery System:** 2.78 / 2.02  
**App Version:** 2.15.16  
**Webinterface:** 3.54  
**FPGA:** 1.12b64 / 0  
**System Controller:** 1.07  
**SNMP MIB:** 4.4  
**Kernel:** 2wcom-01.25-rt60  
**Codec Versions:**  
- MP2 encoder: 1.5.0  
- MP2 decoder: 2.3.0  
- MP3 encoder: 5.12.1  
- MP3 decoder: 5.6.0  
- AAC encoder: 3.10.0  
- xHE-AAC encoder: 04.05.04  
- AAC decoder: 2.12.1  
- Opus: 1.5.2  
- E-aptX: 1.7  
**HW Revision XPS/IF:** 1.02 / 1.10  

---



## ⚠️ Vulnerability Overview

**Type:** Broken Access Control  
**Impact:** Manager-level users can access **admin-only endpoints** without proper authorization, leading to potential configuration changes, sensitive data leaks, or service disruptions.

---

## 🔓 Vulnerable Endpoints

The following endpoints are exposed to manager-level users without proper checks:

```json
/cwi/ajax_request/get_data.php
/cwi/ajax_request/get_data.php?store=1
/cwi/global.php
/cwi/debug.php
/cwi/time.php
/cwi/user.php
/cwi/services.php
/cwi/ntp.php
/cwi/ember.php
/cwi/tcpip.php
/cwi/snmp.php
/device/ip4c_mib.zip
/cwi_audio/switch.php
/cwi/ajax_request/log_out.php
/sdp/AES67-sender-1.sdp
/cwi/ajax_request/debugReport_scriptInfo.php
```

---

## 🛠️ Exploitation Steps

1. **Login** to the web interface as a manager-level user.  
2. **Intercept any request** using a tool like Burp Suite.  
3. **Modify the endpoint** in the intercepted request to one of the vulnerable endpoints listed above.  
4. **Send the modified request**, bypassing the intended access control checks.

---

## 💡 Example Exploit Flow

- A manager-level user logs in normally and **does not** have access to `/cwi/debug.php`.
- In Burp Suite, they intercept a request (e.g., to `/cwi/dashboard.php`) and change the endpoint to `/cwi/debug.php`.  
- The server **does not properly enforce** access control, and the manager-level user can now access or manipulate functions that should only be accessible to the admin.

---

## Proof of Concept (PoC) for(RCE,Information Disclosure,Broken Access Control)
https://github.com/user-attachments/assets/42bc93b9-cc75-47bf-bae4-e33f6f87a3ce

---

## 🔑 Impact

- **Elevation of privileges:** Managers gain admin-level functionality.  
- **Access to sensitive system configurations** (network settings, user management, etc.).  
- **Potential for misconfigurations or denial of service** if misused.  

---

## ✅ Suggested Fixes

- Implement **strict access control** checks on all sensitive endpoints to ensure only authorized roles (e.g., admin) have access.  
- **Audit** all access control logic in the web interface.  
- **Update firmware** to the latest version (if a fix is released).  
- Restrict management interface access to **trusted IPs**.

---

## Workarounds

  * Restrict access to /cwi/* , /sdp/* , /cwi_audio/* and /device/*   endpoints using firewall rules or VPN

  * Monitor system logs for suspicious ping tool usage

