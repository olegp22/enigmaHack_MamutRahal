import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = ""
    password = ""

    server = smtplib.SMTP('smtp.gamil.com')  #
    server.starttls()

    try:
        server.login(sender, password)
        answer = MIMEText(message)
        server.sendmail(sender, sender, answer.as_string())  # оправитель, кому, что
        return "ok"
    except Exception as e:
        return e
