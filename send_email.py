import smtplib
import ssl
import os


def Send_email(message, user_email):
    host = "smtp.gmail.com"
    port = 465
    receiver = "santosh.chezhyan@gmail.com"
    username = "santosh.chezhyan@gmail.com"
    password = "ubdjwcglzdhvindq"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

