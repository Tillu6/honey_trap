
# Honey Trap in Kali Linux

![Honeypot Symbol](5c1c5720-1900-4ac6-94fc-33026157e95d.webp)

A simple SSH honeypot designed to detect unauthorized access attempts by simulating an SSH service and recording malicious activity.

## Features
- **Logs connection attempts**: Captures detailed logs of unauthorized connection attempts, including IP addresses, usernames, and authentication methods.
- **Analyzes attacker behavior**: Tracks failed login attempts and behavior patterns, providing insights into the attacker's strategy.
- **Real-time alerts**: Notifies you in real-time when suspicious activity is detected, allowing for immediate action.


## Installation
### Prerequisites:
Ensure you have the following installed on your Kali Linux machine:
- Python 3.x
- Git
- Virtualenv (optional, but recommended)

### Steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tillu6/honey_trap
   cd <repository_directory>
   ```

2. **Set Up Virtual Environment** (Optional but recommended):
   ```bash
   python3 -m venv honeypot_env
   source honeypot_env/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Honeypot**:
   Modify the `config.yaml` file to set up honeypot parameters, including SSH port, logging directory, and alert preferences.
   Example:
   ```yaml
   ssh_port: 22
   log_file: /var/log/honeypot.log
   alert_email: admin@example.com
   ```

## Usage
### Start the Honeypot:
Start the honeypot by running the following command. This will simulate an SSH server, logging any incoming connection attempts.
```bash
bin/cowrie start
```

### Monitor the Logs:
You can analyze the log file to track connection attempts, suspicious activity, and more.
```bash
python analyze_logs.py
```
The `analyze_logs.py` script will process the log file and provide insights into the attacker's actions, including:
- Failed login attempts
- Common usernames and passwords used
- Potential brute-force attack patterns

### Set Up Real-Time Alerts:
Configure your system to send real-time notifications when a suspicious activity pattern is detected (e.g., multiple failed login attempts). This can be achieved by integrating with email or Slack notifications within the `cowrie` configuration or by using custom scripts.

Example of a simple alert script:
```python
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Honeypot Alert'
    msg['From'] = 'honeypot@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('localhost') as server:
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# Example of sending an alert
send_alert('Suspicious activity detected in the honeypot!')
```

## Customization
You can extend this honeypot with additional features, such as:
- **Automated responses**: Set up rules to execute specific actions when certain types of attacks are detected (e.g., blocking IPs, sending fake credentials).
- **Deeper analytics**: Integrate with SIEM tools or databases to perform deeper analysis and track long-term attack trends.

## Conclusion
This simple SSH honeypot can help detect unauthorized access attempts and provide insights into malicious behavior. You can customize and extend it to suit your specific security needs.
