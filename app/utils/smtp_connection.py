# smtp_client.py
from builtins import Exception, int, str
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings.config import settings
import logging

class SMTPClient:
    def __init__(self, server: str, port: int, username: str, password: str):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, subject: str, html_content: str, recipient: str):
        try:
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.username
            message['To'] = recipient
            message.attach(MIMEText(html_content, 'html'))

            with smtplib.SMTP(self.server, self.port) as server:
                server.ehlo()
                server.starttls()  # Use TLS     
                server.ehlo()
                print(f'Usernme, PW, server, port: {self.username}, {self.password}, {self.server}, {self.port}') 
                server.login(self.username, self.password)
                server.ehlo()
                server.sendmail(self.username, recipient, message.as_string())
                server.close()
            logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")
            raise
