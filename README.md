# Python for Sending mails via Gmail 
Using the codes in "Final scripts" folder one can send bcc mails to multiple authors. 
The interesting part is that rather than sending a general msg, one can put a name of the reciever in the mail to make it more personal 
dispite of it being a BCC mail. The most fun fact is that it wont show the receivers that it was a BCC mail. 

The folder "intial go" contains the simpler seperate scripts for sending mail via gmail using python.

The codes in Regex folder helps to convert a list of mails writen like,

jon.smith@abc.edu  

jane.doe@asd.ce.aus

to 

Smith,jon.smith@abc.edu  

Doe,jane.doe@asd.ce.aus

which is a required format to run the mail.py file from Final_scripts  





Now the sent mail will look like this 

to: jon.smith@abc.edu  

SUB: Subject here!!!

Dear Smith,
This is the message 

to: jane.doe@asd.ce.aus

SUB: Subject here!!!

Dear Doe,
This is the message 
