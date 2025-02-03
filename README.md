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
### 5. **Electrolink**
   - **Product:** db mozart fm transmitter
   - **Vulnerabilities:**  
     - Cross-Site Scripting (XSS) via `/main0.php`.
     - authenticated File Upload via `/patch.php`.
     - Unauthenticated File Upload via `/upload_file.php`.
     
### 6. Itel Electronics

- **Product:** Itel IP Stream
- **Vulnerabilities:**
  - Broken Access Control allowing unauthenticated WebSocket connections, leading to potential unauthorized access and service disruption.


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
