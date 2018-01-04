from Final_scripts import mailing_system as email

def get_message():
    f = open('/home/farshid/Desktop/msg.txt', 'r')
    message_body = f.read()
    # print(message)
    f.close()

    return message_body

import csv

if __name__ == "__main__":




    with open('/home/farshid/Desktop/emails.txt') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        readCSV = list(readCSV)

        counter = 0
        for row in readCSV:
            message =None
            message = "Dear " + row[0] + ', \n' + get_message()  # attaching message body with header
            counter += 1

            print("Authenticating !!!", end='')
            x = email.mail("frayhan133057@bscse.uiu.ac.bd", "password here", row[1])
            x.info("PhD interest", message)

            print("adding attachments !!! ",end='')
            print("Certificate ",end='')
            x.add_attachment("Certificate.pdf", "/home/farshid/Desktop/Certificate.pdf")
            print("CV ", end='')
            x.add_attachment("CV.pdf", "/home/farshid/Desktop/main_CV.pdf")
            print("Transcript ", end='')
            x.add_attachment("transcript.pdf", "/home/farshid/Desktop/transcript final.pdf")
            print("Sending !! ",end='')
            x.send()
            print("Sent to:",row[0])
