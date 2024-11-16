'''
Copyright: (C) Sergius Nyah 2023-12-17
'''

# Import the settings from the settings.py file
# Contains the configuration settings for the email sender.
from config import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import imaplib
import sys
import email
import getpass

# Use the settings in your email sending code
server = settings.EMAIL_HOST
port = settings.EMAIL_PORT
username = settings.EMAIL_USERNAME
password = settings.EMAIL_PASSWORD
sender = settings.DEFAULT_SENDER
recipient = settings.DEFAULT_RECIPIENT
subject = settings.EMAIL_SUBJECT

# Create a multipart message and set headers
def send_email(attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()

    msg.attach(MIMEText(settings.EMAIL_BODY, 'plain'))
    if attachment_path is not None:
        with open(attachment_path, 'rb') as attachment:
            file = MIMEBase('application', 'octet-stream')
            file.set_payload(attachment.read())
            encoders.encode_base64(file)
            file.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
            msg.attach(file)

    email = input('Enter your Email: ')
    password = getpass.getpass('Enter your password: ')
    server.login(email, password)
    server.sendmail(sender, recipient, msg.as_string())

    server.quit()

def receive_emails():
    mail = imaplib.IMAP4_SSL(settings.IMAP_HOST)
    mail.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
    mail.select('inbox')

    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()

    emails = []
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        email_from = msg['from']
        email_subject = msg['subject']
        email_body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    email_body = part.get_payload(decode=True).decode()
                    break
        else:
            email_body = msg.get_payload(decode=True).decode()
        emails.append({'from': email_from, 'subject': email_subject, 'body': email_body})

    mail.logout()
    return emails


if __name__ == '__main__': # Checks the main function in (command_parser.c)
    # Checks if attachment file was provided
    if len(sys.argv)>1:
        attachment_path = sys.argv[1]
    else:
        attachment_path = None
    # Send the email to the recipient
    send_email(settings.DEFAULT_RECIPIENT, settings.EMAIL_SUBJECT, settings.EMAIL_BODY, attachment_path)
