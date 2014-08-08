# testing
# GUI using Tkinter
from tkinter import *

class App(Frame):
    """build the basic window frame template"""
    but =[]
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.but.append( Button(self, bg='green'))
        self.but[0].grid(row=1,column=2,pady=2)
        self.but.append( Button(self, bg='brown'))
        self.but[1].grid(row=2,column=1,padx=3,pady=2)
        
        
root = Tk()

root.title( 'Test window')
root.geometry('300x100')
app = App(root)
app.mainloop()
