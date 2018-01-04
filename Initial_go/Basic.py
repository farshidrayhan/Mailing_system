import smtplib
from Initial_go import infos

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(infos.mymail_2, infos.mymail_2_pass)

msg = "YOUR MESSAGE ffs!"
server.sendmail(infos.mymail_2,infos.mymail_1, msg)
server.quit()

