# testing

# New test.  Trying to get message box working
#Cribbed from http://www.tutorialspoint.com/python/tk_messagebox.htm
#and converted to run in Python 3.4
import tkinter


top = tkinter.Tk()
def hello():
    tkinter.messagebox.showinfo("Say Hello", "Hello World")
    pass

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
