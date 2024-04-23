import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Register")
root.geometry("470x1000")
username_label=tk.Label(root,text="Enter Name")
username_label.place(x=100,y=100)
username_Entry=tk.Entry(root)
username_Entry.place(x=200,y=100)
password_label=tk.Label(root,text="Enter Password")
password_label.place(x=100,y=200)
password_Entry=tk.Entry(root)
password_Entry.place(x=200,y=200)
login_button=tk.Button(root,text="Login")
login_button.place(x=200,y=300)
























root.mainloop()