# check_hosts.py
import socket
import datetime
import os

hosts = [
    {"name": "Google DNS",     "host": "8.8.8.8",    "port": 53},
    {"name": "Cloudflare DNS", "host": "1.1.1.1",    "port": 53},
    {"name": "GitHub",         "host": "github.com", "port": 443},
    {"name": "Oracle Cloud",   "host": "oracle.com", "port": 443},
]

results = []
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for h in hosts:
    try:
        sock = socket.create_connection((h["host"], h["port"]), timeout=3)
        sock.close()
        status = "UP"
        icon = "✅"
    except (socket.timeout, ConnectionRefusedError, OSError):
        status = "DOWN"
        icon = "❌"

    result = f"[{timestamp}] {icon} {h['name']} ({h['host']}:{h['port']}) — {status}"
    results.append(result)
    print(result)

log_file = os.path.join(os.path.dirname(__file__), "check_report.txt")
with open(log_file, "a", encoding="utf-8") as f:
    f.write("\n".join(results) + "\n\n")

print(f"\nRelatório salvo em check_report.txt")
