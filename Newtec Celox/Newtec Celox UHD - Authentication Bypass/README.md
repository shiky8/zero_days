# Newtec Celox UHD Authentication Bypass Vulnerability

## Description

The **Newtec Celox UHD** (models: **CELOXA504**, **CELOXA820**) running firmware version **celox-21.6.13** is vulnerable to an authentication bypass. An attacker can exploit this issue by modifying intercepted responses from the `/celoxservice` endpoint. By injecting a forged response body during the `loginWithUserName` flow, the attacker can gain **Superuser** or **Operator** access without providing valid credentials.

---

## Vendor Information

- **Vendor:** Newtec (ST Engineering iDirect)  
- **Vendor Homepage:** [https://www.newtec.com/](https://www.newtec.com/)

---

## Affected Products

- **Product:** Newtec Celox UHD  
  - **Models:** CELOXA504, CELOXA820  
  - **Firmware Version:** celox-21.6.13

---

## Vulnerability Type

- Authentication Bypass  
- Broken Authentication / Insecure Authorization Flow

---

## Vulnerable Endpoint(s)

- `/celoxservice`  
- `/`

---

## Exploit Summary

The vulnerability exists due to weak validation of the server's response during the login flow. An attacker can:

1. Intercept the HTTP response from the `/celoxservice` endpoint.
2. Replace it with a forged payload granting Superuser or Operator access.
3. The frontend blindly accepts this modified response, allowing login without verifying the password.

---

## Impact

- Full unauthorized access to Superuser or Operator functions  
- No password verification needed if response is modified  
- Remote compromise of device and configuration on exposed networks

---

## Proof of Concept (PoC)

### ✅ Step 1: Intercept the Login Request

Initiate login via the web interface — the frontend sends a `loginWithUserName` request to `/celoxservice`.

### ✅ Step 2: Modify the HTTP Response

Replace the original response with:

**Superuser Payload**
```
//OK[4,3,2,3,1,["[Ljava.lang.String;/2600011424","1234","NEWTEC Superuser","Superuser"],0,7]
```


**Operator Payload**
```
//OK[4,3,2,3,1,["[Ljava.lang.String;/2600011424","1234","Test operator","OPERATOR"],0,7]
```

### ✅ Step 3: Forward the Modified Response

- The frontend accepts the fake response.
- The attacker is logged in as Superuser or Operator.

### Example Using Intercepting Proxy (e.g., Burp Suite)

1. Start intercepting proxy.
2. Attempt login with any credentials.
3. Intercept response from `/celoxservice`.
4. Replace body with one of the crafted payloads.
5. Forward the response — the attacker is now authenticated with elevated privileges.

---

## **PoC Video**  

https://github.com/user-attachments/assets/439c2551-1b77-4fa1-aa3b-c7f698a7b50f

---

## Vulnerability Classification

- **CWE-287** – Improper Authentication  
- **CWE-303** – Incorrect Implementation of Authentication Algorithm  
- **CWE-302** – Authentication Bypass by Assumed-Immutable Data

---

## Suggested Fixes

- Implement server-side validation of login credentials and session tokens.
- Sign and verify server responses to prevent tampering.
- Apply secure session management and use encrypted transport (e.g., HTTPS).
- Ensure backend-side role validation before granting access to any privileged functionality.

---

## Impact Type

- Privilege Escalation  
- Full Administrative Control  
- Unauthorized Access  
- Configuration and Network Compromise

---

## Mitigation & Workaround

- Restrict management interface access to trusted/internal networks.
- Use VPN or firewall to isolate access.
- Monitor login activity and alert on anomalous access behavior.
