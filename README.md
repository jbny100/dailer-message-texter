
# Daily Message Texter

**Daily Message Texter** is a Python program that sends daily text messages from a predefined list of messages to your phone via an email-to-SMS gateway. You can set the time of day for the message to be sent and control the order in which the messages are sent (sequentially or randomly).


## Features

- Sends daily text messages via email-to-SMS gateways.
- Configurable time for daily message delivery.
- Option to send messages in a sequential or random order.
- Logs sent messages and errors to a `logs/message_log.txt` file.

---

## Use Cases

- Motivational Messages: Send yourself daily motivational quotes to kick-start your day.
- Reminders: Use the program to send personal reminders for tasks, goals, affirmations.
- Learning: Use it to send yourself daily facts, vocabulary, or study notes.

## Setup

1. Clone the Repository
To set up the project locally, clone the repository:
```bash
git clone https://github.com/yourusername/daily-message-texter.git
cd daily-message-texter
```

2. Environment Variables
The program requires email login credentials (email and app password) to send messages via an email-to-SMS gateway. These credentials should be stored as environment variables to keep them secure.
    
    For gmail, visit Google's App Password page https://myaccount.google.com/apppasswords and generate an app password.

    For macOS/Linux: Add the following to your ~/.zshrc or ~/.bashrc file:
```bash
export EMAIL_ADDRESS='your_email@gmail.com'
export EMAIL_PASSWORD='your_app_password'
source ~/.zshrc  # Or source ~/.bashrc
```
For Windows: Use the system environment variable settings to add EMAIL_ADDRESS and EMAIL_PASSWORD.

3. Configuration File
The send_time and recipient_email are stored in the config/config.json file for flexibility.

Create/Edit the config/config.json file:
This file contains the time you want to send the message each day and the recipient's email address (typically the email-to-SMS gateway for your phone number).
Example config.json
```json
{
    "send_time": "09:00",
    "recipient_email": "9179748502@txt.att.net"
}
```
send_time: The time at which the message will be sent (in 24-hour format).
recipient_email: The email-to-SMS gateway for your phone number.

Here are some common email-to-SMS gateway formats:

AT&T: [10-digit-phone-number]@txt.att.net
Verizon: [10-digit-phone-number]@vtext.com
T-Mobile: [10-digit-phone-number]@tmomail.net
Sprint: [10-digit-phone-number]@messaging.sprintpcs.com

4. Message List
The program reads messages from a text file located in config/message_list.txt

Create/Edit the config/message_list.txt file. Add one message per line, for example:
```
Stay positive and keep pushing forward.
Every day is a new opportunity for success.
Believe in yourself and your abilities.
```

### Logs

The program logs each sent message with a timestamp and records errors in logs/message_log.txt. If the logs/ directory doesn't exist, it will be created automatically.


## How to Run 

The program must be run from the terminal (macOS/Linux) or Command Prompt/PowerShell (Windows) to ensure it can access the environment variables and configuration files correctly.

1. Running on macOS/Linux

Open the terminal and navigate to the project directory:
```bash
cd /path/to/daily-message-texter
```
Run the program:
```bash
python3 daily_message_texter.py
```

2. Running on Windows

Open Command Prompt or PowerShell.

Navigate to the project directory:
```cmd
cd C:\path\to\daily-message-texter
```
Run the program:
```cmd
python daily_message_texter.py
```
The program will now run continuously, sending a message at the configured time every day.


### Troubleshooting

Environment Variable Errors - If the program raises a ValueError about missing credentials, ensure that your EMAIL_ADDRESS and EMAIL_PASSWORD environment variables are set correctly.

No messages Sent - Ensure that the message_list.txt file in the config/ directory contains at least one message. Verify the format of the recipient's email-to-SMS gateway address.

Message Delivery Issues - Check the carrier's email-to-SMS gateway format. Ensure that your Gmail account (if using gmail) has an active app password and that Gmail allows access from less secure apps.


### Future Improvements

- Add support for multiple phone numbers
- Schedule different messages for different times of the day.





