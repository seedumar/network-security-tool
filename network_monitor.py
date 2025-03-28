import psutil
import time

def monitor_network(interval=5):
    print("\nMonitoring Network Traffic...\n")
    while True:
        stats = psutil.net_io_counters()
        sent = stats.bytes_sent / 1024
        received = stats.bytes_recv / 1024

        print(f"Data Sent: {sent:.2f} KB | Data Received: {received:.2f} KB")
        time.sleep(interval)

# Start monitoring
monitor_network()
