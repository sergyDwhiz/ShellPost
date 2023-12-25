'''
Main Code Description: This piece of software is simply a python script 
that sends emails to a desired recipient with the option of including an
attachment via the Command line/terminal. 

Copyright: (C) Sergius Nyah 2023-12-17
'''

# Import the settings from the settings.py file
# Contains the configuration settings for the email sender. 
from config import settings

# Use the settings in your email sending code
server = settings.EMAIL_HOST
port = settings.EMAIL_PORT
username = settings.EMAIL_USERNAME
password = settings.EMAIL_PASSWORD
sender = settings.DEFAULT_SENDER
recipient = settings.DEFAULT_RECIPIENT
subject = settings.EMAIL_SUBJECT 

# Import the email modules we'll need 
import smtplib # Defines an SMTP client session object that can be used to send mail to any Internet
               # machine with an SMTP or ESMTP listener daemon.

from email.mime.text import MIMEText # For creating MIME objects (Multipurpose Internet Mail Extensions)
                                     # use to create objects of major type text

from email.mime.multipart import MIMEMultipart # MIME obejcts of major type multipart
                                                # use to create objects of major type multipart     

from email.mime.base import MIMEBase # Creates MIME objects of major types other than 
                                     # text, multipart, or message

from email import encoders # Encode and decode MIME 
                           #objects into and out of base64-encoded strings

import sys # For getting the command line arguments
import getpass # Securely gets the password from the user via command line

# Create a multipart message and set headers
def send_email(attachment_path=None):
    #Create a multipart message
    msg = MIMEMultipart()

    # Set email params 
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Set email body
    msg.attach(MIMEText(settings.EMAIL_BODY, 'plain'))

    # Open the attachment file to be sent, if provided
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read()) # Read the attachment file

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header that marks "part" as an attachment
            '''
            Set the attachment filename and add a header to the attachment part.
            f'attachment; filename= {attachment_path}' is a formatted string literal which 
            allows you to embed Python expressions inside a string by prefixing the string with f
            '''
            part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')

            # Add attachment to your email message 
            msg.attach(part)

    # Connect to the email server 
    server = smtplib.SMTP(server, port)
    server.starttls() # Secure the connection

    # Get user credentials
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')

    # Login to the email server
    server.login(username, password)

    # Send the email
    server.sendmail(sender, recipient, msg.as_string())

    # Terminate the SMTP session and close the connection
    server.quit()

if __name__ == '__main__': # Checks the main function in (command_parser.c)
    # Checks if attachment file was provided
    if len(sys.argv)>1:
        attachment_path = sys.argv[1]
    else: 
        attachment_path = None
        
    # Send the email to the recipient
    send_email(attachment_path)
    