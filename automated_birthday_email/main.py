import smtplib
from private_infos import email, password, recipient_email
import datetime as dt_module

my_email = email
my_password = password

now = dt_module.datetime.now()
date_of_birth = dt_module.datetime(year=1999, month=1, day=15)
if now.day == date_of_birth.day and now.month == date_of_birth.month:
    with open("./letter_template.txt") as email_template:
        message_array = email_template.readlines()
        message = ""
        for text in message_array:
            message += text
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=message)
