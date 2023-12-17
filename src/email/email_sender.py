'''
Main Code Description: This piece of software is simply a python script 
that sends emails to a desired recipient with the option of including an
attachment via the Command line/terminal. 

Copyright: (C) Sergius Nyah 2023-12-17
License: MIT License
 '''

# Import the settings from the settings.py file
# Contains the configuration settings for the email sender. 
import settings

# Use the settings in your email sending code
server = settings.EMAIL_HOST
port = settings.EMAIL_PORT
username = settings.EMAIL_USERNAME
password = settings.EMAIL_PASSWORD
sender = settings.DEFAULT_SENDER
recipient = settings.DEFAULT_RECIPIENT
subject = settings.EMAIL_SUBJECT 

# Import the email modules we'll need 