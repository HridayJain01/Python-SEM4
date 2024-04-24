from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Calculator")
    gui.geometry("400x150")
    equation = StringVar()
    expression_feild= Entry(gui, textvariable=equation)
    expression_feild.grid(columnspan =3,ipadx=50,row=1)
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
		    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text='2' , fg='black' , bg='red',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(gui,text='3' , fg='black' , bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2,column=2)
    button4 = Button(gui,text='4' , fg='black' , bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3,column=0)
    button5 = Button(gui,text='5' , fg='black' , bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3,column=1)
    button6 = Button(gui,text='6' , fg='black' , bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3,column=2)
    button7 = Button(gui,text='7' , fg='black' , bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4,column=0)
    button8 = Button(gui,text='8' , fg='black' , bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4,column=1)
    button9 = Button(gui,text='9' , fg='black' , bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4,column=2)
    button0 = Button(gui,text='0' , fg='black' , bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5,column=0)
    buttonp = Button(gui,text='+' , fg='black' , bg='red',
                     command=lambda: press("+"), height=1, width=7)
    buttonp.grid(row=2,column=3)
    buttonm = Button(gui,text='*' , fg='black' , bg='red',
                     command=lambda: press("*"), height=1, width=7)
    buttonm.grid(row=4,column=3)
    buttonmi = Button(gui,text='-' , fg='black' , bg='red',
                     command=lambda: press("-"), height=1, width=7)
    buttonmi.grid(row=3,column=3)
    buttond = Button(gui,text='/' , fg='black' , bg='red',
                     command=lambda: press("/"), height=1, width=7)
    buttond.grid(row=5,column=3)
    buttone = Button(gui,text='=' , fg='black' , bg='red',
                     command=equal , height=1, width=7)
    buttone.grid(row=5,column=2)
    buttonc = Button(gui,text='clear' , fg='black' , bg='red',
                     command=clear, height=1, width=7)
    buttonc.grid(row=1,column=3)
    buttonde = Button(gui,text='.' , fg='black' , bg='red',
                     command=lambda: press("."), height=1, width=7)
    buttonde.grid(row=5,column=1)

    gui.mainloop()
