import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Initial_go import infos

fromaddr = infos.mymail_2
toaddr = infos.mymail_1
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing Mails"

body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, infos.mymail_2_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()