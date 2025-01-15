
import smtplib

def send_alert(message):
    sender_email = "18r91a04e1@gmail.com"  # Replace with your email
    receiver_email = "sakethreddy015@gmail.com" # Replace with recipient email

    # Generate a secure app password from Google
    password = "pvyi qqld jppc pofk "  # Replace with your app password

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)  # Log in to the server
            server.sendmail(sender_email, receiver_email, message)  # Send the email
            print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send alert: {e}")

if __name__ == "__main__":
    send_alert("Suspicious activity detected on your honeypot!")
