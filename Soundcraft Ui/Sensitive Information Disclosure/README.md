# Soundcraft Ui12 & Ui16 WebSocket Information Disclosure Vulnerability

## Description

The **Soundcraft Ui12** and **Ui16** digital audio mixers contain an **information disclosure vulnerability**, allowing **unauthenticated attackers** to connect to the WebSocket API (`/socket.io/1/websocket/`) and intercept **plaintext administrator credentials**.

The password is stored under `settings.block.pass` within WebSocket communication packets, leading to **unauthorized access** and potential **system compromise**.

---

## Vendor Information

- **Vendor:** Soundcraft (by Harman Professional Solutions)
- **Vendor Homepage:** https://www.soundcraft.com/en

---

## Affected Products

| **Product** | **Model(s)** | **Firmware/Software Version** |
|------------|-------------|------------------------------|
| Soundcraft Ui Series | Ui12, Ui16 | 1.0.7x, 1.0.5x |

---

## Vulnerable Endpoint

- **WebSocket Connection:**  ws://<target-ip>/socket.io/1/websocket/10915727835050161812


---

## Attack Type

- **Type:** Exposure of Sensitive Information  
- **Classification:** Unauthorized Access to Credentials  

---

## Impact

- **Severity:** Critical  

### Description:
The **Soundcraft Ui series** digital mixers contain an **unauthenticated sensitive information disclosure vulnerability**.  
An attacker can connect to the WebSocket server (`/socket.io/1/websocket/`) **without authentication** and intercept **administrator credentials**.

By monitoring WebSocket traffic, an attacker can capture a specific request that begins with:

```
3:::SETS^l.1.dyn.prname^
```

Within this request, the administrator password is exposed **in plaintext** under the key:

```
settings.block.pass
```

### Example:

```
SETS^settings.block.pass^AdminPassword
```


This allows an attacker to extract the admin password, enabling **unauthorized access** to the **Soundcraft Ui web interface**, where they can:
- Modify settings  
- Control audio configurations  
- Disrupt live performances or broadcasts  

---

## Affected Components

- **WebSocket Communication** (`/socket.io/1/websocket/`)  
- **Plaintext Storage of Admin Credentials** in WebSocket Responses  

---

## Attack Vector

- **Access Method:** Remote unauthorized WebSocket connection  
- **Authentication Requirement:** None  
- **Exploit Complexity:** Low  

---

## Proof of Concept (PoC)

### Steps to Reproduce

1. Identify the target **Soundcraft Ui mixer’s** IP address.
2. Establish a **WebSocket connection** to the device:

ws://<target-ip>/socket.io/1/websocket/10915727835050161812

3. Listen for WebSocket messages and identify the request that begins with:

```
3:::SETS^l.1.dyn.prname^
```
4. Extract the **admin password** from the response under `settings.block.pass`:

```
SETS^settings.block.pass^SuperSecretPassword
```
5. Use the extracted password to **log into the Soundcraft Ui web interface**.

### PoC Video

[Demo](https://github.com/user-attachments/assets/6a23708f-4b6a-472c-bafc-bb3d25f15182)

---

# Vulnerability Details

## Vulnerability Type Information

- **Vulnerability Type:** Sensitive Information Disclosure  
- **CWE-ID:** [CWE-200](https://cwe.mitre.org/data/definitions/200.html)  
- **Definition:** The product exposes sensitive information to unauthorized users via WebSocket communication.  

---

## Impact Details

### Impact Type

- **Unauthorized Access:** Attackers can retrieve administrator credentials without authentication.  
- **Full System Compromise:** Once logged in, an attacker can modify audio settings, disrupt live performances, or change critical configurations.  
- **Credential Reuse Attack:** If the same credentials are used across multiple devices, attackers can exploit them elsewhere.  

---

## Suggested Fixes

1. **Enforce Authentication for WebSocket Connections:** Require proper session authentication before granting access.  
2. **Encrypt or Hash Passwords in WebSocket Responses:** Do not transmit credentials in plaintext.  
3. **Restrict WebSocket API Access:** Only allow authorized sessions to retrieve settings data.  
4. **Enable Logging and Monitoring:** Detect and block unauthorized WebSocket access attempts.  
