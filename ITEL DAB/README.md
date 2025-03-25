# ITEL DAB Vulnerability Disclosure

## Summary

A critical vulnerability has been identified in the  ITEL DAB devices, Attackers can reuse a valid JWT token obtained from one device to authenticate and gain administrative access to any other device running the same firmware, even if the passwords and networks are different.  
This allows **full compromise** of affected devices.

## Details

- **Vendor:** ITEL Electronics
- | Product     | Firmware Version |
  |-------------|------------------|
  | DAB Mux     | c041640a         |
  | DAB Encoder | 25aec8d          |
  | DAB Gateway | c041640a         |

- **Vulnerabilitys Type:**  Authentication Bypass via  Endpoint jwt  (CWE-287 , CWE-384))

