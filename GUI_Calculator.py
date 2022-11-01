from tkinter import *
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.f = Frame(root, height=450, width=400, bg='white')
        self.f.propagate(0)
        self.f.pack()
        self.plus_btn = Button(self.f,  text='+', width=15, height=2, command=lambda:self.buttonClick('+' , 'o' ))
        self.plus_btn.place(x=290, y=250)
        self.subtraction_btn =Button(self.f,  text='-', width=15 , height=2, command=lambda:self.buttonClick('-' , 'o'))
        self.subtraction_btn.place(x=290, y=290)
        self.divide_btn = Button(self.f,  text='/', width=15 , height=2, command=lambda:self.buttonClick('/' , 'o'))
        self.divide_btn.place(x=290, y=330)
        self.multiply_btn =Button(self.f,  text='*', width=15 , height=2, command=lambda:self.buttonClick('*' , 'o'))
        self.multiply_btn.place(x=290, y=370)
        self.num_e =Button(self.f,  text='=', width=15 , height=2 , command=lambda:self.buttonClick('=', 'e'))
        self.num_e.place(x=63, y=200)
        self.num_1 =Button(self.f,  text='1', width=15 , height=2 , command=lambda:self.buttonClick('1' , 'n'))
        self.num_1.place(x=63, y=250)
        self.num_2 =Button(self.f,  text='2', width=15 , height=2 , command=lambda:self.buttonClick('2' , 'n'))
        self.num_2.place(x=176, y=250)
        self.num_3 =Button(self.f,  text='3', width=15, height=2 , command=lambda:self.buttonClick('3' , 'n'))
        self.num_3.place(x=63, y=290)
        self.num_4 =Button(self.f,  text='4', width=15 , height=2 , command=lambda:self.buttonClick('4' , 'n'))
        self.num_4.place(x=176, y=290)
        self.num_5 =Button(self.f,  text='5', width=15 , height=2 , command=lambda:self.buttonClick('5' , 'n'))
        self.num_5.place(x=63, y=330)
        self.num_6 =Button(self.f,  text='6', width=15 , height=2 , command=lambda:self.buttonClick('6' , 'n'))
        self.num_6.place(x=176, y=330)
        self.num_7 =Button(self.f,  text='7', width=15 , height=2 , command=lambda:self.buttonClick('7' , 'n'))
        self.num_7.place(x=63, y=370)
        self.num_8 =Button(self.f,  text='8', width=15 , height=2 , command=lambda:self.buttonClick('8' , 'n'))
        self.num_8.place(x=176, y=370)
        self.num_9 =Button(self.f,  text='9', width=15 , height=2 , command=lambda:self.buttonClick('9' , 'n'))
        self.num_9.place(x=63, y=410)
        self.num_0 =Button(self.f,  text='0', width=15 , height=2 , command=lambda:self.buttonClick('0' , 'n'))
        self.num_0.place(x=176, y=410)
        self.power_btn =Button(self.f,  text='^', width=15 , height=2 , command=lambda:self.buttonClick('**' , 'o'))
        self.power_btn.place(x=290, y=410)
        self.power_btn =Button(self.f,  text='AC', width=15 , height=2 , command=lambda:self.buttonClick('' , 'a'))
        self.power_btn.place(x=176, y=200)
        self.power_btn =Button(self.f,  text='pi', width=15 , height=2 , command=lambda:self.buttonClick('3.14' , 'n'))
        self.power_btn.place(x=290, y=200)
        self.operator_string=''

    def buttonClick(self, c, ty ):
        x = 0
        y = 0
        if ty =='n':
            self.operator_string += c
            self.lbl=Label(self.f, text= self.operator_string, height=2, font=100, background='white')
            self.lbl.place(x=63, y=150)
        if ty =='o':
            self.operator_string += ' '+ c +' '
            self.lbl=Label(self.f, text= self.operator_string, height=2, font=100, background='white')
            self.lbl.place(x=63, y=150)
        if ty == 'a':
            self.operator_string=''
            self.lbl=Label(self.f, text='                                             ', height=2, font=100, background='white')
            self.lbl.place(x=63, y=150)
        if ty =='e':
         if self.operator_string != ' ':
                self.lbl=Label(self.f, text='                                                                 ', height=2, font=100, background='white')
                self.lbl.place(x=63, y=150)
                self.op_str = self.operator_string.split(' ')
                if len(self.op_str) == 3: 
                    x = float(self.op_str[0])
                    y = float(self.op_str[2])
                    if self.op_str[1] == '+':
                        self.lbl=Label(self.f, text=x+y, height=2, font=100, background='white')
                        self.lbl.place(x=63, y=150)
                    if self.op_str[1] == '-':
                        self.lbl=Label(self.f, text=x-y, height=2, font=100, background='white')
                        self.lbl.place(x=63, y=150)
                    if self.op_str[1] == '*':
                        self.lbl=Label(self.f, text=x*y, height=2, font=100, background='white')
                        self.lbl.place(x=63, y=150)
                    if self.op_str[1] == '/':
                        self.lbl=Label(self.f, text=x/y, height=2, font=100, background='white')
                        self.lbl.place(x=63, y=150)
                    if self.op_str[1] == '**':
                        self.lbl=Label(self.f, text=x**y, height=2, font=100, background='white')
                        self.lbl.place(x=63, y=150)
                else:
                    self.lbl=Label(self.f, text='error, this calculator can only calculate with 2 numbers',foreground='red', background='white')
                    self.lbl.place(x=63, y=100)
                    
            
                
                
                
            
        
     


root = Tk()
setup =Calculator(root)
root.mainloop()
