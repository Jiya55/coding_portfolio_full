from tkinter import *
from time import *
root = Tk()
c = Canvas()
id = c.create_oval((50, 50),(200,200),state='normal', width='4', fill ='orange', outline='brown')
id1 = c.create_oval((60,60),(190,190), state='hidden', width='1', fill ='red', outline='red')
id2 = c.create_oval((70,70),(180,180), state='hidden', width='1', fill ='yellow', outline='yellow')
id3 =  c.create_oval((85,85),(100,100), state='hidden', width='1', fill ='red', outline='red')
id4 = c.create_arc((110,70),(130, 90),state='hidden', width='5', outline='green', style='arc',start =90, extent= 180)
id5 = c.create_rectangle((140,80),(150,90),state='hidden', width='1', fill='navajowhite2', outline='navajowhite3')
id6 = c.create_oval((75,105),(85,115),state='hidden',  width='4', outline='black')
id7 =  c.create_oval((110,105),(120,115), state='hidden', width='1', fill ='yellow2', outline='gold3')
id8 = c.create_oval((140,105),(150,115),state='hidden', width='4', outline='green')
c.pack()


Pizza_order=[]
f = Frame(root, height =200 , width=400, bg ='white')
f.propagate(0)
total=0
def btn_click(num):
    global total
    if num==0:
        c.itemconfig(id1, state='normal')
        Pizza_order.append('pizza sauce')
        total+=1
        
    if num==1:
        c.itemconfig(id2, state='normal')
        Pizza_order.append('cheese')
        total+=1
    if num==2:
        c.itemconfig(id3, state='normal')
        Pizza_order.append('tomato')
        total+=2
    if num==3:
         c.itemconfig(id4, state='normal')
         Pizza_order.append('capsicum')
         total+=2
    if num==4:
         c.itemconfig(id5, state='normal')
         Pizza_order.append('mushroom')
         total+=2
    if num==5:
         c.itemconfig(id6, state='normal')
         Pizza_order.append('olive')
         total+=2
    if num==6:
         c.itemconfig(id7, state='normal')
         Pizza_order.append('sweet corn')
         total+=2
    if num==7:
         c.itemconfig(id8, state='normal')
         Pizza_order.append('jalpeno')
         total+=2
    if num==8:
        print(Pizza_order)
        print('cost= '+str(int(total))+' euros')
        lbl1 = Label(f, text='Order placed', background='white')
        lbl1.place(x=255, y=140)
        lbl1 = Label(f, text='cost= '+str(int(total))+' euros', background='white')
        lbl1.place(x=255, y=155)
        print(e.get())
        global Timer
        Timer = int(input('How much total time will it take to deliver this order: '))
        if Timer<=60:
            lbl1 = Label(f, text='time(secs): '+str(Timer), background='white')
            lbl1.place(x=255, y=170)
        else:
            Timer = Timer/60
            lbl1= Label(f, text='time(mins): '+str(Timer),  background='white')
            lbl1.place(x=255, y=170)
        global tic
        tic = perf_counter()
    if num==9:
        global toc
        toc = perf_counter()
        time= int(toc-tic)
        SET_TIME= Timer
        if SET_TIME>time:
             lbl1 = Label(f, text=str(int(SET_TIME-time))+'secs left ', background='white')
             lbl1.place(x=255, y=185)
        else:
            lbl1 = Label(f, text='your order has been delivered', background='white')
            lbl1.place(x=255, y=185)
    


btn1 = Button(f, width=15, height=2, text='pizza sauce', command=lambda:btn_click(0))
btn1.place(x=5, y=10)
btn2 = Button(f, width=15, height=2, text='cheese', command=lambda:btn_click(1))
btn2.place(x=5, y=55)
btn3 = Button(f, width=15, height=2, text='tomatoes', command=lambda:btn_click(2))
btn3.place(x=5, y=100)
btn4 = Button(f, width=15, height=2, text='capsicum', command=lambda:btn_click(3))
btn4.place(x=5, y=145)
btn5= Button(f, width=15, height=2, text='mushroom', command=lambda:btn_click(4))
btn5.place(x=130, y=10)
btn6= Button(f, width=15, height=2, text='olives', command=lambda:btn_click(5))
btn6.place(x=130, y=55)
btn7= Button(f, width=15, height=2, text='sweet corn', command=lambda:btn_click(6))
btn7.place(x=130, y=100)
btn8= Button(f, width=15, height=2, text='jalpeno', command=lambda:btn_click(7))
btn8.place(x=130, y=145)
e = Entry(f,  width=15)
e.place(x=255, y=10)
btn9= Button(f, width=15, height=2, text='place order', command=lambda:btn_click(8))
btn9.place(x=255, y=55)
btn10= Button(f, width=15, height=2, text='track order', command=lambda:btn_click(9))
btn10.place(x=255, y=100)
f.pack()



root.mainloop()

