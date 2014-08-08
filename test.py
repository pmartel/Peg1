# testing
# GUI using Tkinter
from tkinter import *

class App(Frame):
    """build the basic window frame template"""
    cb =[]
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.cb.append( Checkbutton(self, bg='brown'))
        self.cb[0].grid(row=1,column=2,sticky=N)
        self.cb.append( Checkbutton(self, bg='brown'))
        self.cb[1].grid(row=2,column=1,sticky=N)
        
        
root = Tk()

root.title( 'Test window')
root.geometry('300x100')
app = App(root)
app.mainloop()
