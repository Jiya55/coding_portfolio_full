#'''
from cgitb import text
from re import X
import smtplib
import ssl
from email.message import EmailMessage
import datetime as dt 
from datetime import *
import time
#'''
'''
my email_password= 'wfsjwlldzerhlgtm'
mom email_password = 'ljfbkbmccxjnzcfw'
'''
#'''
#read excel file of clients and send to emails listed
mass_email_list=['jiyakirori@gmail.com', 'daranjan97@gmail.com', 'bobchrisbasket@gmail.com']
def email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, sending_time = None):
    print(email_sender,email_sender_password, email_receiver, subject, body, sending_time)
    email_creator = EmailMessage()
    email_creator['From'] = email_sender
    email_creator['To'] = email_receiver
    email_creator['Subject'] = subject
    email_creator.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_sender_password)
        if sending_time != None:
            send_time = datetime.strptime(sending_time,  '%b %d %Y %I:%M%p') # set your sending time in UTC
            time.sleep(send_time.timestamp() - time.time())
            smtp.sendmail(email_sender, email_receiver, email_creator.as_string())
            print('email sent')
            return 
        smtp.sendmail(email_sender, email_receiver, email_creator.as_string())
        print('email sent')
'''for i in mass_email_list:
    email_sender_bot('jiyakirori@gmail.com','wfsjwlldzerhlgtm', i, 'Mass email test', 'Hello')'''
def main():
    print('Hello, Welcome to auto mail')
    time.sleep(1)
    print('Please answer the following questions to send an auto mail:')
    time.sleep(1)
    email_sender=input('sender: ')
    print('Jiya:wfsjwlldzerhlgtm; Sonia:ljfbkbmccxjnzcfw')
    email_sender_password=input('app password: ')
    email_receiver = input('Reciver gmail: ')
    subject= input('subject: ') 
    body= input('body: ')
    specific_time= input('any specific date/time to send the email?(yes or no) ')
    if specific_time.lower()=='yes':
        set_time = input('date/time(format=Jun 24 2022 5:36PM): ')
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, set_time)
    else:
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body)
#main()
def set_time_send_email(e1,e2,e3,e4,e5,e7):
    time =e7.get()
    email_sender_bot(e1,e2,e3,e4,e5,time)
def entry_to_bot(e1,e2,e3,e4,e5,e6):
    es= e1.get()
    esp= e2.get()
    er= e3.get()
    s= e4.get()
    bo= e5.get()
    ti= e6.get()
    if ti.lower()=='no':
        email_sender_bot(es, esp, er, s, bo)
        return
    l7 = Label(text='date/time(format=Jun 24 2022 5:36PM): ', font=15, bg='white')
    e7 = Entry(f)
    b=Button(f, text='set time and send email', width=20 , height=2, command=lambda:set_time_send_email(es, esp, er, s, bo,e7))
    e7.place(x= 850, y=100)
    l7.place(x=470, y= 100)
    b.place(x=470, y=200)
#GUI 
from tkinter import Frame, Tk, Button, Text, Entry, Label 
root = Tk()
f= Frame(root, height=500, width=1000, bg='white')
f.propagate(0)
t= Label(text='Email Sender Bot', font=15, bg='white')
l1 = Label(text='sender: ', font=15, bg='white')
e1 = Entry(f)
l2 = Label(text='app password: ',font=15, bg='white')
e2 = Entry(f)
l3 = Label(text='Email Receiver: ', font=15, bg='white')
e3 = Entry(f)
l4 = Label(text='Subject: ', font=15, bg='white')
e4 = Entry(f)
l5 = Label(text='body: ' , font=15, bg='white')
e5 = Entry(f)
l6 = Label(text='date/time to send(yes/no)', font=15, bg='white')
e6 = Entry(f)

b=Button(f, text='send email', width=20 , height=2, command=lambda:entry_to_bot(e1,e2,e3,e4,e5,e6))
t.place(x=500,y=10)
l1.place(x=100, y= 100)
e1.place(x= 350, y=100)
l2.place(x=100, y= 150)
e2.place(x= 350, y=150)
l3.place(x=100, y= 200)
e3.place(x= 350, y=200)
l4.place(x=100, y= 250)
e4.place(x= 350, y=250)
l5.place(x=100, y= 300)
e5.place(x= 350, y=300)
l6.place(x=100, y= 350)
e6.place(x= 350, y=350)
b.place(x= 100, y=400)
f.pack()
root.mainloop

#'''
'''
scedule mail,
list of ids

import smtplib
import ssl
from email.message import EmailMessage
import datetime as dt 
from datetime import *
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

msg = MIMEMultipart()
msg.attach(MIMEText(file("h.jpg").read()))
msg.attach(MIMEImage(file("CHEAT SHEET.docx").read()))

'''
'''
my email_password= 'wfsjwlldzerhlgtm'
mom email_password = 'ljfbkbmccxjnzcfw'
'''
'''
def email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, sending_time = None):
    
    email_creator = EmailMessage()
    email_creator['From'] = email_sender
    email_creator['To'] = email_receiver
    email_creator['Subject'] = subject
    email_creator.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_sender_password)
        if sending_time != None:
            send_time = datetime.strptime(sending_time,  '%b %d %Y %I:%M%p') # set your sending time in UTC
            time.sleep(send_time.timestamp() - time.time())
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            print('email sent')
        else:
            smtp.sendmail(email_sender, email_receiver, email_creator.as_string())
            print('email sent')
def main():
    print('Hello, Welcome to auto mail')
    time.sleep(1)
    print('Please answer the following questions to send an auto mail:')
    time.sleep(1)
    email_sender=input('sender: ')
    print('Jiya:wfsjwlldzerhlgtm; Sonia:ljfbkbmccxjnzcfw')
    email_sender_password=input('app password: ')
    email_receiver = input('Reciver gmail: ')
    subject= input('subject: ') 
    body= input('body: ')
    specific_time= input('any specific date/time to send the email?(yes or no) ')
    if specific_time.lower()=='yes':
        set_time = input('date/time(format=Jun 24 2022 5:36PM): ')
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body, set_time)
    else:
        email_sender_bot(email_sender, email_sender_password, email_receiver, subject, body)
main()
'''
