from Final_scripts import mailing_system as email

def get_message():
    f = open('msg.txt', 'r')
    message_body = f.read()
    # print(message)
    f.close()

    return message_body

import csv

if __name__ == "__main__":




    with open('emails.txt') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        readCSV = list(readCSV)

        counter = 0
        for row in readCSV:
            message =None
            message = "Dear " + row[0] + ', \n' + get_message()  # attaching message body with header
            counter += 1

            print("Authenticating !!!", end='')
            x = email.mail("frayhan133057@bscse.uiu.ac.bd", "password here", row[1])
            x.info("Subject HERE !! ", message)

            print("adding attachments !!! ",end='')
            print("CV ", end='')
            x.add_attachment("CV.pdf", "CV.pdf")
            print("Transcript ", end='')
            x.add_attachment("transcript.pdf", "transcript.pdf")
            print("Sending !! ",end='')
            x.send()
            print("Sent to:",row[0])
