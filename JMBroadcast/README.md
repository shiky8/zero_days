# JMBroadcast JMB0150  Audio Processor   Vulnerability Disclosure

## Summary

A critical vulnerability has been identified in the  JMBroadcast JMB0150  device, allowing unauthenticated attackers to 
    An attacker can directly access the admin panel without login credentials.
    The API leaks hardcoded administrator passwords in an unprotected response.
    These vulnerabilities can lead to full system compromise.

## Details

- **Vendor:** JMBroadcast
- **Product:** JMB0150
- **Vulnerabilitys Type:**
   - Broken Access Control  (CWE-285))
   - Information Disclosure (CWE-200))
