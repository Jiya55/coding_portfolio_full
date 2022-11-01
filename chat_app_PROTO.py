from tkinter import *
'''x = 10
global y
y= 10


def Chat(user):
    if user==1:
        if e.get() != '':
            y = globals()['y']
            lbl = Label(root, text='user 1: '+ e.get(), bg='white')
            lbl.place(x=x, y=y)
            lbl = Label(root1, text='user 1: '+ e.get(), bg='white')
            lbl.place(x=x, y=y)
            globals()['y'] += 20
            y = globals()['y']
            e.delete(0, END)
    elif user==2:
         if e1.get() != '':
            y = globals()['y']
            lbl = Label(root1, text='user 2: '+ e1.get(), bg='white')
            lbl.place(x=x, y=y)
            lbl = Label(root, text='user 2: '+ e1.get(), bg='white')
            lbl.place(x=x, y=y)
            globals()['y'] += 20
            y = globals()['y']
            e1.delete(0, END)

root= Tk()
root.title('user1')
f = Frame(root,height=400, width=300, bg='white')
f.propagate(0)
f.pack()

e = Entry(f, width=30, bg='white')
e.place(x=10, y=350)
send_btn= Button(f, text='Send', width=5, height=1, command=lambda:Chat(1))
send_btn.place(x=200, y=350)


root1= Tk()
root1.title('user2')
f1 = Frame(root1,height=400, width=300, bg='white')
f1.propagate(0)
f1.pack()
e1 = Entry(f1, width=30, bg='white')
e1.place(x=10, y=350)
send_btn1= Button(f1, text='Send', width=5, height=1, command=lambda:Chat(2))
send_btn1.place(x=200, y=350)

root.mainloop()

root1.mainloop()
'''
'''def createNewWindow():
    newWindow = Toplevel(app)

app = Tk()
buttonExample = Button(app,
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()
'''
# Global Variables
global chat_y, btn_x, btn_y
chat_x = 10
chat_y= 10
btn_x=10
btn_y=10
btn_h =10
btn_w= 2
backGround = 'white'
msg_space = 20
user_list=['user1', 'jiya', 'user2']
def Chat(Rroot, Sroot, e, name):
    y = globals()['chat_y']
    x=chat_x
    if e.get() != '':
        lbl = Label(Rroot, text=name+ ' : '+ e.get(), bg=backGround)
        lbl.place(x=x, y=y)
        lbl = Label(Sroot, text=name+ ' : '+ e.get(), bg=backGround)
        lbl.place(x=x, y=y)
        globals()['chat_y'] += msg_space
        e.delete(0, END)
           
def create_user(name):
    Rroot = Tk()
    Rroot.title(name)
    Rf = Frame(Rroot, height=400, width=300, bg=backGround)
    Rf.propagate(0)
    Rf.pack()
    Rmsg = Entry(Rf, width=30, bg=backGround)
    Rmsg.place(x=10, y=350)
   
    Sroot= Tk()
    Sroot.title('Me')
    Sf = Frame(Sroot,height=400, width=300, bg=backGround)
    Sf.propagate(0)
    Sf.pack()
    Smsg = Entry(Sf, width=30, bg=backGround)
    Smsg.place(x=10, y=350)

    send_btn1= Button(Sf, text='Send', width=5, height=1, command=lambda:Chat(Rroot, Sroot, Smsg, 'Me'))
    send_btn1.place(x=200, y=350)
    send_btn= Button(Rf, text='Send', width=5, height=1, command=lambda:Chat(Rroot, Sroot, Rmsg, name))
    send_btn.place(x=200, y=350)
    Rroot.mainloop()
    Sroot.mainloop()
   
def addUser(name, pos_y, root):
    button = Button(root, text=name.get(), width=10, height=2, command=lambda: create_user(name.get()))
    button.place(x=10, y=pos_y)
    globals()['btn_y']+= 50
    user_list.append(name.get())
    print(user_list)
    
   
def make_user():
    globals()['btn_y']+= 50
    add_root = Tk()
    add_root.title()
    fr = Frame(add_root, height=400, width=300, bg='white')
    fr.propagate(0)
    fr.pack()
    name= Entry(fr, width=30, bg='white')
    name.place(x=60, y=10)
    name_lbl= Label(fr,text='Name: ', bg='white')
    name_lbl.place(x=10,y=10)
    submit_btn = Button(fr, text='Submit', width=5, height=1, command=lambda:addUser(name, btn_y, ms_frame))
    submit_btn.place(x=200, y=350)
def group():
    grp_root= Tk()
    grpf= Frame(grp_root, height=400, width=300, bg='white')
    grpf.propagate(0)
    grpf.pack()
    label =  Label(grpf,text='Group members', bg='white')
    label.place(x=10,y=10)
    variable= 'hi'
    c1 = Checkbutton(grpf, text='hi', variable=variable, command=lambda:print(variable))
    variable1='hello'
    c2 = Checkbutton(grpf, text='hello', variable=variable1, command=lambda:print(variable1))
    c1.place(x=20, y=50)
    c2.place(x=20, y=70)
group()
Main_screen = Tk()
Main_screen.title('menu')
ms_frame = Frame(Main_screen,height=400, width=300, bg='white')
ms_frame.propagate(0)
ms_frame.pack()
add_user_btn = Button(ms_frame, text='add user',width=10, height=2, command=lambda: make_user())
add_user_btn.place(x=10, y=btn_y)
btn_y+=50
user_1btn = Button(ms_frame, text='user 1', width=10, height=2, command=lambda: create_user('user1'))
user_1btn.place(x=10, y=btn_y)

