# from smtplib import *
#
# my_email = "pawel.lubanski.91@gmail.com"
# password = "wdaiocsapajywwnn"
#
# with SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="lubpaw91@gmail.com",
#         msg="Subject:Hello\n\n This is a body "
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1991, month=7, day=2, hour=23)
print(date_of_birth)