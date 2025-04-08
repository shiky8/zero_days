# Zero Days

This repository contains detailed information about **zero-day vulnerabilities** discovered in various systems and devices. The purpose of this repository is to document and raise awareness about critical security flaws, their impact, and potential fixes. The vulnerabilities are categorized by vendor and product for easy navigation.

---

## Repository Structure

The repository is organized into directories, each corresponding to a specific vendor or product. Below is an overview of the directories and their contents:

### 1. **GatesAir**
   - **Product:** Maxiva UAXT , VAXT Transmitter  
   - **Vulnerabilities:**  
     - Remote Code Execution (RCE) via `/json` endpoint.  
     - Information Disclosure via `/logs/devcfg/` endpoints.  
     - Session Hijacking via `/logs/debug/` endpoints.  

### 2. **WorldCast Systems**
   - **Product:** ECRESO FM/DAB/TV Transmitter  
   - **Vulnerabilities:**  
     - Privilege Escalation via `/wscom` endpoint.  

### 3. **BW Broadcast**
   - **Product:** Transmitter Management System  
   - **Vulnerabilities:**  
     - Session Hijacking via exposed log files.  

### 4. **Electrolink**
   - **Product:** FM/DAB/TV Transmitter Web Management System  
   - **Vulnerabilities:**  
     - Credentials Disclosure via `/controlloLogin.js`.
### 5. **DB Electronica Mozart**
   - **Product:** Mozart FM Transmitter
   - **Vulnerabilities:**  
     - Cross-Site Scripting (XSS) via `/main0.php`.
     - authenticated File Upload via `/patch.php`.
     - Unauthenticated File Upload via `/upload_file.php`.
     
### 6. Itel Electronics

- **Product:** Itel IP Stream
- **Vulnerabilities:**
  - Broken Access Control allowing unauthenticated WebSocket connections, leading to potential unauthorized access and service disruption.

### 7. ELCA Electronics

- **Product:** ELCA Star Transmitter Remote Control
- **Vulnerabilities:**
  - Information Disclosure via an unprotected endpoint, leading to potential unauthorized access.

### 8. Soundcraft Ui 

- **Product:** Soundcraft Ui Series (Ui12, Ui16)
- **Vulnerabilities:**
  - Information Disclosure via an unprotected endpoint, leading to potential unauthorized access.

### 9. Nautel 

- **Product:** Nautel VX Series
- **Vulnerabilities:**
  - Remote Code Execution via Unauthorized Firmware Modification.

### 10. Orban 

- **Product:** Orban OPTIMOD 5950 Audio Processor
- **Vulnerabilities:**
  - Broken Access Control via Client-Side Manipulation.

### 11. JMBroadcast 

- **Product:** JMBroadcast JMB0150
- **Vulnerabilities:**
  - Broken Access Control.
  - Information Disclosure.

### 12. DAEnetIP4 

- **Product:** DAEnetIP4 METO
- **Vulnerabilities:**
  - Session Hijacking via `/login_ok.htm` endpoints.

### 13. Elber 

- **Product:** Elber REBLE310
- **Vulnerabilities:**
  - Session Hijacking via  `/reble310//indexTH.htm` and `/reble310//indexR.htm` endpoints.

### 14. R.V.R Elettronica 

- **Product:** R.V.R Elettronica TEX
- **Vulnerabilities:**
  -  Broken Access Control via  `/_Passwd.html` endpoints.

### 15.  ITEL Electronics 

- **Product:** ITEL ISO FM SFN Adapter
- **Vulnerabilities:**
  - Session Hijacking via  `/home.html` endpoints.

### 16.  Dasan Networks

- **Product:** Dasan Switch DS2924
- **Vulnerabilities:**
  - Authentication Bypass  via  Cookie-Based.

### 17.  QVidium

- **Product:** QVidium Opera11
- **Vulnerabilities:**
  -  Remote Code Execution  via  `/net_ping.cgi` endpoint.

