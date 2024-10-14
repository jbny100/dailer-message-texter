# email_config.py

import os

# Fetch the email credentials and SMTP settings from environment variables

email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Check if credentials are set
if not email_address or not email_password:
	raise ValueError("Email credentials (EMAIL_ADDRESS or EMAIL_PASSWORD) are not set in the environment variables.")
	