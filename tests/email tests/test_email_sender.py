# Unit tests for "email_sender.py" script

import unittest
from unittest.mock import patch, MagicMock
from src.email.email_sender import email_sender

class TestEmailSender(unittest.TestCase):
    @patch('src.email.email_sender.smtplib.SMTP')
    @patch('src.email.email_sender.getpass.getpass')
    @patch('builtins.input')
    def test_send_email(self, mock_input, mock_getpass, mock_smtp):
        # Arrange
        mock_input.return_value = 'test_username'
        mock_getpass.return_value = 'test_password'
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        attachment_path = 'attachment_path'

        