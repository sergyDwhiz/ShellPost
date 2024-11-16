# Unit tests for "email_sender.py" script

import unittest
from unittest.mock import patch, MagicMock, ANY
from email_sender import email_sender

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

        # Act
        email_sender.send_email(attachment_path)

        # Assert
        mock_smtp.assert_called_once_with(email_sender.server, email_sender.port)
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with('test_username', 'test_password')
        mock_server.sendmail.assert_called_once_with(email_sender.sender, email_sender.recipient, ANY)
        mock_server.quit.assert_called_once()

if __name__ == '__main__': # Run tests if file directly executed
    unittest.main()