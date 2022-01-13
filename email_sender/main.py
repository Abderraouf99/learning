import smtplib ## library to send emails using Python !
from private_data import email, password, recipient_email ## importing my private email data

## creating an smtp instance compatible with gmail
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    message = "Hello \n \n World !"
    connection.starttls() # secure message encryption
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=recipient_email, msg=message)
