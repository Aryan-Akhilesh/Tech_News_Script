import smtplib, ssl
import os


def send_email(message):

    host = "smtp.gmail.com"
    port = 465

    user_name = "website.portfolio.ary@gmail.com"
    password = "vzyizwtjhzqoavpp"

    receiver = "aryanakhil99@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message.encode("utf8"))

