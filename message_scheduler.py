# message_scheduler.py

import smtplib
import os
import schedule
import time
from datetime import datetime
from email.mime.text import MIMEText
from config.email_config import email_address, email_password, smtp_server, smtp_port

class MessageScheduler:
    def __init__(self, messages, send_time, recipient_email, random_order=False):
        self.messages = messages
        self.send_time = send_time
        self.recipient_email = recipient_email
        self.random_order = random_order
        self.sent_messages = []

    def text_myself(self, message, retries=3):
        """Sends a text message via email-to-SMS gateway, with retries."""
        for attempt in range(retries):
            try:
                # Add a newline before the message to create a blank line after the FRM part
                clean_message = "\n" + message 
                msg = MIMEText(clean_message)
                msg['From'] = email_address
                msg['To'] = self.recipient_email
                # msg['Subject'] = "Daily Message"

                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(email_address, email_password)
                    server.sendmail(email_address, self.recipient_email, msg.as_string())

                print(f"Message sent: {message}")

                # Ensure logs/ directory exists
                if not os.path.exists('logs'):
                    os.makedirs('logs')
                    
                # Log the message with timestamp
                with open('logs/message_log.txt', 'a') as log_file:
                    log_file.write(f"{datetime.now()}: {message}\n")
                break  # Exit the retry loop if the message is successfully send

            except Exception as e:
                print(f"Failed to send message: (Attempt {attempt + 1}/{retries}): {e}")
                time.sleep(5)  # Wait 5 seconds before retrying
        else:
            # If we exit the loop without breaking, it mean all retries failed
            print(f"Failed to send message after {retries} attempts.")
            # Log failure after retries
            with open('message_log.txt', 'a') as log_file:
                log_file.write(f"{datetime.now()}: Failed to send message after {retries} attempts.\n")

    def schedule_messages(self):
        """Schedules the daily message sending."""
        if self.random_order:
            random.shuffle(self.messages)

        schedule.every().day.at(self.send_time).do(self.send_message)
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("Scheduler interrupted. Exiting program.")

    def send_message(self):
        """Sends a message from the list and keeps track of sent messages."""
        if not self.messages:
            print("No messages to send.")
            return

        if not self.sent_messages or len(self.sent_messages) >= len(self.messages):
            self.sent_messages = []

        # Determine the next message to send
        for message in self.messages:
            if message not in self.sent_messages:
                self.text_myself(message)
                self.sent_messages.append(message)
                break

    @staticmethod
    def validate_time_format(send_time):
        """Validates the time format to be HH:MM."""
        try:
            datetime.strptime(send_time, '%H:%M')
            return True
        except ValueError:
            return False

