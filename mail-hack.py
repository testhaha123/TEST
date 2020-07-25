import getpass
import os
import sys
import smtplib

os.system('clear')
os.system('figlet Email hack')
email=input('Email:')
email_to=input('Email send to:')
password=getpass.getpass('Password')
message=input('Message:')
number=input('Number you want to send:')
server=smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(email, password)
n=1
for i in range(0, int(number)):
    server.sendmail(email, email_to, message)
    print('email send ' + str(n))
    n+=1
server.quit()
