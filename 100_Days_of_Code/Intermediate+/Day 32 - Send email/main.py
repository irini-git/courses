import smtplib
import os

# -------------- Constants --------------
my_email = os.environ.get('MY_EMAIL')
my_password = os.environ.get('MY_PASSWORD')

# Create connection
connection = smtplib.SMTP("smtp.gmail.com")

# Secure the connection
connection.starttls()

# Login
connection.login(user=my_email, password=my_password)

# Send mail
# Google has removed the possibility to send mails from Python...
connection.sendmail(
    from_addr=my_email,
    to_addrs=my_email,
    msg="Hello"
)

