from tkinter import *

#how to make a window(screen)
win = Tk()
#changing the dimentions of the window
win.geometry("600x600")

#how to make a button
btn1 = Button(win,text = "press", command=win.destroy, fg="blue", bg="green", bd=4)
#set the position of the button
btn1.pack(side = "top")





win.mainloop()


















