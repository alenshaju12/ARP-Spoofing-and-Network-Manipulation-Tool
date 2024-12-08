 ARP Spoofing and Network Manipulation Tool

 This Python script demonstrates **ARP Spoofing** (also known as **ARP Poisoning**) using the **Scapy** library.
 It allows for network manipulation by impersonating devices on the local network, which can be used for **Man-in-the-Middle (MitM) attacks**
 and also to **degrade network performance** (e.g., slowing down the network, causing delays, and packet loss).

 > **Warning**: This tool is intended solely for educational purposes and ethical hacking within networks you have explicit permission to test. 
 Unauthorized use can lead to legal consequences.

 ## Features

 - **ARP Spoofing**: Spoofs the ARP tables of both the target device and router, making them believe the attacker's machine is the other party. 
   This enables traffic interception, modification, and routing through the attacker’s machine.
 
 - **Network Degradation**: Causes **slow network speeds**, **increased latency**, and **packet loss** for the target device. 
   By redirecting traffic through the attacker, network performance can be deliberately degraded.

 - **ARP Request Broadcasting**: Sends ARP requests to refresh ARP caches, ensuring the spoofed entries remain active in the network.

 - **Continuous Spoofing**: Runs in a loop to maintain the attack, keeping the ARP tables poisoned and the network performance disrupted.

 ## How it Works

 1. **ARP Spoofing**: The script sends ARP reply packets to both the target device and router. The target device is led to believe the attacker's machine is the router,
    and the router is led to believe the attacker's machine is the target device.

 2. **Network Interruption**: With the traffic being funneled through the attacker’s machine, network performance for the target device can degrade, 
    leading to **slower speeds**, **delayed packets**, and potential **packet loss**.

 3. **ARP Request Broadcasting**: The attacker periodically sends ARP requests to refresh the ARP tables in the network, maintaining the spoofed connections.

 4. **Ongoing Disruption**: The script continuously sends spoofed ARP replies to keep the network in a poisoned state, ensuring ongoing degradation of the target device’s network performance.

 ## Requirements

 - Python 3.x
 - Scapy library: Install it using:

 ```bash
 pip install scapy
 ```

 ## Usage

 1. Clone this repository and navigate to the script’s directory.
 2. Edit the script to specify the correct IP and MAC addresses for the target device, router, and attacker.
 3. Run the script with administrative privileges (root or sudo) to allow ARP packets to be sent.

    ```bash
    sudo python arp_spoof.py
    ```

 4. Observe the network performance of the target device as the network speed slows down, delays increase, and packets may be lost due to the ARP poisoning.

 ## Disclaimer

 This tool is designed for **network security testing** and **educational purposes** only. It should **not be used for illegal or unauthorized access** to networks or devices.
 Always ensure you have permission to conduct any tests on a network.

 By using this script, you agree to take full responsibility for your actions and ensure that the tool is used ethically and within legal boundaries.
