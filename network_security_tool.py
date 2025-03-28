import argparse
from network_scanner import scan_network, scan_ports
from network_monitor import monitor_network

def main():
    parser = argparse.ArgumentParser(description="Network Security Tool")
    parser.add_argument("-s", "--scan", help="Scan network for active devices", action="store_true")
    parser.add_argument("-p", "--ports", help="Scan open ports on a target IP", type=str)
    parser.add_argument("-m", "--monitor", help="Monitor network traffic", action="store_true")
    
    args = parser.parse_args()

    if args.scan:
        network = input("Enter network range (e.g., 192.168.1.1/24): ")
        devices = scan_network(network)
        for device in devices:
            print(f"IP: {device['IP']}, MAC: {device['MAC']}")

    if args.ports:
        target_ip = args.ports
        open_ports = scan_ports(target_ip)
        print(f"Open Ports on {target_ip}: {open_ports}")

    if args.monitor:
        monitor_network()

if __name__ == "__main__":
    main()
