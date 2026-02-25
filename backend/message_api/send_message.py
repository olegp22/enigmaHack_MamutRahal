import smtplib
from email.mime.text import MIMEText


def send_email(to_email: str, message: str):
    sender = ""
    password = ""

    try:
        server = smtplib.SMTP('smtp.yandex.ru', 587)
        server.starttls()
        server.login(sender, password)
        answer = MIMEText(message)
        answer["Subject"] = 'Ответ от системы'
        answer['From'] = sender
        answer['To'] = to_email
        server.sendmail(sender, sender, answer.as_string())  # оправитель, кому, что
        server.quit()
        return "ok"
    except Exception as e:
        return e

