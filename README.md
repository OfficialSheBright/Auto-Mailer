# SheBright Auto Mailer

## Overview
This script (`send_invite.py`) automates the process of sending invitation emails for the SheBright community. It reads recipient details from an Excel file and sends personalized HTML emails using an SMTP server.

## Features
- Loads email credentials securely from a `.env` file
- Reads recipient names and emails from an Excel sheet
- Sends HTML-formatted emails with embedded SheBright social links
- Implements a delay mechanism to avoid spam detection
- Provides detailed logging for sent emails

## Prerequisites
Ensure you have the following installed before running the script:

- Python 3.12+
- Required Python packages:
  - `python-dotenv`
  - `pandas`
  - `openpyxl`
  - `smtplib`
  - `email`

## Installation

1. Clone the repository or download the script.
2. Install dependencies:
   ```sh
   pip install python-dotenv pandas openpyxl
   ```
3. Create a `.env` file in the project directory and add:
   ```sh
   SENDER_EMAIL_PASSWORD=your_email_password_here
   ```
   Replace `your_email_password_here` with your actual email password or app password (if using Gmail with 2FA enabled).

## Usage

1. Ensure your email list is stored in an Excel file (`Untitled spreadsheet.xlsx`) with at least two columns:
   - `Email` (Recipient email addresses)
   - `Name` (Recipient names)

2. Run the script:
   ```sh
   python send_invite.py
   ```

3. The script will:
   - Connect to the SMTP server
   - Read email recipients from the Excel file
   - Send customized invitation emails
   - Introduce pauses after every 10 emails to avoid rate limits

## SMTP Configuration
By default, the script uses Gmail SMTP (`smtp.gmail.com` on port `465`). If using another email provider, update the following in the script:
```python
SMTP_SERVER = "your_smtp_server"
SMTP_PORT = your_smtp_port
```

## Troubleshooting
- **Connection Closed Error:** Ensure your email provider allows SMTP access. For Gmail, enable [Less Secure Apps](https://myaccount.google.com/security) or use an App Password.
- **Missing `.env` Value Error:** Check that `SENDER_EMAIL_PASSWORD` is correctly set in the `.env` file.
- **Excel File Not Found:** Ensure the file `Untitled spreadsheet.xlsx` exists in the script directory and contains the required columns.

## Contribution
Feel free to improve this script by submitting a pull request or reporting issues.

## License
This project is open-source under the MIT License.

