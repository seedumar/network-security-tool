from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered:
        devices.append({"IP": received.psrc, "MAC": received.hwsrc})

    return devices

# Example usage
network = "192.168.1.1/24"  # Change to match your network
devices = scan_network(network)

print("Active Devices:")
for device in devices:
    print(f"IP: {device['IP']}, MAC: {device['MAC']}")

import socket

def scan_ports(target_ip, ports=[21, 22, 80, 443, 3389]):
    print(f"\nScanning {target_ip} for open ports...")
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

# Example usage
target = "192.168.1.10"  # Change to the target device IP
ports_found = scan_ports(target)

print(f"Open Ports on {target}: {ports_found}")
