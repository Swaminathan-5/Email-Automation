import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

def validate_email(email):
    # Basic email regex
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def send_email(sender_email, app_password, to_email, subject, body):
    if not validate_email(to_email):
        raise ValueError("Invalid recipient email address.")
    if not validate_email(sender_email):
        raise ValueError("Invalid sender email address.")

    # Compose the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, to_email, msg.as_string())
    except smtplib.SMTPAuthenticationError:
        raise Exception("Authentication failed. Check your app password and Gmail configuration.")
    except smtplib.SMTPConnectError:
        raise Exception("Could not connect to SMTP server. Check your internet connection.")
    except Exception as e:
        raise Exception(f"SMTP error: {e}")