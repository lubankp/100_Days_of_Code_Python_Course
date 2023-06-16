from smtplib import *
import datetime as dt
from random import *

my_email = "pawel.lubanski.91@gmail.com"
password = "wdaiocsapajywwnn"


def send_mail(text):
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="lubpaw91@gmail.com",
            msg=f"Subject:Motivation text\n\n {text}"
        )


def get_random_text():
    with open("./quotes.txt", "r") as file:
        all_lines = file.readlines()
    return choice(all_lines)


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    text = get_random_text()
    send_mail(text)