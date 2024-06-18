from tkinter import *

a = Tk()
a.title("Log in")
a.geometry("450x300")
a.config(background="red")

#creating a label
username = Label(a, text="Username").place(x=40,y=60)
password = Label(a, text="Password").place(x=40,y=100)

#creating input boxes
username_input = Entry(a, width=30).place(x=110,y=60)
password_input = Entry(a, width=30, show="*").place(x=110,y=100)

btn1 = Button(a, text="Log in")
btn1.place(x=110,y=130)




a.mainloop()





