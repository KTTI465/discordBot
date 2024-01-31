import smtplib
from email.mime.text import MIMEText
from email.header import Header
from env.config import Config

def send_mail(gmail, password, mail, mailText, subject):
    charset = 'iso-2022-jp'
    msg = MIMEText(mailText, 'plain', charset)
    msg['Subject'] = Header(subject.encode(charset), charset)
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(gmail, password)
    smtp_obj.sendmail(gmail, mail, msg.as_string())
    smtp_obj.quit()

config = Config()

def create_mail(mail, subject, mailText):
    send_mail(config.mailaddress, config.mailpassword, mail, mailText, subject)