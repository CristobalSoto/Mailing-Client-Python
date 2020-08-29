import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from variables import *

# if you are using gmail you have to activate unsecure apps in your account

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_mail, mail_password)

msg = MIMEMultipart()
msg['From'] = 'YourName'
msg['To'] = to_mail
msg['Subject'] = 'This is a test email'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail(from_mail, to_mail, text)