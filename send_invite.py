from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import time

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ SMTP Server Details (GoDaddy SMTP)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL Port

# ✅ Your Email & Password (loaded from .env file)
SENDER_EMAIL = "officialshebright@gmail.com"
SENDER_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")  # Load from .env file

if not SENDER_PASSWORD:
    raise ValueError("⚠️ Error: SENDER_EMAIL_PASSWORD not found in .env file!")

# ✅ Excel File Path (Ensure the file is in the correct location)
excel_file = "Untitled spreadsheet.xlsx"  # ⚠️ Update the file path if needed

# ✅ Email Subject
subject = "✨ Join SheBright – A Community for Empowering Girls in Tech!"

# ✅ SheBright Social Media Links
TELEGRAM = "https://t.me/SheBright"
TWITTER = "https://twitter.com/SheBright"
LINKEDIN = "https://linkedin.com/company/shebright"
DISCORD = "https://discord.gg/shebright"

# ✅ Read Email List from Excel
df = pd.read_excel(excel_file)
email_list = list(zip(df["Email"], df["Name"]))

# ✅ Connect to SMTP Server (SSL Secure Connection)
server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
server.login(SENDER_EMAIL, SENDER_PASSWORD)

for index, (email, name) in enumerate(email_list):
    # ✅ Email Body (HTML Format)
    email_body = f'''
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f7f7f7;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background: linear-gradient(135deg, #ff7eb3, #ff758c);
                color: white;
                padding: 30px 20px;
                text-align: center;
            }}
            .header h1 {{
                margin: 0;
                font-size: 28px;
                font-weight: bold;
            }}
            .content {{
                padding: 30px 20px;
            }}
            .content h2 {{
                color: #ff758c;
                font-size: 24px;
                margin-bottom: 20px;
            }}
            .content p {{
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 20px;
            }}
            .button {{
                display: inline-block;
                padding: 12px 24px;
                margin: 10px 0;
                font-size: 16px;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                transition: background 0.3s ease;
            }}
            .button.telegram {{ background: #0088cc; }}
            .button.twitter {{ background: #1DA1F2; }}
            .button.linkedin {{ background: #0077B5; }}
            .button.discord {{ background: #5865F2; }}
            .button:hover {{ opacity: 0.9; }}
            .footer {{
                text-align: center;
                padding: 20px;
                background: #f1f1f1;
                color: #666;
                font-size: 14px;
            }}
            .footer a {{
                color: #ff758c;
                text-decoration: none;
            }}
            .footer a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1>🌸 Hi {name}, Welcome to SheBright! 🌸</h1>
            </div>
            <div class="content">
                <h2>🚀 Join a Thriving Community of Women in Tech!</h2>
                <p>We are excited to invite you to <strong>SheBright</strong>, a growing community for girls passionate about technology, coding, design, and innovation. 🎉</p>
                <p>At SheBright, you will:</p>
                <ul>
                    <li>💡 Gain access to learning resources and mentorship</li>
                    <li>🤝 Connect with inspiring women in tech</li>
                    <li>🚀 Participate in exclusive workshops and hackathons</li>
                </ul>
                <p>Ready to connect with like-minded women? Join us today! 👇</p>
                <a href="{TELEGRAM}" class="button telegram">Join on Telegram</a>
                <a href="{DISCORD}" class="button discord">Join on Discord</a>
                <a href="{LINKEDIN}" class="button linkedin">Follow on LinkedIn</a>
                <a href="{TWITTER}" class="button twitter">Follow on Twitter</a>
                <hr>
                <p><strong>📩 Stay Connected for Future Opportunities!</strong></p>
            </div>
            <div class="footer">
                <p>For any queries, feel free to contact us at: <a href="mailto:contact@shebright.com">contact@shebright.com</a></p>
                <p>Best regards,<br><strong>The SheBright Team</strong></p>
            </div>
        </div>
    </body>
    </html>
    '''

    # ✅ Setup Email Message
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'html'))

    try:
        # ✅ Send the email
        server.sendmail(SENDER_EMAIL, email, msg.as_string())
        print(f"✅ Email sent to {name} ({email})")
    except Exception as e:
        print(f"❌ Error sending to {name} ({email}): {e}")

    # ✅ To avoid spam detection, wait after every 10 emails
    if (index + 1) % 10 == 0:
        print("⏳ Waiting for 30 seconds to avoid rate limits...")
        time.sleep(30)

# ✅ Close SMTP Server Connection
server.quit()
print("🎉 All SheBright invitations sent successfully!")
