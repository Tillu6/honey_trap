import json
from collections import Counter
import matplotlib.pyplot as plt

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        events = [json.loads(line) for line in f]

    # Count connection attempts by IP
    ip_counts = Counter(event['src_ip'] for event in events if 'src_ip' in event)
    return ip_counts

def visualize_attempts(ip_counts):
    ips, counts = zip(*ip_counts.most_common(10))
    plt.bar(ips, counts, color='skyblue')
    plt.xlabel('IP Addresses')
    plt.ylabel('Connection Attempts')
    plt.title('Top 10 Attackers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    log_file = 'var/log/cowrie/cowrie.json'
    ip_counts = analyze_logs(log_file)
    visualize_attempts(ip_counts)
