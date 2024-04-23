from tkinter import *
base=Tk()
base.geometry("450x1000")
base.title("Calci")
'''addB=Button(base,text="+",width=2,height=2)
addB.place(x=400,y=100)
adds=Button(base,text="-",width=2,height=2)
adds.place(x=400,y=135)
addm=Button(base,text="*",width=2,height=2)
addm.place(x=400,y=172)
addd=Button(base,text="%",width=2,height=2)
addd.place(x=400,y=209)
eq=Button(base,text="=",width=2,height=2)
eq.place(x=400,y=250)'''


addB=Button(base,text="+",width=2,height=2)
addB.grid(row=1,column=1)
adds=Button(base,text="+",width=2,height=2)
adds.grid(row=2,column=1)
addd=Button(base,text="+",width=2,height=2)
addd.grid(row=3,column=1)
addm=Button(base,text="+",width=2,height=2)
addm.grid(row=4,column=1)

base.mainloop()

