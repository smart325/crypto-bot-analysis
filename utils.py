import smtplib, os
from email.mime.text import MIMEText

def send_email(subject, body):
    email = os.getenv('GMAIL_EMAIL')
    pwd   = os.getenv('GMAIL_APP_PASSWORD')
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email, pwd)
        server.send_message(msg)
