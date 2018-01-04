import smtplib
from Initial_go import infos


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = infos.mymail_2
toaddr = infos.mymail_1

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"

body = "TEXT YOU WANT TO SEND"

msg.attach(MIMEText(body, 'plain'))

filename = "pic.png"
attachment = open("/home/farshid/Desktop/passport.png", "rb")




part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename) #1st attachment 
msg.attach(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename) #2nd attachment 

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, infos.mymail_2_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
