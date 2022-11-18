# import smtplib
#
# my_email = "zycc2727@gmail.com"
# password = "wcbujxxyjdbnmjdl"
#
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,
#                      password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="yczhu@yahoo.com",
#                         msg="Subject:Hello\n\nThis is body of my email.")

import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
month = now.month
weekday = now.weekday()
print(year)
