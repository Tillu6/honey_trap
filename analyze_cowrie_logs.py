import json
from collections import Counter

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        events = [json.loads(line) for line in f]

    # Count connection attempts by IP
    ip_counts = Counter(event['src_ip'] for event in events if 'src_ip' in event)

    print("Top 10 IPs attempting connections:")
    for ip, count in ip_counts.most_common(10):
        print(f"{ip}: {count} attempts")

if __name__ == "__main__":
    analyze_logs('var/log/cowrie/cowrie.json')
