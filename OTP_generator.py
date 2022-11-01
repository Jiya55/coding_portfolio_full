#CUI
#'''
#Imports
import smtplib
import ssl
from email.message import EmailMessage
from random import randint
def otp_generator(number):
    digits=int(number)
    otp=''
    for i in range(digits):
        otp+=str(randint(0, 9))
    return otp
def send_otp(gmail, otp):
    email_creator = EmailMessage()
    email_creator['From'] = 'jiyakirori@gmail.com'
    email_creator['To'] = gmail
    email_creator['Subject'] = 'your otp is '+otp
    email_creator.set_content('Hello, \n your otp is '+otp)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login('jiyakirori@gmail.com', 'wfsjwlldzerhlgtm')
        smtp.sendmail('jiyakirori@gmail.com', gmail, email_creator.as_string())
    print('otp sent')
def check_otp(org_otp, user_otp):
    if org_otp==user_otp:
        print('you have access to your account now')
        return True
    else:
        print('Wrong OTP')
        return False

print('hello')
inp = input('Please type a yes if you want an otp ')
condition=''
if inp.lower() == 'yes':
    otp=otp_generator(4)
    email= input('Please type your gmail id: ')
    send_otp(email, otp)
    user_otp=input('please type the otp you recived: ')
    check_otp(otp, user_otp)
#'''     
'''   
#GUI 
from tkinter import *
import smtplib
import ssl
from email.message import EmailMessage
from random import randint
global otp
otp_g=''
def otp_generator(number):
    digits=int(number)
    otp=''
    for i in range(digits):
        otp+=str(randint(0, 9))
    return otp
def button_click(n):
    if n==1:
       otp_generator(4)

root = Tk()

f = Frame(root, height= 500, width=600, bg='white')
f.propagate(0)
f.pack()
otp_generator_btn = Button(f, height=2, width=15, text='Generate OTP', command=lambda:otp_generator(4))
otp_generator_btn.place(x=50, y=50)

root.mainloop()
'''







