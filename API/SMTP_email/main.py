import smtplib

my_email = "zycc2727@gmail.com"
password = "wcbujxxyjdbnmjdl"

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=my_email,
                 password=password)
connection.sendmail(from_addr=my_email,to_addrs="yczhu@yahoo.com",
                    msg="Hello")
connection.close()