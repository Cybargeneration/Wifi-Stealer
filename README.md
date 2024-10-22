Here's a **README** file for your GitHub repository:

---

# Wi-Fi Password Extractor (Python)

This is the code demonstrated in the video. The script extracts saved Wi-Fi passwords from a Windows system and sends them via email using an Outlook account. 

## Disclaimer
This code is for **educational purposes only**. Unauthorized use of this script to steal Wi-Fi passwords is illegal and unethical. Please use responsibly.

## Features
- Extracts Wi-Fi network names and passwords saved on the system.
- Sends the extracted data via email using Outlook's SMTP server.
- Runs in the background, waiting for user input to terminate.

## Requirements
- Python 3.x
- `smtplib` (for sending emails)
- `subprocess` (for running system commands)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/wifi-password-extractor.git
cd wifi-password-extractor
```

### 2. Install Required Modules
If not already installed, make sure to have the required modules:

```bash
pip install smtplib
```

### 3. Set Up Outlook Credentials
Open the script and replace the following variables with your Outlook email credentials:
- `sender_email`: Your Outlook email address.
- `receiver_email`: The email address where the data will be sent.
- `password`: The password for your Outlook account or app password.

### 4. Running the Script
Run the script by executing:
```bash
python steal_wifi_passwords.py
```
The script will:
- Retrieve the saved Wi-Fi profiles.
- Extract the passwords associated with those profiles.
- Send the information via email.

### 5. Termination
The script will keep running in the background until you press `Ctrl + C` to exit.

## How It Works

1. **Extracting Wi-Fi Profiles:**
   The script uses the `netsh` command to list all saved Wi-Fi profiles on the system.

2. **Extracting Wi-Fi Passwords:**
   For each profile, the script runs a command to extract the password if available.

3. **Sending Email:**
   The extracted Wi-Fi network names and passwords are sent to the specified email using the SMTP protocol.

## Example Output
The email sent will look like this:
```
Subject: Wi-Fi Credentials

Network: HomeNetwork, Password: mysecurepassword123
Network: WorkNetwork, Password: passwordwork456
```

## Important Notes
- Ensure your Outlook account is properly configured to allow sending emails via SMTP. You may need to enable "Less secure apps" or use an app password.
- This script is intended for educational demonstrations in controlled environments.

## License
This project is licensed under the MIT License.

---

Feel free to update the repository URL and adjust the description as necessary!
