import datetime as dt
import smtplib
import pandas
from random import *

PLACEHOLDER = "[NAME]"


def smtp(file, receivers_email):
    my_email = "SENDERS EMAIL..."
    my_password = "EMAIL PASSWORD APP"
    #select SMTP (Simple Mail Transfer Protocol) server address for respective senders provider
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=f"{receivers_email}",
                        msg=f"Subject: Happy Birthday!\n\n{file}")


now = dt.datetime.now()

current_day = now.day
current_month = now.month

birth_days = pandas.read_csv("birthdays.csv")
birthday_dict = birth_days.to_dict(orient="records")

birthdays_len = len(birthday_dict)
for i in range(birthdays_len):
    birthday_day = birthday_dict[i]["day"]
    birthday_month = birthday_dict[i]["month"]
    birthday_person = birthday_dict[i]["name"]
    birthday_email = birthday_dict[i]["email"]

if current_day == birthday_day and current_month == birthday_month:
    random_choice = randint(1, 3)
    with open(f"./letter_templates/letter_{random_choice}.txt", mode="r") as data:
        letter_content = data.read()
        new_letter = letter_content.replace(PLACEHOLDER, birthday_person)
        smtp(new_letter, birthday_email)
