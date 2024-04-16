Birthday Wisher with SMTPlib

This Python script helps you send birthday emails to individuals based on the data stored in a CSV file. It checks the current date against the birthdays listed in the file, and if there's a match, it sends a personalized email to the birthday person.
Prerequisites

Python 3 installed on your system.
Access to an email account for sending birthday emails.
Familiarity with editing Python scripts and CSV files.

Setup

Download or clone the repository containing the script.
Install the required dependencies, including pandas.
Update the script with your email address and password.
Customize the birthdays.csv file with the birthdays and email addresses of the individuals you want to send emails to.
Optionally, create letter templates in the letter_templates folder. Use the placeholder [NAME] to personalize each email.

Usage

Run the script using Python:

bash

python main.py

The script will check for birthdays matching the current date and send personalized emails to the recipients.

Hosting on PythonAnywhere

You can host this script on PythonAnywhere to run it in the cloud. Follow these steps:

Sign up for a PythonAnywhere account.
Upload your script file and CSV file to your PythonAnywhere account.
Set up a scheduled task to run the script daily using PythonAnywhere's task scheduler.
Ensure that your PythonAnywhere account has internet access to send emails via SMTP.

Important Notes

Ensure that you have enabled access to less secure apps in your email account settings (for Gmail accounts) or use an app password if two-factor authentication is enabled.
Test the script with your own email address first to verify that it's working correctly before sending emails to others.
Make sure to review and comply with email sending policies and regulations, especially if sending emails in bulk.
Regularly update the birthdays.csv file with new birthdays or changes to existing ones.
Use responsibly and respect the privacy of the recipients.
