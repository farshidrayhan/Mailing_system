import csv
import re


path = 'sample_mails.txt'   # mail ids containing last name of the recipient

with open(path, 'r') as f:
    msg = f.readlines()

msg = [x.strip() for x in msg]
with open('test.txt','w') as x: # the output file
    writer = csv.writer(x)

    for message in msg:
        m = re.search('\.(\w+)\@', message)
        try:
            last_name = m.group(0).strip('\.').strip('\@').title()

            print(last_name ,end='  ')

            writer.writerow([last_name,message])
        except:
            None

    f.close()
