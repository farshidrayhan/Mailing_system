import smtplib
from Initial_go import infos

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class mail:

    fromaddr = None
    toaddr = None
    password = None
    msg = None

    def __init__(self,my_address,my_password,send_to):

        mail.fromaddr = my_address
        mail.toaddr = send_to
        mail.password = my_password

        mail.msg = MIMEMultipart()
        mail.msg['From'] = mail.fromaddr
        mail.msg['To'] = mail.toaddr
        # mail.msg['bcc'] = mail.toaddr
        # mail.msg['cc'] = mail.toaddr


    def info(self,subject,message):

        mail.msg['Subject'] = subject

        body = message

        mail.msg.attach(MIMEText(body, 'plain'))

    def add_attachment(self,filename_with_extention,path):

        filename = filename_with_extention
        attachment = open(path, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        mail.msg.attach(part)
        # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        #
        # mail.msg.attach(part)

        # print(subject)
        # print(message)
        # print(mail.fromaddr)
        # print(mail.toaddr)
        # print(mail.password)

    def send(self):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(mail.fromaddr, password=mail.password)
        text = mail.msg.as_string()
        server.sendmail(mail.fromaddr, mail.toaddr, text)
        server.quit()


