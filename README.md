
# Honey Trap in Kali Linux

![Honeypot Symbol](5c1c5720-1900-4ac6-94fc-33026157e95d.webp)


## Project Overview
This project demonstrates the creation of a **honey trap** using **Kali Linux** to detect and log unauthorized access attempts. By simulating a vulnerable service, the honey trap attracts malicious actors attempting to exploit the service. The project uses **Cowrie**, a popular SSH honeypot, to mimic an insecure environment, collect data on attempted intrusions, and provide real-time alerts for suspicious activities.

## Key Features
- **Deception Environment**: A fake vulnerable SSH service is set up to attract attackers.
- **Intrusion Detection**: Logs all incoming connection attempts, including failed login attempts.
- **Data Analysis**: Analyzes attack patterns to gain insights into the intruders' tactics.
- **Alert System**: Sends real-time email notifications when suspicious activities are detected.

## Tools and Technologies
- **Honeypot Framework**: Cowrie (SSH-based honeypot).
- **Platform**: Kali Linux.
- **Programming Languages**: Python, Bash.
- **Log Analysis**: Kibana, Splunk, or custom Python scripts.
- **Alerting System**: Email alerts using Python's SMTP library.
- **Visualization**: Matplotlib (for visualizing attack patterns).

## How It Works
1. **Simulated Vulnerable Service**:
   - A fake SSH service (port 2222) is set up using Cowrie.
   - Attackers interact with the honeypot, attempting login and exploitation.

2. **Data Collection**:
   - All activities are logged in JSON and text formats, detailing attacker actions such as login attempts and commands executed.

3. **Analysis**:
   - The collected logs are analyzed to detect trends in attack attempts, such as frequently targeted IPs and common attack vectors.
   - Visualizations are created to present the findings.

4. **Alerting**:
   - A Python script sends an email alert whenever suspicious activity is detected.

## Setup Instructions
### 1. Install Dependencies
Ensure Kali Linux is installed and updated:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
```

### 2. Clone the Repository
```bash
git clone https://github.com/Tillu6/honey-trap.git
cd honey-trap
```

### 3. Install and Set Up Cowrie
Clone the Cowrie repository:
```bash
git clone https://github.com/cowrie/cowrie.git
cd cowrie
```

Create a virtual environment and install dependencies:
```bash
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install -r requirements.txt
```

### 4. Configure Cowrie
Modify `cowrie.cfg` to customize the honeypot:
```bash
cp etc/cowrie.cfg.dist etc/cowrie.cfg
nano etc/cowrie.cfg
```
Adjust the following settings:
- Change `hostname` to your desired fake server name.
- Set `sshPort` to `2222` or any other unused port.

### 5. Start the Honeypot
```bash
bin/cowrie start
```

## Data Analysis
### 1. Analyze Logs
Cowrie stores logs in the `var/log/cowrie/` directory. To analyze logs:
```python
import json
from collections import Counter

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        events = [json.loads(line) for line in f]

    ip_counts = Counter(event['src_ip'] for event in events if 'src_ip' in event)

    print("Top 10 IPs attempting connections:")
    for ip, count in ip_counts.most_common(10):
        print(f"{ip}: {count} attempts")

if __name__ == "__main__":
    analyze_logs('var/log/cowrie/cowrie.json')
```
![image](https://github.com/user-attachments/assets/fdec5716-d285-4867-b13e-dd551cec17f2)

### 2. Visualize Data
Use Matplotlib to visualize attack patterns:
```python
import matplotlib.pyplot as plt

def visualize_attempts(ip_counts):
    ips, counts = zip(*ip_counts.most_common(10))
    plt.bar(ips, counts)
    plt.xlabel('IP Addresses')
    plt.ylabel('Connection Attempts')
    plt.title('Top 10 Attackers')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
```
![image](https://github.com/user-attachments/assets/20e42f7c-bd9b-441e-bbde-c44c2ef5f290)

## Real-Time Alerts
Set up an alert system to notify you of suspicious activities via email:
```python
import smtplib

def send_alert(message):
    sender_email = "your_email@example.com"
    receiver_email = "alert_receiver@example.com"
    password = "your_password"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

send_alert("Suspicious activity detected on your honeypot!")
```
![image](https://github.com/user-attachments/assets/b462a07f-a792-4847-9de9-41b6333765af)

## Where Can This Be Used?
- **Security Research**: Analyze attacker behavior and common attack vectors.
- **Cybersecurity Defense**: Deploy honeypots as part of a broader defense strategy to lure attackers away from real systems.
- **Training and Education**: Teach cybersecurity concepts by demonstrating how attackers interact with vulnerable services.

## Implementation Suggestions
- **Expand to Multiple Protocols**: Implement additional honeypots for HTTP, FTP, or other services.
- **Machine Learning**: Integrate machine learning to classify threats based on attack patterns.
- **Automation**: Set up automatic responses to detected attacks, such as blocking IPs.

## Screenshots
Include any relevant screenshots showing:
- Cowrie logs in action.
- Data visualizations (e.g., top attacker IPs).
- Real-time email alerts.

---

## Contributing
Feel free to fork the repository, create pull requests, and contribute to this project.

---
