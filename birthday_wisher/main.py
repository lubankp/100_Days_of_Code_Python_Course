##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
from smtplib import *
import datetime as dt
from random import *

my_email = "pawel.lubanski.91@gmail.com"
password = "wdaiocsapajywwnn"
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


def send_mail(text, adress):
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=adress,
            msg=f"Subject:Birthday wishes\n\n {text}"
        )


def get_random_letter(name):
    letter = choice(letters)
    with open(f"./letter_templates/{letter}", "r") as file:
        all_lines = file.readlines()
        text = ""
        for line in all_lines:
            text += line
            line.strip()
            if "[NAME]" in text:
                text = text.replace("[NAME]", name)
    print(text)
    return text


data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
now = dt.datetime.now()

for person in data_dict:
    if now.day == person["day"] and now.month == person["month"]:
        ready_letter = get_random_letter(person["name"])
        send_mail(ready_letter, person["email"])


