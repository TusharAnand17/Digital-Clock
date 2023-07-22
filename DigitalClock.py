from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.geometry("500x60")
root.resizable(0, 0)
root.title("Digital Clock")


def gettime():
    t = strftime("%H:%M:%S")
    l.config(text=t)
    l.after(1000, gettime)


l = Label(root, background="black", foreground="white",
          font=('calibri', 40, 'bold'))
l.pack(fill=X)
gettime()

root.mainloop()
