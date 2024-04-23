from tkinter import *  
  
top = Tk()  
  
top.geometry("200x250")  
  
lbl = Label(top,text = "A list of favourite countries...")  
  
listbox = Listbox(top)  
  
listbox.insert(1,"India")  
  
listbox.insert(2, "Uganda")  
  
listbox.insert(3, "Cambodia")  
  
listbox.insert(4, "Amazon")  
  
lbl.pack()  
listbox.pack()  
  
top.mainloop()  
