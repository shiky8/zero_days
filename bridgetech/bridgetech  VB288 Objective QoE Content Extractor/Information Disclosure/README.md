# bridgetech VB288 Objective QoE Content Extractor Information Disclosure Vulnerability

## Too lazy to write details, so here’s the description of the device from the vendor’s website
---
## Description

The VB288 is a software-only solution from Bridge Technologies that runs on standard, off-the-shelf server hardware. It was specifically designed to monitor video and audio quality across multiple broadcast streams, using Objective Quality of Experience (QoE) metrics rather than subjective scoring systems like MOS (Mean Opinion Score).

Bridge Technologies is a Norwegian company based in Oslo that specializes in advanced monitoring, analysis, and quality assurance systems for digital media and telecommunications. Their solutions ensure high service quality across broadcast, cable, satellite, OTT, IPTV, and home networks, safeguarding content delivery for over 1.2 billion subscribers and thousands of channels worldwide
## Who Uses These Devices?

These solutions are primarily used by:

Broadcast and media companies (TV stations) operating studios,professional streamers, head-ends, and remote production environments.

Telecom, cable, satellite, and OTT providers ensuring service quality across networks.

Network engineers and QA teams needing real-time and historic insight into media delivery.

Remote production and field engineers deploying NOMAD in dynamic environments.

Large-scale operations.

---

## Vendor Information
- **Vendor:** bridgetech
- **Vendor Homepage:** [https://bridgetech.tv/](https://bridgetech.tv/)

---

## Affected Products
- **Product:** bridgetech VB288 Objective QoE Content Extractor


- **Built Version:** Jul 1 2025 12:43:42
- **Firmware Version:**  5.6.0-8

---

## Vulnerable Endpoints
- `/vbc/data/rdplist`  


---

## Attack Type
- **Type:** Information Disclosure  
- **Classification:** Improper Authorization  

---

## Impact
**Severity:** High  
---
## Attack Vector
- **Access Method:** Remote, over HTTP  
- **Authentication Requirement:** None (unauthenticated)  
- **Exploit Complexity:** Low (simple HTTP requests)  

---

## Proof of Concept (PoC)
make a get requste for his endpoints

{target}/extractor/core/setup/passwd?Change=1&=&passwd2=slvisolp&submitflash=OK&secs=1756630638395


this will show you the admin password


---

## PoC Video


https://github.com/user-attachments/assets/f678a8af-fe20-445b-9aec-7b53fff45959
