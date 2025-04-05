# Newtec Celox Vulnerability Disclosure

## Summary

A critical vulnerability has been identified in the  Newtec Celox devices, Attackers can injecting a forged response body during the `loginWithUserName` flow, the attacker can gain **Superuser** or **Operator** access without providing valid credentials.

## Details

- **Vendor:** ITEL Electronics
- | Product     | Firmware Version |
  |-------------|------------------|
  | Celox UHD     | 21.6.13         |
  | CELOXA504 | 21.6.13          |
  | CELOXA820| 21.6.13         |

- **Vulnerabilitys Type:**  Authentication Bypass via  Endpoint   (CWE-287 , CWE-384))

