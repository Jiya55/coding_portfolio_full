from tkinter import *
from tkinter import font

class MyEntry:
    def __init__(self, root):
        self.data = {'Jiya55':'html1419!' }
        self.f = Frame(root, height=500, width=400, bg='White')
        self.f.propagate(0)
        self.f.pack()

        self.b1 = Button(self.f, height=2, width=15, text='Sign up',  command=lambda: self.ButtonClick(1))
        self.b2= Button(self.f, height=2, width=15, text='Log in',  command=lambda: self.ButtonClick(2))
        self.l1 = Label(text='Enter User Name: ', bg='White')
        self.l2 = Label(text='Enter Password: ', bg='White')

        self.e1 = Entry(self.f, width=25, fg ='black', bg='white', font=('Arial', 14))
        self.e2 = Entry(self.f, width=25, fg ='black', bg='white', show='*')


        self.b1.place(x=50, y=50)
        self.b2.place(x=200, y=50)
        self.l1.place(x=50, y=100)
        self.e1.place(x=200, y=100)
        self.l2.place(x=50, y=150)
        self.e2.place(x=200, y=150)
        
    def ButtonClick(self, num):
        str1 = self.e1.get()
        str2 = self.e2.get()
        str3 = ''
        if num == 1:
            if str1 == '':
                str3 = 'Please type your desired username '
                lbl = Label(text=str3, bg='white', fg='red').place(x=50, y =240)
                
            elif str2 == '':
                lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 240)
                str3 = 'please type your desired password ',
                lbl = Label(text= str3, bg='white', fg='red').place(x=50, y =260)
            else:
                for i in self.data.keys():
                    if i == str1:
                        lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 240)
                        lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 260)
                        lbl = Label(text='Please type another username, this username is already registered ', bg='white', fg='red').place(x=50, y= 240)
                        str3 ='userNameTaken'
                        
                    
                if str3 != 'userNameTaken':
                    str3 = 'welcome '
                    self.data[str1] = str2
                    lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 240)
                    lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 260)
                    lbl1 = Label(text=str3 + str1, bg='white').place(x=50, y=240)
        elif num ==2:
            for i in self.data.keys():
                for j in self.data.values():
                    if i == str1:
                        if j ==str2:
                            str3 = 'login done'
                            lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 240)
                            lbl1 = Label(text=str3, bg='white').place(x=50, y=240)
                            lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 260)
                            lbl2 = Label(text='hi '+ str1, bg='white').place(x=50, y=260)
                            lbl3 = Label(text=' ', bg='white', width=200).place(x=50, y=200)
            if str3 != 'login done':
                str3 ='wrong username/password '
                lbl3 = Label(text=str3, bg='white', fg='red').place(x=50, y=200)
                lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 240)
                lbl = Label(text=' ', bg='white', width=200).place(x=50, y= 260)

                    
root = Tk()
mb = MyEntry(root)
root.mainloop()

    
