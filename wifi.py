import subprocess, json

print("Scanning WiFi...")

try:
    result = subprocess.run(["termux-wifi-scaninfo"], capture_output=True, text=True)
    networks = json.loads(result.stdout)
    print(f"Found {len(networks)} networks:\n")
    for net in networks:
        print(f"Name: {net.get('ssid')}")
        print(f"Signal: {net.get('rssi')} | Frequency: {net.get('frequencyMhz')} MHz")
        print("-" * 30)
except Exception as e:
    print("Install Termux API first:")
    print("pkg install termux-api")
    print(e)