### 18.  Sencore

- **Product:** Sencore SMP100 SMP Media Platform
- **Vulnerabilities:**
  -  Session Hijacking  via  `/UserManagement.html` endpoint.

### 19.  Eurolab

- **Product:** Eurolab ELTS100_UBX GPS
- **Vulnerabilities:**
  -  Broken Access Control via Endpoints.

### 20.  axeltechnology

- | Product | Firmware Version |
  |---------|------------------|
  | WOLF1MS | 0.8.5 to 1.0.3 |
  | WOLF2MS | 0.8.5 to 1.0.3 |
  | puma | 0.8.5 to 1.0.3 |
  | StreamerMAX MK II | 0.8.5 to 1.0.3 |
- **Vulnerabilities:**
  -  Broken Access Control via Endpoints.

### 21.  ITEL Electronics DAB

- | Product     | Firmware Version |
  |-------------|------------------|
  | DAB Mux     | c041640a         |
  | DAB Encoder | 25aec8d          |
  | DAB Gateway | c041640a         |
- **Vulnerabilities:**
  -  Authentication Bypass via Endpoints.

### 22.  Newtec Celox

- **Product:** Newtec Celox UHD
- **Vulnerabilities:**
  -  Authentication Bypass  via  `/celoxservice` endpoint.
  -  Privilege Escalation

### 23. **ENENSYS Technologies**
   - | Product          | Firmware Version | Vulnerabilitys Type                                                                        |
     |------------------|------------------|--------------------------------------------------------------------------------------------|
     | IPGuard V2       | 2.10.0         | Information Disclosure Leading to Unauthorized Access (CWE-798,CWE-200,CWE-522)              |
     | ENENSYS ATSC3.0  | 1.6.1          | Authentication Bypass via JWT Reuse and HTTP Response Manipulation (CWE-287,CWE-345,CWE-384) |

### 24. **NovelSat Ltd**
   - | Product     | Firmware Version | Vulnerabilitys Type                                                                             |
     |-------------|------------------|-------------------------------------------------------------------------------------------------|
     | NS2000  Satellite Modem        | NS3000.7.x | **unauthenticated session hijacking** and **administrative access** (CWE-306,CWE-285,CWE-640,CWE-434)              |
     | NS3000 Satellite Modem         | NS2000.x         | **unauthenticated session hijacking** and **administrative access** (CWE-306,CWE-285,CWE-640,CWE-434)   |





---

## Key Features of the Repository
- **Detailed Vulnerability Reports:** Each directory contains a detailed description of the vulnerabilities, including affected endpoints, attack vectors, and impact.  
- **Suggested Fixes:** Recommendations for mitigating the vulnerabilities are provided to help vendors and users secure their systems.  
- **CWE and CVE References:** Vulnerabilities are mapped to Common Weakness Enumeration (CWE) and Common Vulnerabilities and Exposures (CVE) where applicable.  
- **Educational Purpose:** This repository is intended for educational and research purposes to promote awareness and improve cybersecurity practices.  

---

## How to Use This Repository
1. Navigate to the directory corresponding to the vendor or product of interest.  
2. Review the vulnerability details, including the affected endpoints, attack types, and impact.  
3. Refer to the suggested fixes to understand how to mitigate the vulnerabilities.  
4. Use the information responsibly and only with proper authorization.  

---

## Disclaimer
This repository is for **educational and research purposes only**. The vulnerabilities described here are intended to raise awareness and help improve the security of affected systems. Use this information responsibly and only with proper authorization. The maintainers of this repository are not responsible for any misuse of the information provided.

---

## Contributing
If you would like to contribute to this repository by adding new vulnerabilities or improving existing documentation, please follow these steps:  
1. Fork the repository.  
2. Create a new branch for your changes.  
3. Submit a pull request with a detailed description of your changes.  

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or feedback, please open an issue in the repository or contact the maintainers directly.
