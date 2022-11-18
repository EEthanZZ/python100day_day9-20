import smtplib

my_email = "zycc2727@gmail.com"
password = "wcbujxxyjdbnmjdl"
#


import datetime as dt
import random
import smtplib

now = dt.datetime.now()
print(now)
year = now.year
month = now.month
weekday = now.weekday()
print(weekday)
print(year)
date_of_birth = dt.datetime(year=1995, month=12, day=8)
print(date_of_birth)

if weekday == 4:
    with open("quotes.txt") as file:
        quote = file.readlines()
        to_send = random.choice(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,
                         password=password)
        # if weekday == 6:
        connection.sendmail(from_addr=my_email, to_addrs="yczhu@yahoo.com",
                            msg=f"Subject:Hello\n\n{to_send}")
