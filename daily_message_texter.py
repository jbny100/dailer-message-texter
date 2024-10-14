# daily_message_texter.py

import json
from message_scheduler import MessageScheduler
from config.email_config import email_address, email_password, smtp_server, smtp_port

# Ensure the environment variables are set
if not email_address or not email_password:
    print("Error: Missing email credentials. Please set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")

def run_message_scheduler(): 
    # Load the configuration from config.json
    try:
        with open('config/config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print("Error: 'config.json' file not found in the 'config/' directory.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to parse 'config.json'. Ensure the file is in valid JSON format.")
        return

    # Extract send_time and recipient_email from the config
    send_time = config.get("send_time")
    recipient_email = config.get("recipient_email")

    # Validate the configuration
    if not send_time or not recipient_email:
        print("Error: 'send_time' or 'recipient_email' is missing in 'config.json'.")
        return

    # Load messages from the text file
    try:
        with open('config/message_list.txt', 'r') as file:
            message_list = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("Error: 'message_list.txt' file not found. Please make sure the file is in the correct directory.")
        return

    # Check if the message list is empty
    if not message_list:
        print("Error: 'message_list.txt' is empty. Please add messages to the file.")
        return

    # Create a MessageScheduler instance
    message_scheduler = MessageScheduler(
        messages=message_list,
        send_time=send_time,
        recipient_email=recipient_email,
        random_order=False  # Set to True for random order, False for sequential order
    )

    # Validate time format
    if message_scheduler.validate_time_format(send_time):
        # Start the message scheduling process
        print(f"Starting the message scheduler at {send_time} for {recipient_email}.")
        message_scheduler.schedule_messages()
    else:
        print("Invalid time format. Please use HH:MM format.")

# To run the function:
if __name__ == "__main__":
    run_message_scheduler()

